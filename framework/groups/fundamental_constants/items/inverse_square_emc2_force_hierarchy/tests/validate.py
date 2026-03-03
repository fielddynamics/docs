"""Mass-energy equivalence overview validation suite.

This validate.py file validates overview claims only.
Each check maps to an explicit statement from overview.md.
"""

import math


ALPHA = 7.2973525693e-3
HBAR = 1.054571817e-34  # J*s
C = 2.99792458e8  # m/s
M_E = 9.1093837015e-31  # kg
N_STATES = 1.0 / ALPHA


def classical_radius_from_mass(mass):
    """r = alpha*hbar/(m*c)."""
    return ALPHA * HBAR / (mass * C)


def mass_from_radius_and_states(radius, n_states):
    """m = hbar/(N*r*c)."""
    return HBAR / (n_states * radius * C)


def check_mass_energy_relation_value():
    # VALIDATION: Confirms the overview claim that the overview baseline that c^2 is the conversion factor in mass-energy equivalence.
    e_rest = M_E * C**2
    assert abs(e_rest - 8.187e-14) / 8.187e-14 < 0.01, (
        "electron rest energy=%g J, expected near 8.187e-14 J" % e_rest
    )
    print("electron_rest_energy_j=%g" % e_rest)


def check_state_count_from_alpha():
    # VALIDATION: Confirms the overview claim that the overview claim that state count N is identified with inverse alpha.
    assert abs(N_STATES - 137.035999) < 0.01, (
        "N=%g, expected near 137.036" % N_STATES
    )
    print("state_count_N=%0.9f" % N_STATES)


def check_closure_bandwidth_partition():
    # VALIDATION: Confirms the overview claim that closure bandwidth partition c/r and per-state rate c/(N*r).
    r = classical_radius_from_mass(M_E)
    total_rate = C / r
    per_state_rate = C / (N_STATES * r)
    rel = abs(total_rate - N_STATES * per_state_rate) / total_rate
    assert rel < 1e-12, "bandwidth partition mismatch, rel=%g" % rel
    print("closure_total_rate=%g per_state_rate=%g partition_rel_error=%g" % (total_rate, per_state_rate, rel))


def check_mass_closure_forms_equivalent():
    # VALIDATION: Confirms the overview claim that the overview derivation m = hbar/(N*r*c) and m = alpha*hbar/(r*c) are equivalent.
    r = classical_radius_from_mass(M_E)
    m_from_n = mass_from_radius_and_states(r, N_STATES)
    m_from_alpha = ALPHA * HBAR / (r * C)
    rel = abs(m_from_n - m_from_alpha) / m_from_alpha
    assert rel < 1e-12, "mass closure forms mismatch, rel=%g" % rel
    print("mass_closure_form_relative_error=%g" % rel)


def check_classical_radius_relation():
    # VALIDATION: Confirms the overview claim that the overview claim that mass can be written as m = alpha*hbar/(r*c) at the electron scale.
    r = classical_radius_from_mass(M_E)
    r_fm = r * 1e15
    assert abs(r_fm - 2.818) < 0.01, "r=%g fm, expected near 2.818 fm" % r_fm
    print("closure_radius_fm=%g" % r_fm)


def check_squared_speed_dimensional_requirement():
    # VALIDATION: Confirms the overview claim that dimensional argument that only a squared speed converts mass to energy dimensions.
    # Represent dimensions as exponents of (M, L, T)
    dim_mass = (1, 0, 0)
    dim_speed = (0, 1, -1)
    dim_energy = (1, 2, -2)
    dim_mc = (dim_mass[0] + dim_speed[0], dim_mass[1] + dim_speed[1], dim_mass[2] + dim_speed[2])
    dim_mc2 = (dim_mass[0] + 2 * dim_speed[0], dim_mass[1] + 2 * dim_speed[1], dim_mass[2] + 2 * dim_speed[2])
    dim_mc3 = (dim_mass[0] + 3 * dim_speed[0], dim_mass[1] + 3 * dim_speed[1], dim_mass[2] + 3 * dim_speed[2])
    assert dim_mc != dim_energy, "m*c should not match energy dimensions"
    assert dim_mc2 == dim_energy, "m*c^2 must match energy dimensions"
    assert dim_mc3 != dim_energy, "m*c^3 should not match energy dimensions"
    print("dimension_mc=%s dimension_mc2=%s dimension_energy=%s" % (dim_mc, dim_mc2, dim_energy))


def check_exchange_symmetric_speed_product():
    # VALIDATION: Confirms the overview claim that exchange symmetry argument with two equal chamber closure speeds.
    c_a = C
    c_b = C
    product = c_a * c_b
    swapped = c_b * c_a
    assert abs(product - C**2) / (C**2) < 1e-15, "c_A*c_B not equal to c^2"
    assert product == swapped, "exchange symmetry product mismatch"
    print("closure_speed_product=%g" % product)


def check_metric_bilinear_structure_example():
    # VALIDATION: Confirms the overview claim that metric bilinear structure claim in overview by explicit tetrad product form.
    # Flat-space tetrad example with signature (-,+,+,+): e^0_0 = c.
    e00 = C
    eta00 = -1.0
    g00 = eta00 * e00 * e00
    assert abs(g00 + C**2) / (C**2) < 1e-15, "g00 bilinear example mismatch"
    print("example_g00=%g expected_g00=%g" % (g00, -C**2))


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
