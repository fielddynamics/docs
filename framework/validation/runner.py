"""Subprocess runner for validate.py check_ functions.

Imports a validate.py module, discovers check_ functions, runs each one,
and outputs structured JSON results to stdout.

Usage:
    python runner.py /path/to/validate.py
"""

import importlib.util
import io
import inspect
import json
import sys
import time
from contextlib import redirect_stderr, redirect_stdout


def run_checks(validate_path):
    """Import and execute all check_ functions from the given file."""
    spec = importlib.util.spec_from_file_location("_validate_target", validate_path)
    if spec is None or spec.loader is None:
        return {
            "error": "Could not load module from %s" % validate_path,
            "total": 0,
            "passed": 0,
            "failed": 0,
            "errors": 0,
            "checks": [],
        }

    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    check_fns = sorted(
        (name, fn)
        for name, fn in inspect.getmembers(mod, inspect.isfunction)
        if name.startswith("check_")
    )

    results = []
    for name, fn in check_fns:
        doc = (fn.__doc__ or "").strip()
        t0 = time.perf_counter()
        output = ""
        try:
            stream = io.StringIO()
            with redirect_stdout(stream), redirect_stderr(stream):
                fn()
            output = stream.getvalue().strip()
            status = "PASS"
            message = ""
        except AssertionError as exc:
            output = stream.getvalue().strip()
            status = "FAIL"
            message = str(exc)
        except Exception as exc:
            output = stream.getvalue().strip()
            status = "ERROR"
            message = "%s: %s" % (type(exc).__name__, exc)

        duration_ms = round((time.perf_counter() - t0) * 1000, 2)
        results.append({
            "name": name,
            "doc": doc,
            "status": status,
            "duration_ms": duration_ms,
            "message": message,
            "output": output,
        })

    return {
        "total": len(results),
        "passed": sum(1 for r in results if r["status"] == "PASS"),
        "failed": sum(1 for r in results if r["status"] == "FAIL"),
        "errors": sum(1 for r in results if r["status"] == "ERROR"),
        "checks": results,
    }


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write("Usage: python runner.py <validate.py path>\n")
        sys.exit(2)

    result = run_checks(sys.argv[1])
    json.dump(result, sys.stdout, indent=2)
