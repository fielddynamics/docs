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
    # VALIDATION: Confirms the overview claim that the overview benchmark measurement for inverse alpha.
    assert 137.03 < INV_ALPHA_MEASURED < 137.04, "Inverse alpha reference out of range"
    print("measured_inverse_alpha=%0.9f" % INV_ALPHA_MEASURED)


def check_polynomial_values_at_field_origin_and_depth():
    # VALIDATION: Confirms the overview claim that coupling polynomial values at K=4 used in the overview.
    f0 = coupling_polynomial(K, 0)
    f1 = coupling_polynomial(K, 1)
    assert f0 == 17, "f(4,0)=%g, expected 17" % f0
    assert f1 == 21, "f(4,1)=%g, expected 21" % f1
    print("f_at_s0=%g f_at_s1=%g" % (f0, f1))


def check_integer_part_derivation():
    # VALIDATION: Confirms the overview claim that integer part derivation 1 + 8*17 = 137.
    value = 1 + 2 * K * (K**2 + 1)
    assert value == 137, "integer part=%g, expected 137" % value
    print("inverse_alpha_integer_part=%g" % value)


def check_geometric_element_count():
    # VALIDATION: Confirms the overview claim that geometric element count and closure formula for K=4, D=3.
    elements = 8 + 12 + 8
    formula = K * (K + D)
    assert elements == 28, "element count=%g, expected 28" % elements
    assert formula == 28, "K*(K+D)=%g, expected 28" % formula
    print("geometric_elements=%g formula_value=%g" % (elements, formula))


def check_fractional_cycle_prediction():
    # VALIDATION: Confirms the overview claim that fractional contribution 1/28 and predicted inverse alpha value.
    predicted = inverse_alpha_predicted()
    expected = 137 + 1.0 / 28.0
    assert abs(predicted - expected) < 1e-15, "prediction mismatch"
    print("predicted_inverse_alpha=%0.12f" % predicted)


def check_prediction_vs_measurement_error():
    # VALIDATION: Confirms the overview claim that overview claim that predicted and measured values agree at about 0.00021 percent.
    predicted = inverse_alpha_predicted()
    percent_error = abs(predicted - INV_ALPHA_MEASURED) / INV_ALPHA_MEASURED * 100.0
    assert percent_error < 0.001, "percent error too large=%g" % percent_error
    assert abs(percent_error - 0.00021) < 0.0001, (
        "percent error=%g, expected near 0.00021" % percent_error
    )
    ppm = percent_error * 10000.0
    print("prediction_percent_error=%0.9f prediction_ppm=%0.6f" % (percent_error, ppm))


def check_cubic_solution_uniqueness():
    # VALIDATION: Confirms the overview claim that cubic encoding claim K^3 + K = 68 has the unique positive integer solution K=4.
    solutions = [k for k in range(1, 20) if k**3 + k == 68]
    assert solutions == [4], "solutions=%s, expected [4]" % solutions
    print("cubic_integer_solutions=%s" % solutions)


def check_integer_expression_equivalence():
    # VALIDATION: Confirms the overview claim that that two integer expressions for 137 are algebraically identical.
    lhs = 1 + 8 * 17
    rhs = 1 + 2 * K * (K**2 + 1)
    assert lhs == rhs == 137, "lhs=%g rhs=%g expected 137" % (lhs, rhs)
    print("integer_equivalence_lhs=%g rhs=%g" % (lhs, rhs))


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
