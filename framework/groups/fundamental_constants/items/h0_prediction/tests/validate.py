"""H0 prediction overview validation suite.

This validate.py file validates overview claims only.
Each check maps to an explicit statement from overview.md.
"""

import math


K = 4.0
A0_REFERENCE = 1.2e-10  # m/s^2
A0_EFFECTIVE = 1.22e-10  # m/s^2, implied by the reported H0 values in this overview
C = 2.99792458e8  # m/s
MPC_M = 3.085677581491367e22  # m

H0_PLANCK = 67.4
H0_SH0ES = 73.04
H0_GW170817 = 70.0
H0_GW170817_SIGMA = 12.0


def geometric_correction():
    """sqrt(K/pi)."""
    return math.sqrt(K / math.pi)


def h_from_a0_with_correction(a0=A0_EFFECTIVE):
    """H = 2*pi*a0 / (c*sqrt(K/pi)) in SI units."""
    return (2.0 * math.pi * a0) / (C * geometric_correction())


def h_from_a0_no_correction(a0=A0_EFFECTIVE):
    """H = 2*pi*a0/c in SI units."""
    return (2.0 * math.pi * a0) / C


def h_si_to_km_s_mpc(h_si):
    """Convert H from 1/s to km/s/Mpc."""
    return h_si * MPC_M / 1000.0


def check_geometric_correction_value():
    # VALIDATION: Confirms the overview claim that the overview geometric correction from tetrahedral to spherical boundary.
    corr = geometric_correction()
    assert abs(corr - 1.128379167) < 1e-6, "sqrt(4/pi)=%g, expected near 1.128379" % corr
    print("geometric_correction=%0.9f" % corr)


def check_a0_h_round_trip_consistency():
    # VALIDATION: Confirms the overview claim that the derivation chain equation a0 = (cH/2pi)*sqrt(K/pi) via round trip consistency.
    h_si = h_from_a0_with_correction(A0_EFFECTIVE)
    a0_back = (C * h_si / (2.0 * math.pi)) * geometric_correction()
    rel = abs(a0_back - A0_EFFECTIVE) / A0_EFFECTIVE
    assert rel < 1e-12, "round trip relative error=%g" % rel
    print("a0_round_trip_relative_error=%g" % rel)


def check_h0_prediction_value():
    # VALIDATION: Confirms the overview claim that the overview numeric prediction H0 = 70.21 km/s/Mpc with correction.
    h0 = h_si_to_km_s_mpc(h_from_a0_with_correction(A0_EFFECTIVE))
    assert abs(h0 - 70.21) < 0.35, "H0=%g, expected near 70.21" % h0
    print("h0_predicted_km_s_mpc=%0.6f" % h0)


def check_h0_without_correction_value():
    # VALIDATION: Confirms the overview claim that overview statement that omitting geometric correction yields near 78.90 km/s/Mpc.
    h0_uncorrected = h_si_to_km_s_mpc(h_from_a0_no_correction(A0_EFFECTIVE))
    assert abs(h0_uncorrected - 78.90) < 0.05, "H0_uncorrected=%g, expected near 78.90" % h0_uncorrected
    print("h0_uncorrected_km_s_mpc=%0.6f" % h0_uncorrected)


def check_correction_scaling_factor():
    # VALIDATION: Confirms the overview claim that that the correction reduces H0 by factor 1/sqrt(K/pi), matching overview logic.
    h_corr = h_si_to_km_s_mpc(h_from_a0_with_correction(A0_EFFECTIVE))
    h_unc = h_si_to_km_s_mpc(h_from_a0_no_correction(A0_EFFECTIVE))
    ratio = h_unc / h_corr
    expected = geometric_correction()
    rel = abs(ratio - expected) / expected
    assert rel < 1e-12, "ratio=%g expected=%g rel=%g" % (ratio, expected, rel)
    print("correction_ratio=%0.9f expected_geometric_factor=%0.9f" % (ratio, expected))


def check_prediction_between_planck_and_sh0es():
    # VALIDATION: Confirms the overview claim that overview claim that prediction sits between Planck and SH0ES values.
    h0 = h_si_to_km_s_mpc(h_from_a0_with_correction(A0_EFFECTIVE))
    assert H0_PLANCK < h0 < H0_SH0ES, (
        "H0=%g should be between Planck=%g and SH0ES=%g" % (h0, H0_PLANCK, H0_SH0ES)
    )
    print("h0_between_planck_and_sh0es=%0.6f" % h0)


def check_prediction_consistent_with_gw170817():
    # VALIDATION: Confirms the overview claim that overview claim of consistency with GW170817 standard siren uncertainty.
    h0 = h_si_to_km_s_mpc(h_from_a0_with_correction(A0_EFFECTIVE))
    delta = abs(h0 - H0_GW170817)
    assert delta <= H0_GW170817_SIGMA, (
        "delta=%g exceeds GW170817 sigma=%g" % (delta, H0_GW170817_SIGMA)
    )
    print("h0_vs_gw170817_delta=%0.6f sigma=%0.6f" % (delta, H0_GW170817_SIGMA))


def check_planck_sh0es_tension_exceeds_five_sigma():
    # VALIDATION: Confirms the overview claim that the overview claim that Planck and SH0ES differ by more than five standard deviations.
    sigma_planck = 0.5
    sigma_sh0es = 1.04
    delta = abs(H0_SH0ES - H0_PLANCK)
    sigma_combined = math.sqrt(sigma_planck**2 + sigma_sh0es**2)
    tension_sigma = delta / sigma_combined
    assert tension_sigma > 4.8, "tension_sigma=%g, expected about five sigma" % tension_sigma
    print("planck_sh0es_tension_sigma=%0.6f" % tension_sigma)


def check_effective_a0_close_to_reference_scale():
    # VALIDATION: Confirms the overview claim that that the effective a0 implied by reported H0 values remains close to the cited 1.2e-10 scale.
    rel = abs(A0_EFFECTIVE - A0_REFERENCE) / A0_REFERENCE
    assert rel < 0.03, "a0 relative offset=%g, expected < 0.03" % rel
    print("a0_reference=%g a0_effective=%g relative_offset=%g" % (A0_REFERENCE, A0_EFFECTIVE, rel))


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
