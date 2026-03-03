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
A0 = 1.2e-10  # m/s^2
K = 4.0
M_E = 9.1093837015e-31  # kg
M_MU = 1.883531627e-28  # kg
M_P = 1.67262192369e-27  # kg
E_CHARGE = 1.602176634e-19  # C
EPS0 = 8.8541878128e-12  # F/m
MPC_M = 3.085677581491367e22  # m


def route1_radius_from_em(mass):
    """Classical EM stability radius."""
    return (E_CHARGE**2) / (4.0 * math.pi * EPS0 * mass * C**2)


def route1_radius_from_alpha(mass):
    """Equivalent form using alpha and hbar."""
    return ALPHA * HBAR / (mass * C)


def route2_radius_from_gravity(mass):
    """Topology plus gravity route with fixed a0 and K."""
    return K * math.sqrt(G * mass / A0)


def route3_a0_from_hubble(H):
    """Hubble relation used in the closure topology route."""
    return (C * H / (2.0 * math.pi)) * math.sqrt(K / math.pi)


def route3_radius_from_constants(H):
    """Solve r from route 3 without electron mass input."""
    a0_from_H = route3_a0_from_hubble(H)
    return ((K**2) * G * ALPHA * HBAR / (C * a0_from_H)) ** (1.0 / 3.0)


def route3_mass_from_radius(radius):
    """Mass closure identity m = alpha*hbar/(r*c)."""
    return ALPHA * HBAR / (radius * C)


def check_reference_electron_mass_value():
    # VALIDATION: Confirms the overview claim that the overview reference value for electron mass and keeps constants anchored.
    assert 9.0e-31 < M_E < 9.2e-31, "Electron mass constant out of expected range"
    print("electron_mass_kg=%g" % M_E)


def check_route1_formula_equivalence():
    # VALIDATION: Confirms the overview claim that route 1 electromagnetic self energy formula equals the alpha hbar form.
    r_em = route1_radius_from_em(M_E)
    r_alpha = route1_radius_from_alpha(M_E)
    rel = abs(r_em - r_alpha) / r_alpha
    assert rel < 1e-8, "Route 1 formulas disagree, rel=%g" % rel
    print("route1_formula_relative_error=%g" % rel)


def check_route1_radius_value():
    # VALIDATION: Confirms the overview claim that checks route 1 returns the classical electron radius scale shown in the overview.
    r1 = route1_radius_from_em(M_E)
    r1_fm = r1 * 1e15
    assert abs(r1_fm - 2.818) < 0.01, "Route 1 radius=%g fm, expected near 2.818 fm" % r1_fm
    print("route1_radius_fm=%g" % r1_fm)


def check_route2_radius_value():
    # VALIDATION: Confirms the overview claim that checks route 2 gravitational topology radius for electron scale in the overview.
    r2 = route2_radius_from_gravity(M_E)
    r2_fm = r2 * 1e15
    assert abs(r2_fm - 2.82) < 0.08, "Route 2 radius=%g fm, expected near 2.82 fm" % r2_fm
    print("route2_radius_fm=%g" % r2_fm)


def check_route1_route2_convergence():
    # VALIDATION: Confirms the overview claim that overview statement that routes 1 and 2 converge for the electron.
    r1 = route1_radius_from_em(M_E)
    r2 = route2_radius_from_gravity(M_E)
    percent = abs(r1 - r2) / r1 * 100.0
    assert percent < 1.5, "Route 1 and 2 mismatch too large, percent=%g" % percent
    print("route1_route2_percent_difference=%g" % percent)


def check_route3_hubble_to_a0_link():
    # VALIDATION: Confirms the overview claim that route 3 Hubble relation produces the acceleration scale used in the overview.
    H0 = 70.0 * 1000.0 / MPC_M  # 70 km/s/Mpc in SI
    a0_h = route3_a0_from_hubble(H0)
    rel = abs(a0_h - A0) / A0
    assert rel < 0.1, "a0 from H mismatch too large, rel=%g" % rel
    print("route3_a0_from_H=%g route3_a0_relative_error=%g" % (a0_h, rel))


def check_route3_radius_and_mass_solution():
    # VALIDATION: Confirms the overview claim that route 3 solves radius and mass from constants without using electron mass as input.
    H0 = 70.0 * 1000.0 / MPC_M
    r3 = route3_radius_from_constants(H0)
    m3 = route3_mass_from_radius(r3)
    r3_fm = r3 * 1e15
    rel_mass = abs(m3 - M_E) / M_E
    assert abs(r3_fm - 2.82) < 0.08, "Route 3 radius=%g fm, expected near 2.82 fm" % r3_fm
    assert rel_mass < 0.02, "Route 3 mass relative error too large, rel=%g" % rel_mass
    print("route3_radius_fm=%g route3_mass_kg=%g route3_mass_relative_error=%g" % (r3_fm, m3, rel_mass))


def check_non_electron_mismatch_large():
    # VALIDATION: Confirms the overview claim that overview uniqueness claim, non electron masses do not show route 1 and 2 convergence.
    r1_mu = route1_radius_from_em(M_MU)
    r2_mu = route2_radius_from_gravity(M_MU)
    ratio_mu = max(r1_mu, r2_mu) / min(r1_mu, r2_mu)

    r1_p = route1_radius_from_em(M_P)
    r2_p = route2_radius_from_gravity(M_P)
    ratio_p = max(r1_p, r2_p) / min(r1_p, r2_p)

    assert ratio_mu > 1e3, "Muon mismatch ratio too small, ratio=%g" % ratio_mu
    assert ratio_p > 1e4, "Proton mismatch ratio too small, ratio=%g" % ratio_p
    print("muon_route_mismatch_ratio=%g proton_route_mismatch_ratio=%g" % (ratio_mu, ratio_p))


def check_mass_closure_identity_at_route1_radius():
    # VALIDATION: Confirms the overview claim that overview closure claim, m = alpha*hbar/(r*c) returns electron mass at route 1 radius.
    r1 = route1_radius_from_em(M_E)
    m_from_r1 = route3_mass_from_radius(r1)
    rel = abs(m_from_r1 - M_E) / M_E
    assert rel < 1e-8, "Mass closure identity mismatch at route 1 radius, rel=%g" % rel
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
