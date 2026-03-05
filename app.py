"""
Field Dynamics Documentation Suite
Flask application factory.

Serves the frontend (Jinja2 templates + static assets) and framework content API.
Server-side renders the initial page load so that AI crawlers, search engines,
and View Page Source all receive the full article content in the HTML document.

Supports framework-level versioning via /v{major.minor}/framework/ URL prefix.
Archived versions are served from frozen framework-v{X.Y}/ snapshot directories.

Usage:
    python app.py                            # Development server
    gunicorn --bind 0.0.0.0:8000 app:app     # Azure / production
"""

__version__ = "1.0"

import ast
import json
import os
import re
import subprocess
import sys

import latex2mathml.converter
import markdown as md_lib
from flask import (
    Flask,
    Response,
    abort,
    jsonify,
    render_template,
    request,
    send_from_directory,
)

# ---------------------------------------------------------------------------
# Navigation registry
# ---------------------------------------------------------------------------

NAV_GROUPS = {
    "foundations": [
        "the_gravity_field",
        "field_closure_principle",
        "why_k4_d3",
        "dual_tetrahedron_field_origin",
        "propagation_requires_neighbors",
        "field_closure_in_gr",
        "characteristic_scale",
        "face_structure_and_spin",
        "twenty_eight_geometric_elements",
        "stellated_octahedron",
    ],
    "gravitation": [
        "coupling_polynomial_structural_states",
        "g_from_topology",
        "constitutive_law_mu_x",
        "poisson_scale_invariance",
        "covariant_completion",
        "bimetric_locking",
        "weak_strong_field_limits",
        "lensing_time_delay",
        "thermodynamic_relations",
        "action_prefactor_dictionary",
    ],
    "fundamental_constants": [
        "fine_structure_constant_alpha",
        "electron_mass",
        "electron_spin",
        "inverse_square_emc2_force_hierarchy",
        "h0_prediction",
        "capstone_constants_suite",
    ],
    "matter_nuclear_physics": [
        "nuclear_synthesis_bridge",
        "magic_numbers_shells",
        "binding_energy_envelope",
        "heavy_end_honest_failure",
        "resonance_modes",
        "stability_ceiling",
    ],
    "gauge_particle_physics": [
        "electromagnetic_sector",
        "strong_sector_structure",
        "weak_sector_parity",
        "particle_inventory",
        "generation_logic",
        "mass_hierarchy",
    ],
    "quantum_theory": [
        "born_rule_origin",
        "measurement_mechanism",
        "entanglement_structure",
        "decoherence_timescale",
    ],
    "cosmology": [
        "expansion_history",
        "dark_sector_alternative",
        "nucleosynthesis_tensions",
        "cmb_constraints",
        "structure_growth",
    ],
}

ITEM_TO_GROUP = {}
for _gid, _items in NAV_GROUPS.items():
    for _iid in _items:
        ITEM_TO_GROUP[_iid] = _gid

_VERSION_RE = re.compile(r"^\d+\.\d+$")
_SAFE_ID_RE = re.compile(r"^[a-z0-9_]+$")


# ---------------------------------------------------------------------------
# Versioning helpers
# ---------------------------------------------------------------------------

def _read_manifest_version(framework_root):
    """Read the version string from manifest.yaml under the framework root."""
    manifest_path = os.path.join(framework_root, "manifest.yaml")
    if os.path.isfile(manifest_path):
        with open(manifest_path, "r", encoding="utf-8") as fh:
            for line in fh:
                m = re.match(r'^version:\s*"?(\d+\.\d+)"?\s*$', line.strip())
                if m:
                    return m.group(1)
    return "1.0"


def _scan_archived_versions(app_root):
    """Find all framework-v{X.Y}/ directories on disk."""
    versions = set()
    if not os.path.isdir(app_root):
        return versions
    for name in os.listdir(app_root):
        m = re.match(r"^framework-v(\d+\.\d+)$", name)
        if m and os.path.isdir(os.path.join(app_root, name)):
            versions.add(m.group(1))
    return versions


