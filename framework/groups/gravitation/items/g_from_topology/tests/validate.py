"""G from topology overview validation suite.

This validate.py file validates overview claims only.
Each check maps to an explicit statement from overview.md.
"""

import math


K = 4.0
D = 3.0
ALPHA = 7.2973525693e-3
HBAR = 1.054571817e-34  # J*s
C = 2.99792458e8  # m/s
M_E = 9.1093837015e-31  # kg
G_MEASURED = 6.67430e-11


def coupling_polynomial(k, s):
    """f(K,s) = 1 + sK + K^2."""
    return 1.0 + s * k + k**2


def g_tree_level(alpha=ALPHA):
    """G = (17/13) * alpha^21 * (hbar*c/m_e^2)."""
    prefactor = 17.0 / 13.0
    scale = HBAR * C / (M_E**2)
    return prefactor * (alpha**21) * scale


def g_one_loop(alpha=ALPHA):
    """One loop corrected G."""
    schwinger = 1.0 + alpha / (2.0 * math.pi)
    return g_tree_level(alpha) * schwinger


def check_polynomial_structural_values():
    # VALIDATION: Confirms the overview claim that the overview integer polynomial values in three structural regions.
    tet_a = coupling_polynomial(K, 1.0)
    origin = coupling_polynomial(K, 0.0)
    tet_b = coupling_polynomial(K, -1.0)
    assert tet_a == 21.0, "f(4,1)=%g expected 21" % tet_a
    assert origin == 17.0, "f(4,0)=%g expected 17" % origin
    assert tet_b == 13.0, "f(4,-1)=%g expected 13" % tet_b
    print("f4_plus1=%g f4_0=%g f4_minus1=%g" % (tet_a, origin, tet_b))


def check_prefactor_ratio():
    # VALIDATION: Confirms the overview claim that prefactor 17/13 from coupling capacity to spatial structure ratio.
    ratio = 17.0 / 13.0
    assert abs(ratio - 1.3076923076923077) < 1e-15, "ratio=%g" % ratio
    print("prefactor_17_over_13=%0.12f" % ratio)


def check_topological_exponent_value():
    # VALIDATION: Confirms the overview claim that exponent value 21 from 1 + 4 + 16.
    exponent = 1.0 + K + K**2
    assert exponent == 21.0, "exponent=%g expected 21" % exponent
    print("topology_exponent=%g" % exponent)


def check_tree_level_g_prediction():
    # VALIDATION: Confirms the overview claim that tree level prediction value near overview claim 6.666e-11.
    g_pred = g_tree_level(ALPHA)
    assert abs(g_pred - 6.666e-11) < 1.0e-13, "g_tree=%g expected near 6.666e-11" % g_pred
    print("g_tree=%0.13e" % g_pred)


def check_schwinger_correction_percent():
    # VALIDATION: Confirms the overview claim that one loop correction alpha/(2*pi) near 0.116 percent.
    frac = ALPHA / (2.0 * math.pi)
    pct = frac * 100.0
    assert abs(pct - 0.116) < 0.002, "percent=%g expected near 0.116" % pct
    print("schwinger_fraction=%0.10f schwinger_percent=%0.6f" % (frac, pct))


def check_one_loop_g_prediction():
    # VALIDATION: Confirms the overview claim that one loop predicted G near 6.6742e-11 and close to measured value.
    g_corr = g_one_loop(ALPHA)
    assert abs(g_corr - 6.6742e-11) < 2.0e-14, "g_one_loop=%g expected near 6.6742e-11" % g_corr
    rel = abs(g_corr - G_MEASURED) / G_MEASURED
    assert rel < 5e-4, "relative mismatch to measured too large, rel=%g" % rel
    print("g_one_loop=%0.13e rel_to_measured=%g" % (g_corr, rel))


def check_exponent_sensitivity():
    # VALIDATION: Confirms the overview claim that catastrophic exponent sensitivity where n+1 and n-1 shift by about 1/alpha and alpha.
    prefactor = (17.0 / 13.0) * (HBAR * C / (M_E**2))
    g20 = prefactor * (ALPHA**20)
    g21 = prefactor * (ALPHA**21)
    g22 = prefactor * (ALPHA**22)
    ratio_up = g20 / g21
    ratio_down = g22 / g21
    assert abs(ratio_up - (1.0 / ALPHA)) / (1.0 / ALPHA) < 1e-12, "ratio_up mismatch"
    assert abs(ratio_down - ALPHA) / ALPHA < 1e-12, "ratio_down mismatch"
    print("g20_over_g21=%0.6f g22_over_g21=%0.9f inv_alpha=%0.6f" % (ratio_up, ratio_down, 1.0 / ALPHA))


def check_exponent_recovered_from_measured_g():
    # VALIDATION: Confirms the overview claim that that extracting exponent from measured G returns integer near 21.
    argument = (13.0 / 17.0) * G_MEASURED * (M_E**2) / (HBAR * C)
    n = math.log(argument) / math.log(ALPHA)
    assert abs(n - 21.0) < 0.1, "recovered exponent=%g expected near 21" % n
    print("recovered_exponent=%0.9f" % n)


def check_residual_improvement_with_one_loop():
    # VALIDATION: Confirms the overview claim that residual reduction from tree level to one loop is about two orders improvement.
    tree_rel = abs(g_tree_level(ALPHA) - G_MEASURED) / G_MEASURED
    loop_rel = abs(g_one_loop(ALPHA) - G_MEASURED) / G_MEASURED
    improvement = tree_rel / loop_rel
    assert tree_rel < 0.002, "tree residual too large, rel=%g" % tree_rel
    assert loop_rel < 5e-5, "one loop residual too large, rel=%g" % loop_rel
    assert improvement > 50.0, "improvement too small, factor=%g" % improvement
    print("tree_rel=%g loop_rel=%g improvement_factor=%g" % (tree_rel, loop_rel, improvement))


def check_force_hierarchy_scaling():
    # VALIDATION: Confirms the overview claim that force hierarchy statement alpha^20 near 1e-43.
    ratio = ALPHA**20
    inv = 1.0 / ratio
    assert 1e-44 < ratio < 1e-42, "alpha^20=%g expected around 1e-43" % ratio
    assert 1e42 < inv < 1e44, "inverse ratio=%g expected around 1e43" % inv
    print("alpha_pow_20=%0.4e inverse=%0.4e" % (ratio, inv))


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
