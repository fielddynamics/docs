"""Fine structure constant overview validation suite.

This validate.py file validates overview claims only.
Each check maps to an explicit statement from overview.md.
"""

import math


K = 4
D = 3
INV_ALPHA_MEASURED = 137.035999177


def coupling_polynomial(k, s):
    """f(K,s) = 1 + K*s + K^2."""
    return 1 + k * s + k**2


def inverse_alpha_predicted():
    """Overview prediction 1/alpha = 137 + 1/28."""
    return 137 + 1.0 / 28.0


def check_measured_inverse_alpha_reference():
    # VALIDATION: Confirms the overview claim that 1/alpha = 137.035999177(12).
    assert 137.03 < INV_ALPHA_MEASURED < 137.04, "Inverse alpha reference out of range"
    print("measured_inverse_alpha=%0.9f" % INV_ALPHA_MEASURED)


def check_simplex_theorem():
    # VALIDATION: Confirms the overview claim that K = D + 1 = 4.
    assert K == D + 1, "K=%g, D+1=%g, expected equal" % (K, D + 1)
    assert K == 4, "K=%g, expected 4" % K
    print("K=%g D=%g D_plus_1=%g" % (K, D, D + 1))


def check_uniqueness_equation():
    # VALIDATION: Confirms the overview claim that 2(D+1) = 2^D has exactly
    # one positive integer solution D=3, where both sides equal 8.
    lhs = 2 * (D + 1)
    rhs = 2 ** D
    assert lhs == rhs == 8, "2(D+1)=%g, 2^D=%g, expected 8" % (lhs, rhs)
    solutions = [d for d in range(1, 30) if 2 * (d + 1) == 2 ** d]
    assert solutions == [3], "uniqueness solutions=%s, expected [3]" % solutions
    print("uniqueness_lhs=%g rhs=%g solutions=%s" % (lhs, rhs, solutions))


def check_polynomial_at_s0_and_s1():
    # VALIDATION: Confirms the overview claims that f(K,0) = 17 (coupling
    # depth at Field Origin) and f(K,1) = 21 (full coupling depth).
    f_origin = coupling_polynomial(K, 0)
    f_active = coupling_polynomial(K, 1)
    assert f_origin == 17, "f(4,0)=%g, expected 17" % f_origin
    assert f_active == 21, "f(4,1)=%g, expected 21" % f_active
    print("f_at_origin=%g f_at_active=%g" % (f_origin, f_active))


def check_evaluation_sites():
    # VALIDATION: Confirms the overview claim that 2K = 8 evaluation sites.
    sites = 2 * K
    assert sites == 8, "evaluation sites=%g, expected 8" % sites
    print("evaluation_sites_2K=%g" % sites)


def check_balance_point_composition():
    # VALIDATION: Confirms the overview claim that f(K,0) = 1 + K^2 = 17.
    origin = coupling_polynomial(K, 0)
    composition = 1 + K ** 2
    assert origin == composition == 17, (
        "origin=%g, 1+K^2=%g, expected 17" % (origin, composition)
    )
    print("f_at_balance=%g composition_1_plus_k2=%g" % (origin, composition))


def check_frame_transition_components():
    # VALIDATION: Confirms the overview claim that K^2 = 16 frame-transition
    # components.
    components = K ** 2
    assert components == 16, "K^2=%g, expected 16" % components
    print("frame_transition_components=%g" % components)


def check_k_squared_equals_two_to_k():
    # VALIDATION: Confirms the overview claim that 2^K = K^2 at K = 4.
    assert K ** 2 == 2 ** K == 16, (
        "K^2=%g, 2^K=%g, expected 16" % (K ** 2, 2 ** K)
    )
    print("K_squared=%g two_to_K=%g" % (K ** 2, 2 ** K))


def check_multiplicative_counting():
    # VALIDATION: Confirms the overview claim that 8 * 17 = 136 and
    # 1 + 136 = 137.
    product = 8 * 17
    assert product == 136, "8*17=%g, expected 136" % product
    total = 1 + product
    assert total == 137, "1+136=%g, expected 137" % total
    print("vertices_times_levels=%g plus_global_vertex=%g" % (product, total))


def check_integer_formula():
    # VALIDATION: Confirms the overview claim that 1 + 2K(K^2+1) = 137.
    value = 1 + 2 * K * (K ** 2 + 1)
    assert value == 137, "integer part=%g, expected 137" % value
    print("inverse_alpha_integer=%g" % value)


def check_integer_equivalence():
    # VALIDATION: Confirms that 1+8*17 and 1+2K(K^2+1) both give 137.
    lhs = 1 + 8 * 17
    rhs = 1 + 2 * K * (K ** 2 + 1)
    assert lhs == rhs == 137, "lhs=%g rhs=%g expected 137" % (lhs, rhs)
    print("integer_equivalence_lhs=%g rhs=%g" % (lhs, rhs))