def _find_item_group(framework_root, item_id):
    """Find which group an item belongs to by scanning the directory tree."""
    groups_dir = os.path.join(framework_root, "groups")
    if not os.path.isdir(groups_dir):
        return None
    for group_name in os.listdir(groups_dir):
        item_dir = os.path.join(groups_dir, group_name, "items", item_id)
        if os.path.isdir(item_dir):
            return group_name
    return None


# ---------------------------------------------------------------------------
# Server-side Markdown rendering
# ---------------------------------------------------------------------------

_MD = md_lib.Markdown(
    extensions=["tables", "fenced_code"],
)


def _latex_to_mathml(latex_src, display=False):
    """Convert a LaTeX string to MathML, falling back to raw LaTeX on error."""
    try:
        mathml = latex2mathml.converter.convert(latex_src)
        if display:
            mathml = mathml.replace('display="inline"', 'display="block"', 1)
        return mathml
    except Exception:
        if display:
            return "<p>$$" + latex_src + "$$</p>"
        return "$" + latex_src + "$"


def _convert_math_blocks(html):
    """Replace $$...$$ and $...$ with MathML in rendered HTML."""
    html = re.sub(
        r"\$\$\s*(.+?)\s*\$\$",
        lambda m: _latex_to_mathml(m.group(1), display=True),
        html,
        flags=re.DOTALL,
    )
    html = re.sub(
        r"(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)",
        lambda m: _latex_to_mathml(m.group(1), display=False),
        html,
    )
    return html


def render_markdown_to_html(raw_md):
    """Convert a markdown string to HTML with math rendered as MathML."""
    _MD.reset()
    html = _MD.convert(raw_md)
    html = _convert_math_blocks(html)
    return html


