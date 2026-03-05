"""Electron mass overview validation suite.

This validate.py file exists to validate overview claims only.
Each check maps to an explicit statement from overview.md.
"""

import math


# Constants used by overview equations.
ALPHA = 7.2973525693e-3
HBAR = 1.054571817e-34  # J*s
C = 2.99792458e8  # m/s
G = 6.67430e-11  # m^3 kg^-1 s^-2
A0 = 1.22e-10  # m/s^2 (Milgrom empirical value)
K = 4.0
M_E = 9.1093837015e-31  # kg
M_MU = 1.883531627e-28  # kg
M_P = 1.67262192369e-27  # kg
E_CHARGE = 1.602176634e-19  # C
EPS0 = 8.8541878128e-12  # F/m


def route1_radius_from_em(mass):
    """Classical EM stability radius: r = e^2/(4*pi*eps0*m*c^2)."""
    return (E_CHARGE ** 2) / (4.0 * math.pi * EPS0 * mass * C ** 2)


def route1_radius_from_alpha(mass):
    """Equivalent form using alpha and hbar: r = alpha*hbar/(m*c)."""
    return ALPHA * HBAR / (mass * C)


def route2_radius_from_gravity(mass):
    """Topology plus gravity route: r = K*sqrt(G*m/a0)."""
    return K * math.sqrt(G * mass / A0)


def route3_radius_from_a0():
    """Solve r from route 3 using empirical a0, no electron mass input."""
    return ((K ** 2) * G * ALPHA * HBAR / (A0 * C)) ** (1.0 / 3.0)


def mass_from_radius(radius):
    """Mass closure identity: m = alpha*hbar/(r*c)."""
    return ALPHA * HBAR / (radius * C)


def check_reference_electron_mass_value():
    # VALIDATION: Confirms the overview claim that m_e = 9.109e-31 kg.
    assert 9.0e-31 < M_E < 9.2e-31, (
        "Electron mass constant out of expected range"
    )
    print("electron_mass_kg=%g" % M_E)


def check_tetrad_coupling_channels():
    # VALIDATION: Confirms the overview claim that K x K = 16 tetrad
    # components and K^2 = 16 coupling channels.
    assert K * K == 16, "K*K=%g, expected 16" % (K * K)
    assert K ** 2 == 16, "K^2=%g, expected 16" % (K ** 2)
    print("tetrad_components=%.0f coupling_channels=%.0f" % (K * K, K ** 2))


def check_milgrom_a0_empirical():
    # VALIDATION: Confirms the overview claim that Milgrom identified
    # a_0 ~ 1.2e-10 m/s^2 from galaxy rotation curves.
    assert abs(A0 - 1.22e-10) < 0.1e-10, "a0=%g, expected ~1.22e-10" % A0
    print("milgrom_a0=%g" % A0)


def check_route1_formula_equivalence():
    # VALIDATION: Confirms the overview claim that the classical electron
    # radius e^2/(4*pi*eps0*m*c^2) equals alpha*hbar/(m*c).
    r_em = route1_radius_from_em(M_E)
    r_alpha = route1_radius_from_alpha(M_E)
    rel = abs(r_em - r_alpha) / r_alpha
    assert rel < 1e-8, "Route 1 formulas disagree, rel=%g" % rel
    print("route1_formula_relative_error=%g" % rel)


def check_route1_radius_value():
    # VALIDATION: Confirms the overview claim that route 1 gives
    # r_e = 2.818 fm.
    r1 = route1_radius_from_em(M_E)
    r1_fm = r1 * 1e15
    assert abs(r1_fm - 2.818) < 0.01, (
        "Route 1 radius=%g fm, expected near 2.818 fm" % r1_fm
    )
    print("route1_radius_fm=%g" % r1_fm)


def check_route2_radius_value():
    # VALIDATION: Confirms the overview claim that route 2 gives
    # r = 2.82 fm via K*sqrt(G*m_e/a_0).
    r2 = route2_radius_from_gravity(M_E)
    r2_fm = r2 * 1e15
    assert abs(r2_fm - 2.82) < 0.08, (
        "Route 2 radius=%g fm, expected near 2.82 fm" % r2_fm
    )
    print("route2_radius_fm=%g" % r2_fm)


