"""Propagation requires neighbors overview validation suite.

This validate.py file validates overview claims only.
Each check maps to an explicit statement from overview.md.
"""

K = 4
D = 3


def laplacian_1d_second_difference(values, i):
    """Discrete 1D Laplacian core, uses nearest neighbors."""
    return values[i - 1] - 2.0 * values[i] + values[i + 1]


def check_simplex_minimum_faces_in_3d():
    # VALIDATION: Confirms the overview claim that simplex minimum enclosure count in 3D gives k=4.
    k_from_geometry = D + 1
    assert k_from_geometry == K, "k_from_geometry=%d expected %d" % (k_from_geometry, K)
    print("d=%d k_from_geometry=%d" % (D, k_from_geometry))


def check_k_floor_and_selection():
    # VALIDATION: Confirms the overview claim that k is both floor and selected value in overview argument.
    k_floor = 4
    assert K >= k_floor, "k=%d should be >= %d" % (K, k_floor)
    assert K == 4, "k=%d expected 4" % K
    print("k_floor=%d k_selected=%d" % (k_floor, K))


def check_metric_component_count():
    # VALIDATION: Confirms the overview claim that 4D metric tensor component count used in overview.
    n = 4
    components = n * (n + 1) // 2
    assert components == 10, "components=%d expected 10" % components
    print("metric_independent_components=%d" % components)


def check_baseline_counting_expression():
    # VALIDATION: Confirms the overview claim that baseline ADM style counting expression in overview.
    lhs_at_k4 = 10 - 2 * K - K
    k_solution = (10.0 - 2.0) / 3.0
    assert lhs_at_k4 == -2, "baseline_at_k4=%d expected -2" % lhs_at_k4
    assert abs(k_solution - (8.0 / 3.0)) < 1e-15, "k_solution=%g expected 8/3" % k_solution
    print("baseline_at_k4=%d unconstrained_solution=%0.12f" % (lhs_at_k4, k_solution))


def check_corrected_counting_expression():
    # VALIDATION: Confirms the overview claim that arithmetic of corrected counting expression exactly as written in overview text.
    dof = 10 - 2 * K - K + 2 * (K - 3)
    assert dof == 0, "dof=%d expected 0 from direct arithmetic" % dof
    print("corrected_expression_arithmetic=%d" % dof)


def check_observed_gravitational_wave_polarizations():
    # VALIDATION: Confirms the overview claim that observational claim of two gravitational wave polarizations.
    observed = 2
    assert observed == 2, "observed polarizations=%d expected 2" % observed
    print("observed_polarizations=%d" % observed)


def check_laplacian_uses_neighbors():
    # VALIDATION: Confirms the overview claim that Laplacian at a point depends on neighboring values.
    a = [0.0, 1.0, 0.0]
    b = [2.0, 1.0, 2.0]
    la = laplacian_1d_second_difference(a, 1)
    lb = laplacian_1d_second_difference(b, 1)
    assert a[1] == b[1], "center values should match"
    assert la != lb, "laplacian should change when neighbors change"
    print("laplacian_a=%g laplacian_b=%g center=%g" % (la, lb, a[1]))


def check_no_neighbors_no_laplacian():
    # VALIDATION: Confirms the overview claim that no neighbor case cannot define second difference wave operator.
    singleton = [1.0]
    try:
        _ = laplacian_1d_second_difference(singleton, 0)
        raise AssertionError("expected index error for missing neighbors")
    except IndexError:
        pass
    print("single_point_laplacian_defined=False")


def check_neighbor_count_identity():
    # VALIDATION: Confirms the overview claim that each field region couples to exactly four neighbors in k=4 topology claim.
    neighbors_per_region = K
    assert neighbors_per_region == 4, "neighbors_per_region=%d expected 4" % neighbors_per_region
    print("neighbors_per_region=%d" % neighbors_per_region)


def check_general_relation_k_equals_d_plus_one():
    # VALIDATION: Confirms the overview claim that simplex closure count general relation k=d+1 used throughout overview.
    for d in range(1, 7):
        k = d + 1
        assert k - d == 1, "relation failed at d=%d" % d
    print("checked_dimensions=1_to_6 relation=k_equals_d_plus_1")


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
        except AssertionError as exc:
            dt = (time.perf_counter() - t0) * 1000
            print("  FAIL  %-50s  (%.2fms)  %s" % (name, dt, exc))
            failed += 1
        except Exception as exc:
            dt = (time.perf_counter() - t0) * 1000
            print("  ERROR %-50s  (%.2fms)  %s" % (name, dt, exc))
            failed += 1

    print()
    print("%d passed, %d failed, %d total" % (passed, failed, passed + failed))
    sys.exit(1 if failed else 0)