def extract_page_meta(raw_md):
    """Pull the H1 title and a plain-text description from raw markdown."""
    title_match = re.match(r"^#\s+(.+)$", raw_md, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else ""

    desc_parts = []
    for line in raw_md.split("\n"):
        s = line.strip()
        if not s or s.startswith("#") or s.startswith("$$") or s.startswith("|"):
            if desc_parts:
                break
            continue
        desc_parts.append(s)

    description = " ".join(desc_parts)
    description = re.sub(r"\*\*([^\*]+)\*\*", r"\1", description)
    description = re.sub(r"\*([^\*]+)\*", r"\1", description)
    description = re.sub(r"\$[^\$]+\$", "", description)
    description = re.sub(r"\s+", " ", description).strip()
    return title, description[:300]


def _read_item_overview(framework_root, group_id, item_id):
    """Read overview.md for an item and return (html, title, description)
    or (None, None, None) if the file does not exist."""
    item_dir = os.path.join(
        framework_root, "groups", group_id, "items", item_id
    )
    overview_path = os.path.join(item_dir, "overview.md")
    if not os.path.isfile(overview_path):
        return None, None, None
    with open(overview_path, "r", encoding="utf-8") as fh:
        raw_md = fh.read()
    html = render_markdown_to_html(raw_md)
    title, description = extract_page_meta(raw_md)
    return html, title, description


def _resolve_item_dir(framework_root, group_id, item_id):
    """Build the absolute path to an item directory within a framework root."""
    return os.path.join(
        framework_root, "groups", group_id, "items", item_id
    )

def _clean_yaml_value(raw_value):
    value = raw_value.strip()
    if len(value) >= 2 and value[0] in ("'", '"') and value[-1] == value[0]:
        value = value[1:-1]
    return value


def _normalize_validation_description(rel_path, raw_description):
    """Return a consistent, user-facing description for validation files."""
    description = (raw_description or "").strip()
    placeholder = "Placeholder validation for this item."
    if description and description != placeholder:
        return description

    normalized_path = rel_path.replace("\\", "/").strip()
    filename = os.path.basename(normalized_path).lower()
    if filename == "validate.py":
        return "Overview validation for this item."
    if filename.startswith("validate-") and filename.endswith(".py"):
        label = filename[len("validate-") : -len(".py")].replace("_", " ").strip()
        if label:
            return "Validation extension: {}.".format(label)
    return "Validation for this item."


def _read_validation_entries(item_dir):
    """Read validation file entries from item.yaml or discover validate files."""
    entries = []
    item_yaml = os.path.join(item_dir, "item.yaml")
    if os.path.isfile(item_yaml):
        in_tests = False
        in_entrypoints = False
        with open(item_yaml, "r", encoding="utf-8") as handle:
            for raw_line in handle:
                line = raw_line.rstrip("\n")
                stripped = line.strip()
                if not stripped or stripped.startswith("#"):
                    continue
                if re.match(r"^tests:\s*$", stripped):
                    in_tests = True
                    in_entrypoints = False
                    continue
                if in_tests:
                    if not line.startswith("  "):
                        in_tests = False
                        in_entrypoints = False
                        continue
                    match = re.match(r"^\s*entrypoint:\s*(.+)$", stripped)
                    if match:
                        path = _clean_yaml_value(match.group(1))
                        entries.append({"path": path, "description": ""})
                        continue
                    match = re.match(r"^\s*description:\s*(.+)$", stripped)
                    if match and entries:
                        entries[-1]["description"] = _clean_yaml_value(match.group(1))
                        continue
                    if re.match(r"^\s*entrypoints:\s*$", stripped):
                        in_entrypoints = True
                        continue
                    if in_entrypoints:
                        if not line.startswith("    "):
                            in_entrypoints = False
                            continue
                        match = re.match(r"^\s*-\s*path:\s*(.+)$", stripped)
                        if match:
                            entries.append({
                                "path": _clean_yaml_value(match.group(1)),
                                "description": "",
                            })
                            continue
                        match = re.match(r"^\s*-\s*(tests\/[^\s#]+\.py)$", stripped)
                        if match:
                            entries.append({
                                "path": _clean_yaml_value(match.group(1)),
                                "description": "",
                            })
                            continue
                        match = re.match(r"^\s*path:\s*(.+)$", stripped)
                        if match and entries:
                            entries[-1]["path"] = _clean_yaml_value(match.group(1))
                            continue
                        match = re.match(r"^\s*description:\s*(.+)$", stripped)
                        if match and entries:
                            entries[-1]["description"] = _clean_yaml_value(match.group(1))
                            continue

    if not entries:
        tests_dir = os.path.join(item_dir, "tests")
        if os.path.isdir(tests_dir):
            validate_files = sorted(
                name for name in os.listdir(tests_dir)
                if name.startswith("validate") and name.endswith(".py")
            )
            for name in validate_files:
                entries.append({"path": "tests/" + name, "description": ""})

    resolved = []
    for entry in entries:
        rel_path = entry.get("path", "").lstrip("./")
        if not rel_path:
            continue
        abs_path = os.path.join(item_dir, rel_path.replace("/", os.sep))
        if os.path.isfile(abs_path):
            resolved.append({
                "path": rel_path,
                "description": _normalize_validation_description(
                    rel_path, entry.get("description", "")
                ),
            })
    return resolved


def _read_item_visibility(item_dir):
    """Read optional top-level visible flag from item.yaml."""
    item_yaml = os.path.join(item_dir, "item.yaml")
    if not os.path.isfile(item_yaml):
        return True

    with open(item_yaml, "r", encoding="utf-8") as handle:
        for raw_line in handle:
            stripped = raw_line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            match = re.match(r"^visible:\s*(true|false)\s*$", stripped, re.IGNORECASE)
            if match:
                return match.group(1).lower() == "true"
    return True


def _collect_hidden_nav_item_ids(framework_root):
    """Collect item IDs marked as visible: false for nav rendering."""
    hidden_item_ids = []
    for group_id, item_ids in NAV_GROUPS.items():
        for item_id in item_ids:
            item_dir = _resolve_item_dir(framework_root, group_id, item_id)
            if not os.path.isdir(item_dir):
                continue
            if not _read_item_visibility(item_dir):
                hidden_item_ids.append(item_id)
    return hidden_item_ids


# ---------------------------------------------------------------------------
# Validation: AST-based check discovery
# ---------------------------------------------------------------------------

def _collect_checks(validate_path):
    """Parse a validate.py with AST and return check_ function metadata."""
    with open(validate_path, "r", encoding="utf-8") as fh:
        source = fh.read()

    source_lines = source.splitlines()
    tree = ast.parse(source, filename=validate_path)

    checks = []
    for node in ast.iter_child_nodes(tree):
        if not isinstance(node, ast.FunctionDef):
            continue
        if not node.name.startswith("check_"):
            continue

        doc = ast.get_docstring(node) or ""
        start = node.lineno - 1
        end_line = node.end_lineno or node.lineno
        fn_source = "\n".join(source_lines[start:end_line])
        reasoning = ""
        comment_lines = []
        comment_idx = start - 1
        while comment_idx >= 0:
            raw_line = source_lines[comment_idx]
            stripped = raw_line.strip()
            if stripped.startswith("#"):
                comment_lines.insert(0, stripped.lstrip("#").strip())
                comment_idx -= 1
                continue
            if stripped == "" and comment_lines:
                break
            if stripped == "":
                comment_idx -= 1
                continue
            break

        for line in comment_lines:
            lower = line.lower()
            if lower.startswith("scientific reasoning:"):
                reasoning = line.split(":", 1)[1].strip()
                break
        if not reasoning and comment_lines:
            reasoning = " ".join(comment_lines).strip()

        checks.append({
            "name": node.name,
            "doc": doc,
            "reasoning": reasoning,
            "source": fn_source,
            "line_start": node.lineno,
            "line_end": end_line,
        })

    return checks


_RUNNER_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "framework", "validation", "runner.py",
)


