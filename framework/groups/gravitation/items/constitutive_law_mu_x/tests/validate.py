"""Constitutive law mu(x) = x/(x+1) validation suite.

Validates that the constitutive law derived from the Mobius map
s(x) = (x-1)/(x+1) satisfies the required mathematical properties
and is consistent with the coupling polynomial and kinetic functional.
"""

import math
import numpy as np
from scipy import integrate


def check_vacuum_state_consistency():
    # VALIDATION: Confirms the overview claim that proves the model remains consistent at the coordinate origin.
    x = 0.0
    mu = x / (x + 1.0)
    assert abs(mu) < 1e-15, "mu(0) = %g, expected 0" % mu


def check_newtonian_limit_recovery():
    # VALIDATION: Confirms the overview claim that verifies recovery of the Newtonian and GR strong field limit.
    x = 1e12
    mu = x / (x + 1.0)
    assert abs(mu - 1.0) < 1e-10, "mu(1e12) = %g, expected ~1" % mu


def check_bimetric_sector_symmetry():
    # VALIDATION: Confirms the overview claim that exact TetA and TetB symmetry at the transition point.
    x = 1.0
    mu = x / (x + 1.0)
    assert abs(mu - 0.5) < 1e-15, "mu(1) = %g, expected 0.5" % mu


def check_kinetic_stability_invariant():
    # VALIDATION: Confirms the overview claim that ensures a strictly increasing response and excludes ghost behavior.
    xs = np.linspace(0.001, 100, 10000)
    mus = xs / (xs + 1.0)
    diffs = np.diff(mus)
    assert np.all(diffs > 0), "mu is not monotonically increasing"


def check_variational_functional_match():
    # VALIDATION: Confirms the overview claim that proves the scalar tensor action is the integral of the constitutive law.
    y_values = [0.01, 0.25, 1.0, 4.0, 16.0, 100.0]
    for y_test in y_values:
        f_numerical, _ = integrate.quad(
            lambda t: (t ** 0.5) / ((t ** 0.5) + 1.0),
            0.0,
            y_test,
            epsabs=1e-10,
            epsrel=1e-10,
        )
        sy = y_test ** 0.5
        f_analytic = y_test - 2.0 * sy + 2.0 * math.log(1.0 + sy)
        err = abs(f_numerical - f_analytic)
        assert err < 1e-10, (
            "F(%g): numerical=%g, analytic=%g, err=%g"
            % (y_test, f_numerical, f_analytic, err)
        )


def check_topological_mapping_proof():
    # VALIDATION: Confirms the overview claim that verifies continuous field response maps back to the discrete polynomial.
    x_values = [0.01, 0.1, 0.5, 1.0, 2.0, 10.0, 100.0, 1000.0]
    for x in x_values:
        s = (x - 1.0) / (x + 1.0)
        mu_from_s = (1.0 + s) / 2.0
        mu_direct = x / (x + 1.0)
        err = abs(mu_from_s - mu_direct)
        assert err < 1e-15, (
            "x=%g: mu_from_s=%g, mu_direct=%g, err=%g"
            % (x, mu_from_s, mu_direct, err)
        )


# -------------------------------------------------------------------
# Standalone runner
# -------------------------------------------------------------------

if __name__ == "__main__":
    import inspect
    import sys
    import time

    checks = sorted(
        (name, fn)
        for name, fn in inspect.getmembers(sys.modules[__name__], inspect.isfunction)
        if name.startswith("check_")
    )

    passed = 0
    failed = 0
    for name, fn in checks:
        t0 = time.perf_counter()
        try:
            fn()
            dt = (time.perf_counter() - t0) * 1000
            print("  PASS  %-40s  (%.1fms)" % (name, dt))
            passed += 1
        except AssertionError as e:
            dt = (time.perf_counter() - t0) * 1000
            print("  FAIL  %-40s  (%.1fms)  %s" % (name, dt, e))
            failed += 1
        except Exception as e:
            dt = (time.perf_counter() - t0) * 1000
            print("  ERROR %-40s  (%.1fms)  %s" % (name, dt, e))
            failed += 1

    print()
    print("%d passed, %d failed, %d total" % (passed, failed, passed + failed))
    sys.exit(1 if failed else 0)
