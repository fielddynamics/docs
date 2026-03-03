"""AST-based discovery of check_ functions in validate.py files.

Parses Python source without importing or executing it, extracting
function names, docstrings, and source code for each check.
"""

import ast


def collect_checks(source_path):
    """Parse a validate.py and return metadata for each check_ function.

    Returns a list of dicts with keys:
        name, doc, source, line_start, line_end
    """
    with open(source_path, "r", encoding="utf-8") as fh:
        source = fh.read()

    source_lines = source.splitlines()
    tree = ast.parse(source, filename=source_path)

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
            if line.lower().startswith("scientific reasoning:"):
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