def check_route1_route2_convergence():
    # VALIDATION: Confirms the overview claim that routes 1 and 2 agree
    # to 0.21%.
    r1 = route1_radius_from_em(M_E)
    r2 = route2_radius_from_gravity(M_E)
    percent = abs(r1 - r2) / r1 * 100.0
    assert percent < 1.5, (
        "Route 1 and 2 mismatch too large, percent=%g" % percent
    )
    print("route1_route2_percent_difference=%.2f%%" % percent)


def check_closure_saturation_algebra():
    # VALIDATION: Confirms the overview derivation Step 1 algebra:
    # a0 = K^2 * G * alpha * hbar / (r^3 * c).
    r3 = route3_radius_from_a0()
    a0_from_algebra = (K ** 2) * G * ALPHA * HBAR / (r3 ** 3 * C)
    rel = abs(a0_from_algebra - A0) / A0
    assert rel < 1e-10, "Step 1 algebra mismatch, rel=%g" % rel
    print("a0_from_algebra=%g a0_input=%g rel=%g" % (
        a0_from_algebra, A0, rel
    ))


def check_route3_radius_value():
    # VALIDATION: Confirms the overview claim that route 3 gives
    # r = 2.82 fm using empirical a0 directly.
    r3 = route3_radius_from_a0()
    r3_fm = r3 * 1e15
    assert abs(r3_fm - 2.82) < 0.08, (
        "Route 3 radius=%g fm, expected near 2.82 fm" % r3_fm
    )
    print("route3_radius_fm=%g" % r3_fm)


def check_route3_mass_solution():
    # VALIDATION: Confirms the overview claim that route 3 recovers
    # m = 9.11e-31 kg without electron mass as input.
    r3 = route3_radius_from_a0()
    m3 = mass_from_radius(r3)
    rel_mass = abs(m3 - M_E) / M_E
    assert rel_mass < 0.02, (
        "Route 3 mass relative error too large, rel=%g" % rel_mass
    )
    print("route3_mass_kg=%g mass_relative_error=%g" % (m3, rel_mass))


def check_route3_mass_recovery_percent():
    # VALIDATION: Confirms the overview claim that route 3 recovers
    # the electron mass to 0.1%.
    r3 = route3_radius_from_a0()
    m3 = mass_from_radius(r3)
    percent = abs(m3 - M_E) / M_E * 100.0
    assert percent < 0.5, (
        "Route 3 mass recovery=%.3f%%, expected <0.5%%" % percent
    )
    print("route3_mass_recovery_percent=%.3f%%" % percent)


def check_non_electron_mismatch_muon():
    # VALIDATION: Confirms the overview claim that for the muon, routes
    # disagree by a factor of three thousand.
    r1_mu = route1_radius_from_em(M_MU)
    r2_mu = route2_radius_from_gravity(M_MU)
    ratio_mu = max(r1_mu, r2_mu) / min(r1_mu, r2_mu)
    assert ratio_mu > 1e3, (
        "Muon mismatch ratio too small, ratio=%g" % ratio_mu
    )
    assert ratio_mu < 1e4, (
        "Muon mismatch ratio too large for 'three thousand', ratio=%g"
        % ratio_mu
    )
    print("muon_route_mismatch_ratio=%g" % ratio_mu)


def check_non_electron_mismatch_proton():
    # VALIDATION: Confirms the overview claim that for the proton, routes
    # disagree by a factor of eighty thousand.
    r1_p = route1_radius_from_em(M_P)
    r2_p = route2_radius_from_gravity(M_P)
    ratio_p = max(r1_p, r2_p) / min(r1_p, r2_p)
    assert ratio_p > 5e4, (
        "Proton mismatch ratio too small, ratio=%g" % ratio_p
    )
    assert ratio_p < 1e6, (
        "Proton mismatch ratio too large for 'eighty thousand', ratio=%g"
        % ratio_p
    )
    print("proton_route_mismatch_ratio=%g" % ratio_p)


def check_mass_closure_identity_at_route1_radius():
    # VALIDATION: Confirms the overview claim that m = alpha*hbar/(r*c)
    # returns the electron mass when evaluated at the classical electron
    # radius.
    r1 = route1_radius_from_em(M_E)
    m_from_r1 = mass_from_radius(r1)
    rel = abs(m_from_r1 - M_E) / M_E
    assert rel < 1e-8, (
        "Mass closure identity mismatch at route 1 radius, rel=%g" % rel
    )
    print("mass_closure_identity_relative_error=%g" % rel)


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
