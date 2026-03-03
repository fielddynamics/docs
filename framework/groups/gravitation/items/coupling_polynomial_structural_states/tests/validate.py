"""Coupling polynomial overview validation suite.

This validate.py file validates overview claims only.
Each check maps to an explicit statement from overview.md.
"""

import math


K = 4.0
D = 3.0


def coupling_polynomial(k, s):
    """f(K,s) = 1 + sK + K^2."""
    return 1.0 + s * k + k**2


def simplex_boundary_sum(k, d):
    """(K^D - 1)/(K - 1)."""
    return (k**d - 1.0) / (k - 1.0)


def check_full_coupling_depth_value():
    # VALIDATION: Confirms the overview claim that full coupling depth from geometric series at K=4.
    value = 1.0 + K + K**2
    assert value == 21.0, "full depth=%g expected 21" % value
    print("full_coupling_depth=%g" % value)


def check_geometric_series_identity():
    # VALIDATION: Confirms the overview claim that geometric series identity used for coupling depth.
    lhs = 1.0 + K + K**2
    rhs = (K**3 - 1.0) / (K - 1.0)
    assert abs(lhs - rhs) < 1e-15, "identity mismatch, lhs=%g rhs=%g" % (lhs, rhs)
    print("geometric_series_lhs=%g rhs=%g" % (lhs, rhs))


def check_simplex_boundary_sum_form():
    # VALIDATION: Confirms the overview claim that simplex boundary sum form with D=3.
    value = simplex_boundary_sum(K, D)
    assert abs(value - 21.0) < 1e-15, "simplex sum=%g expected 21" % value
    print("simplex_boundary_sum=%g" % value)


def check_structural_state_values():
    # VALIDATION: Confirms the overview claim that structural state polynomial values 21, 17, and 13.
    tet_a = coupling_polynomial(K, 1.0)
    origin = coupling_polynomial(K, 0.0)
    tet_b = coupling_polynomial(K, -1.0)
    assert tet_a == 21.0, "tet_a=%g expected 21" % tet_a
    assert origin == 17.0, "origin=%g expected 17" % origin
    assert tet_b == 13.0, "tet_b=%g expected 13" % tet_b
    print("tet_a=%g origin=%g tet_b=%g" % (tet_a, origin, tet_b))


def check_structural_equal_spacing():
    # VALIDATION: Confirms the overview claim that equal spacing lock with step K between structural values.
    tet_a = coupling_polynomial(K, 1.0)
    origin = coupling_polynomial(K, 0.0)
    tet_b = coupling_polynomial(K, -1.0)
    d1 = tet_a - origin
    d2 = origin - tet_b
    assert d1 == K, "tet_a - origin=%g expected %g" % (d1, K)
    assert d2 == K, "origin - tet_b=%g expected %g" % (d2, K)
    print("spacing_1=%g spacing_2=%g k=%g" % (d1, d2, K))


def check_arithmetic_mean_lock():
    # VALIDATION: Confirms the overview claim that arithmetic mean identity where field origin value is midpoint.
    tet_a = coupling_polynomial(K, 1.0)
    origin = coupling_polynomial(K, 0.0)
    tet_b = coupling_polynomial(K, -1.0)
    mean = 0.5 * (tet_a + tet_b)
    assert mean == origin, "mean=%g origin=%g expected equal" % (mean, origin)
    print("arithmetic_mean=%g origin=%g" % (mean, origin))


def check_integer_lock_rigidity():
    # VALIDATION: Confirms the overview claim that one unit perturbation breaks arithmetic lock, showing rigidity.
    tet_a = coupling_polynomial(K, 1.0)
    origin = coupling_polynomial(K, 0.0)
    tet_b = coupling_polynomial(K, -1.0)
    perturbed_tet_a = tet_a + 1.0
    perturbed_mean = 0.5 * (perturbed_tet_a + tet_b)
    assert perturbed_mean != origin, "perturbation should break midpoint lock"
    print("origin=%g perturbed_mean=%g delta=%g" % (origin, perturbed_mean, perturbed_mean - origin))


def check_capacity_and_structure_decomposition():
    # VALIDATION: Confirms the overview claim that 17 as 16 plus 1 and 13 as 12 plus 1 from K and D structure.
    capacity = K**2 + 1.0
    structure = K * D + 1.0
    assert capacity == 17.0, "capacity=%g expected 17" % capacity
    assert structure == 13.0, "structure=%g expected 13" % structure
    print("capacity_k2_plus_1=%g structure_kd_plus_1=%g" % (capacity, structure))


def check_structural_ratio_value():
    # VALIDATION: Confirms the overview claim that ratio 17/13 from structural values used in subsequent gravitation equations.
    origin = coupling_polynomial(K, 0.0)
    tet_b = coupling_polynomial(K, -1.0)
    ratio = origin / tet_b
    expected = 17.0 / 13.0
    rel = abs(ratio - expected) / expected
    assert rel < 1e-15, "ratio mismatch, rel=%g" % rel
    print("structural_ratio=%0.12f expected=%0.12f" % (ratio, expected))


def check_alpha_depth_gap_scale():
    # VALIDATION: Confirms the overview claim that force hierarchy depth scaling claim alpha^20 near 1e-43.
    alpha = 7.2973525693e-3
    gap = alpha**20
    assert 1e-44 < gap < 1e-42, "alpha^20=%g expected around 1e-43" % gap
    print("alpha_depth_gap=%0.4e" % gap)


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