def check_geometric_element_count():
    # VALIDATION: Confirms the overview claim that 8+12+8 = K(K+D) = 28.
    elements = 8 + 12 + 8
    formula = K * (K + D)
    product = 4 * 7
    assert elements == 28, "element count=%g, expected 28" % elements
    assert formula == 28, "K*(K+D)=%g, expected 28" % formula
    assert product == 28, "4*7=%g, expected 28" % product
    print("geometric_elements=%g formula=%g product=%g" % (elements, formula, product))


def check_f_vector_components():
    # VALIDATION: Confirms the overview claim that f0+f1+f2 = 8+12+8 = 28.
    f0, f1, f2 = 8, 12, 8
    total = f0 + f1 + f2
    assert total == 28, "f-vector sum=%g, expected 28" % total
    print("f0=%g f1=%g f2=%g sum=%g" % (f0, f1, f2, total))


def check_dynamical_counting():
    # VALIDATION: Confirms the overview claim that 7 DOF * 4 faces = 28
    # (2 massless + 5 massive graviton DOF, each through K = 4 faces).
    massless = 2
    massive = 5
    dof = massless + massive
    assert dof == 7, "DOF=%g, expected 7" % dof
    mode_face = dof * K
    assert mode_face == 28, "7*K=%g, expected 28" % mode_face
    print("dof=%g faces=%g mode_face_couplings=%g" % (dof, K, mode_face))


def check_fractional_correction():
    # VALIDATION: Confirms the overview claim that 1/alpha = 137 + 1/28.
    predicted = inverse_alpha_predicted()
    expected = 137 + 1.0 / 28.0
    assert abs(predicted - expected) < 1e-15, "prediction mismatch"
    assert abs(predicted - 137.0357) < 0.0001, (
        "predicted=%g, expected near 137.0357" % predicted
    )
    print("predicted_inverse_alpha=%0.12f" % predicted)


def check_predicted_digits():
    # VALIDATION: Confirms the overview claim that the predicted value is
    # 137.035,714,2... (the repeating decimal of 137 + 1/28).
    predicted = inverse_alpha_predicted()
    assert abs(predicted - 137.0357142) < 1e-7, (
        "predicted=%0.10f, expected 137.0357142..." % predicted
    )
    print("predicted_digits=%0.10f" % predicted)


def check_prediction_vs_measurement():
    # VALIDATION: Confirms the overview claim of agreement to two parts
    # per million.
    predicted = inverse_alpha_predicted()
    ppm = abs(predicted - INV_ALPHA_MEASURED) / INV_ALPHA_MEASURED * 1e6
    assert ppm < 3.0, "ppm error=%g, expected below 3" % ppm
    assert ppm > 1.0, "ppm error=%g, expected above 1" % ppm
    print("prediction_ppm=%0.4f" % ppm)


def check_residual():
    # VALIDATION: Confirms the overview claim that the residual is
    # 2.8 * 10^-4.
    predicted = inverse_alpha_predicted()
    residual = abs(predicted - INV_ALPHA_MEASURED)
    assert abs(residual - 2.8e-4) < 0.5e-4, (
        "residual=%g, expected near 2.8e-4" % residual
    )
    print("residual=%0.6f" % residual)


def check_cubic_solution():
    # VALIDATION: Confirms the overview claim that K^3 + K = 68 has exactly
    # one positive integer solution K = 4.
    assert K ** 3 + K == 68, "K^3+K=%g, expected 68" % (K ** 3 + K)
    solutions = [k for k in range(1, 20) if k ** 3 + k == 68]
    assert solutions == [4], "solutions=%s, expected [4]" % solutions
    print("cubic_solutions=%s K_cubed_plus_K=%g" % (solutions, K ** 3 + K))


def check_recover_d_from_k():
    # VALIDATION: Confirms the overview claim that from K = 4 and K = D + 1
    # you recover D = 3.
    recovered_d = K - 1
    assert recovered_d == D == 3, "recovered D=%g, expected 3" % recovered_d
    print("recovered_D=%g" % recovered_d)


def check_depth_and_breadth():
    # VALIDATION: Confirms the overview claim that depth = f(K,+1) = 21
    # (giving G through alpha^21) and breadth = 1 + 8*17 = 137.
    depth = coupling_polynomial(K, 1)
    breadth = 1 + 2 * K * (K ** 2 + 1)
    assert depth == 21, "depth=%g, expected 21" % depth
    assert breadth == 137, "breadth=%g, expected 137" % breadth
    print("depth=%g breadth=%g" % (depth, breadth))


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
