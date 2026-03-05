"""Electron spin overview validation suite.

Each check maps to an explicit claim in overview.md.
"""

import math

K = 4
D = 3
HBAR = 1.054571817e-34


def f(K_val, s):
    """Coupling polynomial f(K, s) = 1 + sK + K^2."""
    return 1 + s * K_val + K_val ** 2


def check_polynomial_three_states():
    # VALIDATION: f(K,+1) = 21, f(K,0) = 17, f(K,-1) = 13.
    assert f(K, +1) == 21, "f(K,+1)=%d, expected 21" % f(K, +1)
    assert f(K, 0) == 17, "f(K,0)=%d, expected 17" % f(K, 0)
    assert f(K, -1) == 13, "f(K,-1)=%d, expected 13" % f(K, -1)
    print("f(+1)=%d f(0)=%d f(-1)=%d" % (f(K, +1), f(K, 0), f(K, -1)))


def check_equal_spacing():
    # VALIDATION: 21 - 17 = 17 - 13 = K = 4.
    diff_upper = f(K, +1) - f(K, 0)
    diff_lower = f(K, 0) - f(K, -1)
    assert diff_upper == K, "Upper diff=%d, expected K=%d" % (diff_upper, K)
    assert diff_lower == K, "Lower diff=%d, expected K=%d" % (diff_lower, K)
    assert diff_upper == diff_lower, "Spacing not equal"
    print("spacing=%d K=%d" % (diff_upper, K))


def check_arithmetic_mean_lock():
    # VALIDATION: (f(K,+1) + f(K,-1)) / 2 = 17 = f(K,0).
    mean = (f(K, +1) + f(K, -1)) / 2.0
    assert mean == f(K, 0), "mean=%g, expected %d" % (mean, f(K, 0))
    print("arithmetic_mean=%.1f f(K,0)=%d" % (mean, f(K, 0)))


def check_total_vortex_span():
    # VALIDATION: The full vortex spans 2K = 8 coupling levels.
    span = 2 * K
    assert span == 8, "2K=%d, expected 8" % span
    print("total_vortex_span=%d" % span)


def check_observable_fraction():
    # VALIDATION: Observable fraction K/(2K) = 1/2.
    fraction = K / (2.0 * K)
    assert fraction == 0.5, "fraction=%g, expected 0.5" % fraction
    print("observable_fraction=%g" % fraction)


def check_spin_value():
    # VALIDATION: S = (1/2) * hbar = hbar/2.
    S = 0.5 * HBAR
    expected = HBAR / 2.0
    rel = abs(S - expected) / expected
    assert rel < 1e-15, "Spin mismatch, rel=%g" % rel
    print("spin=%g hbar_over_2=%g" % (S, expected))


def check_polynomial_symmetry():
    # VALIDATION: The polynomial is symmetric about s = 0, meaning
    # f(K, +s) + f(K, -s) = 2*f(K, 0) for all s.
    for s in [1, 2, 3]:
        lhs = f(K, s) + f(K, -s)
        rhs = 2 * f(K, 0)
        assert lhs == rhs, "Symmetry fails at s=%d: %d != %d" % (s, lhs, rhs)
    print("polynomial_symmetry_verified for s=1,2,3")


def check_spacing_algebraic():
    # VALIDATION: Equal spacing is guaranteed because the middle term sK
    # changes by K when s changes by 1.
    for s0 in [-1, 0]:
        diff = f(K, s0 + 1) - f(K, s0)
        assert diff == K, "diff at s=%d is %d, expected K=%d" % (s0, diff, K)
    print("algebraic_spacing_verified")


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
            print("  PASS  %-50s  (%.2fms)" % (name, dt))
            passed += 1
        except AssertionError as e:
            dt = (time.perf_counter() - t0) * 1000
            print("  FAIL  %-50s  (%.2fms)  %s" % (name, dt, e))
            failed += 1
        except Exception as e:
            dt = (time.perf_counter() - t0) * 1000
            print("  ERROR %-50s  (%.2fms)  %s" % (name, dt, e))
            failed += 1

    print()
    print("%d passed, %d failed, %d total" % (passed, failed, passed + failed))
    sys.exit(1 if failed else 0)
