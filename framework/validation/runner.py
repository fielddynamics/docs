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
import traceback
from contextlib import redirect_stderr, redirect_stdout


def run_checks(validate_path):
    """Import and execute all check_ functions from the given file."""
    spec = importlib.util.spec_from_file_location("_validate_target", validate_path)
    if spec is None or spec.loader is None:
        return {
            "total": 0, "passed": 0, "failed": 0, "errors": 1,
            "checks": [{
                "name": "import_error",
                "doc": "",
                "status": "ERROR",
                "duration_ms": 0,
                "message": "Could not load module from %s" % validate_path,
                "output": "",
            }],
        }

    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
    except Exception as exc:
        tb = traceback.format_exc()
        sys.stderr.write("[IMPORT ERROR] %s\n%s\n" % (validate_path, tb))
        return {
            "total": 0, "passed": 0, "failed": 0, "errors": 1,
            "checks": [{
                "name": "import_error",
                "doc": "",
                "status": "ERROR",
                "duration_ms": 0,
                "message": "%s: %s" % (type(exc).__name__, exc),
                "output": "",
            }],
        }

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
            tb = traceback.format_exc()
            sys.stderr.write("[FAIL] %s: %s\n%s\n" % (name, exc, tb))
        except Exception as exc:
            output = stream.getvalue().strip()
            status = "ERROR"
            message = "%s: %s" % (type(exc).__name__, exc)
            tb = traceback.format_exc()
            sys.stderr.write("[ERROR] %s: %s\n%s\n" % (name, message, tb))

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

    try:
        result = run_checks(sys.argv[1])
    except Exception as exc:
        tb = traceback.format_exc()
        sys.stderr.write("[RUNNER CRASH]\n%s\n" % tb)
        result = {
            "total": 0, "passed": 0, "failed": 0, "errors": 1,
            "checks": [{
                "name": "runner_crash",
                "doc": "",
                "status": "ERROR",
                "duration_ms": 0,
                "message": "%s: %s" % (type(exc).__name__, exc),
                "output": "",
            }],
        }
    json.dump(result, sys.stdout, indent=2)