# ---------------------------------------------------------------------------
# Application factory
# ---------------------------------------------------------------------------

def create_app():
    """Application factory for Field Dynamics docs app."""
    app = Flask(
        __name__,
        static_folder="static",
        template_folder="templates",
    )

    framework_root = os.path.join(app.root_path, "framework")
    fw_version = _read_manifest_version(framework_root)
    archived_versions = _scan_archived_versions(app.root_path)

    @app.context_processor
    def inject_version():
        return {"version": __version__}

    # ------------------------------------------------------------------
    # Shared rendering helper
    # ------------------------------------------------------------------

    def _render_framework_page(framework_root, item_id, viewing_version=""):
        """Common rendering logic for latest and versioned framework pages."""
        ssr_html = ""
        ssr_title = ""
        ssr_description = ""
        ssr_group_id = ""
        hidden_nav_item_ids = _collect_hidden_nav_item_ids(framework_root)

        if item_id:
            if viewing_version:
                ssr_group_id = _find_item_group(framework_root, item_id) or ""
            else:
                ssr_group_id = ITEM_TO_GROUP.get(item_id, "")

            if ssr_group_id:
                html, title, desc = _read_item_overview(
                    framework_root, ssr_group_id, item_id
                )
                if html is not None:
                    ssr_html = html
                    ssr_title = title
                    ssr_description = desc

        return render_template(
            "framework.html",
            active_page="framework",
            initial_item_id=item_id or "",
            ssr_content_html=ssr_html,
            ssr_title=ssr_title,
            ssr_description=ssr_description,
            ssr_group_id=ssr_group_id,
            hidden_nav_item_ids=hidden_nav_item_ids,
            framework_version=fw_version,
            viewing_version=viewing_version,
        )

    # ------------------------------------------------------------------
    # Shared API helper
    # ------------------------------------------------------------------

    def _serve_item_doc(framework_root, group_id, item_id, doc_kind):
        """Serve a content document from the given framework root."""
        if not _SAFE_ID_RE.match(group_id) or not _SAFE_ID_RE.match(item_id):
            abort(404)

        item_dir = _resolve_item_dir(framework_root, group_id, item_id)
        if not os.path.isdir(item_dir):
            abort(404)

        if doc_kind == "overview":
            filename = "overview.md"
            if not os.path.isfile(os.path.join(item_dir, filename)):
                abort(404)
            return send_from_directory(item_dir, filename, mimetype="text/markdown")

        if doc_kind == "examples":
            filename = "examples.md"
            if not os.path.isfile(os.path.join(item_dir, filename)):
                abort(404)
            return send_from_directory(item_dir, filename, mimetype="text/markdown")

        if doc_kind == "validation":
            entries = _read_validation_entries(item_dir)
            if not entries:
                abort(404)
            blocks = ["# Validation", ""]
            for entry in entries:
                rel_path = "groups/{}/items/{}/{}".format(
                    group_id, item_id, entry["path"]
                )
                abs_path = os.path.join(item_dir, entry["path"].replace("/", os.sep))
                with open(abs_path, "r", encoding="utf-8") as handle:
                    code = handle.read().rstrip()
                blocks.extend([
                    "## {}".format(entry["path"]),
                    "",
                    "`{}`".format(rel_path),
                    "",
                    "```python",
                    code,
                    "```",
                    "",
                ])
            return Response("\n".join(blocks), mimetype="text/markdown")

        abort(404)

    def _serve_item_meta(framework_root, group_id, item_id):
        """Serve item metadata from the given framework root."""
        if not _SAFE_ID_RE.match(group_id) or not _SAFE_ID_RE.match(item_id):
            abort(404)

        item_dir = _resolve_item_dir(framework_root, group_id, item_id)
        if not os.path.isdir(item_dir):
            abort(404)

        tabs = {"overview": True, "examples": False, "validation": True}
        item_yaml = os.path.join(item_dir, "item.yaml")
        if os.path.isfile(item_yaml):
            in_tabs_section = False
            with open(item_yaml, "r", encoding="utf-8") as handle:
                for raw_line in handle:
                    line = raw_line.rstrip("\n")
                    stripped = line.strip()
                    if not stripped or stripped.startswith("#"):
                        continue
                    if re.match(r"^tabs:\s*$", stripped):
                        in_tabs_section = True
                        continue
                    if in_tabs_section:
                        if not line.startswith("  "):
                            in_tabs_section = False
                            continue
                        match = re.match(
                            r"^\s*(overview|examples|validation):\s*(true|false)\s*$",
                            stripped,
                            re.IGNORECASE,
                        )
                        if match:
                            tab_name = match.group(1).lower()
                            tabs[tab_name] = match.group(2).lower() == "true"

        tabs["examples"] = False
        validation_entries = _read_validation_entries(item_dir)
        return jsonify({
            "groupId": group_id,
            "itemId": item_id,
            "tabs": tabs,
            "validationFiles": validation_entries,
        })

    def _serve_item_checks(framework_root, group_id, item_id):
        """Collect check_ metadata from validate.py via AST (no execution)."""
        if not _SAFE_ID_RE.match(group_id) or not _SAFE_ID_RE.match(item_id):
            abort(404)
        item_dir = _resolve_item_dir(framework_root, group_id, item_id)
        entries = _read_validation_entries(item_dir)
        if not entries:
            return jsonify({"groups": []})
        groups = []
        for entry in entries:
            validate_path = os.path.join(item_dir, entry["path"].replace("/", os.sep))
            checks = _collect_checks(validate_path)
            groups.append({
                "path": entry["path"],
                "description": entry.get("description", ""),
                "checks": checks,
            })
        return jsonify({"groups": groups})

    def _run_item_checks(framework_root, group_id, item_id):
        """Run check_ functions from validate.py in a subprocess."""
        if not _SAFE_ID_RE.match(group_id) or not _SAFE_ID_RE.match(item_id):
            abort(404)
        item_dir = _resolve_item_dir(framework_root, group_id, item_id)
        entries = _read_validation_entries(item_dir)
        if not entries:
            return jsonify({
                "total": 0,
                "passed": 0,
                "failed": 0,
                "errors": 0,
                "groups": [],
            })

        total = 0
        passed = 0
        failed = 0
        errors = 0
        groups = []

        for entry in entries:
            validate_path = os.path.join(item_dir, entry["path"].replace("/", os.sep))
            try:
                result = subprocess.run(
                    [sys.executable, _RUNNER_PATH, validate_path],
                    capture_output=True,
                    text=True,
                    timeout=120,
                )
                if result.stderr:
                    app.logger.warning(
                        "Runner stderr for %s:\n%s",
                        entry["path"], result.stderr.strip(),
                    )
                report = json.loads(result.stdout)
            except subprocess.TimeoutExpired:
                app.logger.error("Runner timeout for %s", entry["path"])
                report = {
                    "total": 0,
                    "passed": 0,
                    "failed": 0,
                    "errors": 1,
                    "checks": [{
                        "name": "timeout",
                        "doc": "",
                        "status": "ERROR",
                        "duration_ms": 120000,
                        "message": "Execution timed out after 120 seconds",
                        "output": "",
                    }],
                }
            except json.JSONDecodeError:
                stderr_text = (getattr(result, "stderr", "") or "").strip()
                stdout_text = (getattr(result, "stdout", "") or "").strip()
                msg = stderr_text or stdout_text or "Runner produced no output"
                app.logger.error(
                    "Runner JSON error for %s:\n%s", entry["path"], msg,
                )
                report = {
                    "total": 0,
                    "passed": 0,
                    "failed": 0,
                    "errors": 1,
                    "checks": [{
                        "name": "runner_error",
                        "doc": "",
                        "status": "ERROR",
                        "duration_ms": 0,
                        "message": msg,
                        "output": "",
                    }],
                }
            except Exception as exc:
                msg = "%s: %s" % (type(exc).__name__, exc)
                app.logger.error(
                    "Runner exception for %s: %s", entry["path"], msg,
                )
                report = {
                    "total": 0,
                    "passed": 0,
                    "failed": 0,
                    "errors": 1,
                    "checks": [{
                        "name": "runner_error",
                        "doc": "",
                        "status": "ERROR",
                        "duration_ms": 0,
                        "message": msg,
                        "output": "",
                    }],
                }

            total += report.get("total", 0)
            passed += report.get("passed", 0)
            failed += report.get("failed", 0)
            errors += report.get("errors", 0)
            groups.append({
                "path": entry["path"],
                "description": entry.get("description", ""),
                "total": report.get("total", 0),
                "passed": report.get("passed", 0),
                "failed": report.get("failed", 0),
                "errors": report.get("errors", 0),
                "checks": report.get("checks", []),
            })

        return jsonify({
            "total": total,
            "passed": passed,
            "failed": failed,
            "errors": errors,
            "groups": groups,
        })

    def _serve_global_image(filename):
        """Serve files from docs/images/."""
        images_dir = os.path.join(app.root_path, "images")
        if not os.path.isdir(images_dir):
            abort(404)
        return send_from_directory(images_dir, filename)

    def _serve_item_asset(framework_root, group_id, item_id, filename):
        """Serve files from groups/<group>/items/<item>/assets/."""
        if not _SAFE_ID_RE.match(group_id) or not _SAFE_ID_RE.match(item_id):
            abort(404)
        item_dir = _resolve_item_dir(framework_root, group_id, item_id)
        if not os.path.isdir(item_dir):
            abort(404)
        item_assets_dir = os.path.join(item_dir, "assets")
        if not os.path.isdir(item_assets_dir):
            abort(404)
        if filename.endswith(".html"):
            return send_from_directory(item_assets_dir, filename,
                                       mimetype="text/html")
        return send_from_directory(item_assets_dir, filename)

    # ------------------------------------------------------------------
    # SEO and AI discovery
    # ------------------------------------------------------------------

    @app.route("/sitemap.xml")
    def sitemap():
        base = "https://docs.fielddynamics.org"
        today = __import__("datetime").date.today().isoformat()
        urls = []
        urls.append({"loc": base + "/", "priority": "1.0"})
        urls.append({"loc": base + "/framework/", "priority": "0.9"})
        urls.append({"loc": base + "/tests/", "priority": "0.7"})
        for item_id, group_id in ITEM_TO_GROUP.items():
            urls.append({
                "loc": base + "/framework/" + item_id + "/",
                "priority": "0.8",
            })
            item_dir = _resolve_item_dir(framework_root, group_id, item_id)
            for entry in _read_validation_entries(item_dir):
                filename = entry["path"].replace("tests/", "")
                urls.append({
                    "loc": base + "/tests/" + group_id + "/" + item_id + "/" + filename,
                    "priority": "0.6",
                })
        lines = ['<?xml version="1.0" encoding="UTF-8"?>']
        lines.append(
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        )
        for entry in urls:
            lines.append("  <url>")
            lines.append("    <loc>%s</loc>" % entry["loc"])
            lines.append("    <lastmod>%s</lastmod>" % today)
            lines.append("    <priority>%s</priority>" % entry["priority"])
            lines.append("  </url>")
        lines.append("</urlset>")
        xml = "\n".join(lines)
        return Response(xml, mimetype="application/xml")

    @app.route("/llms.txt")
    def llms_txt():
        path = os.path.join(app.root_path, "llms.txt")
        if not os.path.isfile(path):
            abort(404)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        return Response(content, mimetype="text/plain; charset=utf-8")

    # ------------------------------------------------------------------
    # Test file routes
    # ------------------------------------------------------------------

    @app.route("/tests/")
    def tests_index():
        """Plain-text index of every validation file in the framework."""
        lines = ["# Field Dynamics Validation Tests", ""]
        for item_id, group_id in sorted(ITEM_TO_GROUP.items()):
            item_dir = _resolve_item_dir(framework_root, group_id, item_id)
            entries = _read_validation_entries(item_dir)
            if not entries:
                continue
            lines.append("## %s/%s" % (group_id, item_id))
            for entry in entries:
                filename = entry["path"].replace("tests/", "")
                url = "/tests/%s/%s/%s" % (group_id, item_id, filename)
                lines.append("  %s" % url)
            lines.append("")
        return Response("\n".join(lines), mimetype="text/plain; charset=utf-8")

    @app.route("/tests/<group_id>/<item_id>/<filename>")
    def tests_file(group_id, item_id, filename):
        """Serve a raw validation .py file as plain text."""
        if not _SAFE_ID_RE.match(group_id) or not _SAFE_ID_RE.match(item_id):
            abort(404)
        if not filename.startswith("validate") or not filename.endswith(".py"):
            abort(404)
        item_dir = _resolve_item_dir(framework_root, group_id, item_id)
        if not os.path.isdir(item_dir):
            abort(404)
        test_path = os.path.join(item_dir, "tests", filename)
        if not os.path.isfile(test_path):
            abort(404)
        with open(test_path, "r", encoding="utf-8") as f:
            content = f.read()
        return Response(content, mimetype="text/plain; charset=utf-8")

    # ------------------------------------------------------------------
    # Page routes (latest)
    # ------------------------------------------------------------------

    @app.route("/")
    def root():
        return _render_framework_page(framework_root, None)

    @app.route("/home")
    def home():
        return _render_framework_page(framework_root, None)

    @app.route("/framework")
    @app.route("/framework/")
    @app.route("/framework/<item_id>/")
    def framework(item_id=None):
        return _render_framework_page(framework_root, item_id)

    @app.route("/images/<path:filename>")
    def global_images(filename):
        return _serve_global_image(filename)

    @app.route("/framework/assets/<group_id>/<item_id>/<path:filename>")
    def framework_item_image(group_id, item_id, filename):
        return _serve_item_asset(framework_root, group_id, item_id, filename)

    # ------------------------------------------------------------------
    # Page routes (versioned)
    # ------------------------------------------------------------------

    @app.route("/v<version>/framework/")
    @app.route("/v<version>/framework/<item_id>/")
    def framework_versioned(version, item_id=None):
        if not _VERSION_RE.match(version):
            abort(404)
        if version not in archived_versions:
            abort(404)
        fw_root = os.path.join(app.root_path, "framework-v" + version)
        if not os.path.isdir(fw_root):
            abort(404)
        return _render_framework_page(fw_root, item_id, viewing_version=version)

    @app.route("/v<version>/framework/assets/<group_id>/<item_id>/<path:filename>")
    def framework_item_image_versioned(version, group_id, item_id, filename):
        if not _VERSION_RE.match(version) or version not in archived_versions:
            abort(404)
        fw_root = os.path.join(app.root_path, "framework-v" + version)
        if not os.path.isdir(fw_root):
            abort(404)
        return _serve_item_asset(fw_root, group_id, item_id, filename)

    # ------------------------------------------------------------------
    # Content API (latest)
    # ------------------------------------------------------------------

    @app.route("/api/framework/item/<group_id>/<item_id>/<doc_kind>")
    def framework_item_doc(group_id, item_id, doc_kind):
        return _serve_item_doc(framework_root, group_id, item_id, doc_kind)

    @app.route("/api/framework/item-meta/<group_id>/<item_id>")
    def framework_item_meta(group_id, item_id):
        return _serve_item_meta(framework_root, group_id, item_id)

    # ------------------------------------------------------------------
    # Validation checks API (latest)
    # ------------------------------------------------------------------

    @app.route("/api/framework/item/<group_id>/<item_id>/checks")
    def framework_item_checks(group_id, item_id):
        return _serve_item_checks(framework_root, group_id, item_id)

    @app.route(
        "/api/framework/item/<group_id>/<item_id>/checks/run",
        methods=["POST"],
    )
    def framework_item_checks_run(group_id, item_id):
        return _run_item_checks(framework_root, group_id, item_id)

    # ------------------------------------------------------------------
    # Content API (versioned)
    # ------------------------------------------------------------------

    @app.route("/api/v<version>/framework/item/<group_id>/<item_id>/<doc_kind>")
    def framework_item_doc_versioned(version, group_id, item_id, doc_kind):
        if not _VERSION_RE.match(version) or version not in archived_versions:
            abort(404)
        fw_root = os.path.join(app.root_path, "framework-v" + version)
        if not os.path.isdir(fw_root):
            abort(404)
        return _serve_item_doc(fw_root, group_id, item_id, doc_kind)

    @app.route("/api/v<version>/framework/item-meta/<group_id>/<item_id>")
    def framework_item_meta_versioned(version, group_id, item_id):
        if not _VERSION_RE.match(version) or version not in archived_versions:
            abort(404)
        fw_root = os.path.join(app.root_path, "framework-v" + version)
        if not os.path.isdir(fw_root):
            abort(404)
        return _serve_item_meta(fw_root, group_id, item_id)

    return app


# Module-level app object required for gunicorn (e.g. gunicorn app:app).
# Harmless when running directly via python app.py.
app = create_app()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "1") == "1"
    app.run(debug=debug, host="0.0.0.0", port=port)
