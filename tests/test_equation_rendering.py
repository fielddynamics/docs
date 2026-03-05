"""Smoke tests for the server-side rendering pipeline.

Verifies that every $$...$$ and $...$ block in every overview.md survives
the latex2mathml conversion and appears as <math> in the rendered HTML.
If any equation falls back to raw dollar signs, the test fails and names
the file and the offending LaTeX source.

Run:
    cd docs
    python -m pytest tests/test_equation_rendering.py -v
"""

import os
import re
import sys

import pytest

DOCS_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, DOCS_ROOT)

from app import render_markdown_to_html  # noqa: E402

FRAMEWORK_DIR = os.path.join(DOCS_ROOT, "framework")

DISPLAY_RE = re.compile(r"\$\$\s*(.+?)\s*\$\$", re.DOTALL)
INLINE_RE = re.compile(r"(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)")


def _collect_overviews():
    """Yield (relative_path, absolute_path) for every overview.md."""
    for root, _dirs, files in os.walk(FRAMEWORK_DIR):
        for fn in files:
            if fn == "overview.md":
                abs_path = os.path.join(root, fn)
                rel_path = os.path.relpath(abs_path, DOCS_ROOT)
                yield rel_path, abs_path


def _extract_latex_blocks(raw_md):
    """Return a list of (kind, latex_source) from the markdown."""
    blocks = []
    for m in DISPLAY_RE.finditer(raw_md):
        blocks.append(("display", m.group(1).strip()))
    stripped = DISPLAY_RE.sub("", raw_md)
    for m in INLINE_RE.finditer(stripped):
        blocks.append(("inline", m.group(1).strip()))
    return blocks


OVERVIEWS = list(_collect_overviews())


@pytest.mark.parametrize(
    "rel_path,abs_path",
    OVERVIEWS,
    ids=[o[0] for o in OVERVIEWS],
)
def test_overview_equations_render(rel_path, abs_path):
    """Every LaTeX block must produce <math> in the SSR output."""
    with open(abs_path, "r", encoding="utf-8") as fh:
        raw_md = fh.read()

    latex_blocks = _extract_latex_blocks(raw_md)
    if not latex_blocks:
        pytest.skip("no equations in %s" % rel_path)

    html = render_markdown_to_html(raw_md)

    math_count = html.count("<math")
    fallback_display = html.count("$$")
    fallback_inline_dollars = 0
    for m in re.finditer(r"(?<!</math>)\$(?!\$)", html):
        fallback_inline_dollars += 1

    failures = []
    if fallback_display > 0:
        remaining = re.findall(r"\$\$(.+?)\$\$", html, re.DOTALL)
        for src in remaining:
            failures.append("DISPLAY fallback: %s" % src.strip()[:80])

    assert not failures, (
        "%s has %d equation(s) that fell back to raw LaTeX:\n  %s"
        % (rel_path, len(failures), "\n  ".join(failures))
    )

    assert math_count >= len(latex_blocks), (
        "%s: expected >= %d <math> elements, found %d. "
        "Some equations may have been silently dropped."
        % (rel_path, len(latex_blocks), math_count)
    )


@pytest.mark.parametrize(
    "rel_path,abs_path",
    OVERVIEWS,
    ids=[o[0] for o in OVERVIEWS],
)
def test_overview_no_empty_equations(rel_path, abs_path):
    """No overview should contain empty $$$$ blocks."""
    with open(abs_path, "r", encoding="utf-8") as fh:
        raw_md = fh.read()

    empties = re.findall(r"\$\$[ \t]*\n?[ \t]*\$\$", raw_md)
    assert not empties, (
        "%s contains %d empty display equation block(s)" % (rel_path, len(empties))
    )
