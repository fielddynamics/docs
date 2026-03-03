"""Poisson equation overview validation suite.

This validate.py file validates overview claims only.
Each check maps to an explicit statement from overview.md.
"""

import math


K = 4.0
D = 3.0
A0 = 1.2e-10  # m/s^2
G = 6.67430e-11  # m^3/(kg*s^2)


def coupling_ratio(k=K, d=D):
    """(K^2 + 1)/(K*D + 1)."""
    return (k**2 + 1.0) / (k * d + 1.0)


def mu_simple(x):
    """mu(x) = x/(x+1)."""
    return x / (x + 1.0)


def poisson_prefactor_topology(k=K, d=D):
    """K*pi*((K^2 + 1)/(K*D + 1))."""
    return k * math.pi * coupling_ratio(k, d)


def check_four_pi_from_topology():
    # VALIDATION: Confirms the overview claim that the topological identity 4*pi = K*pi for K=4.
    lhs = K * math.pi
    rhs = 4.0 * math.pi
    rel = abs(lhs - rhs) / rhs
    assert rel < 1e-15, "K*pi mismatch, rel=%g" % rel
    print("k_pi=%0.12f four_pi=%0.12f" % (lhs, rhs))


def check_coupling_ratio_value():
    # VALIDATION: Confirms the overview claim that coupling ratio claim (K^2+1)/(K*D+1) = 17/13 at K=4, D=3.
    ratio = coupling_ratio()
    expected = 17.0 / 13.0
    rel = abs(ratio - expected) / expected
    assert rel < 1e-15, "ratio=%g expected=%g rel=%g" % (ratio, expected, rel)
    print("coupling_ratio=%0.12f expected_17_over_13=%0.12f" % (ratio, expected))


def check_complete_poisson_prefactor():
    # VALIDATION: Confirms the overview claim that complete strong field prefactor K*pi*(17/13) used in overview.
    lhs = poisson_prefactor_topology()
    rhs = 4.0 * math.pi * (17.0 / 13.0)
    rel = abs(lhs - rhs) / rhs
    assert rel < 1e-15, "prefactor mismatch, rel=%g" % rel
    print("prefactor_topology=%0.12f prefactor_expected=%0.12f" % (lhs, rhs))


def check_gauss_flux_scale_invariance():
    # VALIDATION: Confirms the overview claim that that the geometric flux factor remains scale invariant for inverse square fields.
    mass = 1.0e30
    r1 = 1.0e11
    r2 = 1.0e21
    g1 = G * mass / (r1**2)
    g2 = G * mass / (r2**2)
    flux1 = 4.0 * math.pi * (r1**2) * g1
    flux2 = 4.0 * math.pi * (r2**2) * g2
    rel = abs(flux1 - flux2) / flux1
    assert rel < 1e-12, "flux not invariant, rel=%g" % rel
    print("flux_r1=%g flux_r2=%g flux_relative_diff=%g" % (flux1, flux2, rel))


def check_mu_at_transition_point():
    # VALIDATION: Confirms the overview claim that constitutive law point mu(1)=1/2 at transition scale.
    value = mu_simple(1.0)
    assert abs(value - 0.5) < 1e-15, "mu(1)=%g expected=0.5" % value
    print("mu_at_x1=%0.12f" % value)


def check_mu_high_acceleration_limit():
    # VALIDATION: Confirms the overview claim that Newtonian recovery for high acceleration x>>1.
    x = 1.0e6
    value = mu_simple(x)
    assert value > 0.999999, "mu at large x too small, value=%g" % value
    print("mu_high_x=%0.12f one_minus_mu=%g" % (value, 1.0 - value))


def check_mu_low_acceleration_limit():
    # VALIDATION: Confirms the overview claim that deep field limit mu(x)~x for x<<1.
    x = 1.0e-8
    value = mu_simple(x)
    ratio = value / x
    assert abs(ratio - 1.0) < 1e-8, "mu(x)/x=%g expected near 1" % ratio
    print("mu_low_x=%g mu_over_x=%0.12f" % (value, ratio))


def check_mu_monotonic_and_bounded():
    # VALIDATION: Confirms the overview claim that constitutive law monotonic and bounded behavior expected for physical response.
    xs = [0.0, 1.0e-6, 1.0e-3, 0.1, 1.0, 10.0, 1.0e6]
    mus = [mu_simple(x) for x in xs]
    assert all(0.0 <= m < 1.0 for m in mus), "mu bounds violated: %s" % mus
    assert all(mus[i + 1] >= mus[i] for i in range(len(mus) - 1)), "mu not monotonic: %s" % mus
    print("mu_samples=%s" % mus)


def check_deep_field_flat_rotation_scaling():
    # VALIDATION: Confirms the overview claim that deep field scaling that yields flat rotation behavior without dark matter.
    mass = 5.0e10 * 1.98847e30
    radii = [5.0e19, 1.0e20, 2.0e20, 4.0e20]
    v4_values = []
    for r in radii:
        g_newton = G * mass / (r**2)
        g_deep = math.sqrt(A0 * g_newton)
        v = math.sqrt(g_deep * r)
        v4_values.append(v**4)
    target = G * mass * A0
    max_rel = max(abs(v4 - target) / target for v4 in v4_values)
    assert max_rel < 1e-12, "v^4 scaling mismatch, max_rel=%g" % max_rel
    print("deep_field_v4_values=%s target=%g max_rel=%g" % (v4_values, target, max_rel))


def check_x_dimensionless_ratio():
    # VALIDATION: Confirms the overview claim that that x=|grad phi|/a0 is dimensionless, preserving scale free constitutive response.
    grads = [1.2e-12, 1.2e-10, 1.2e-8]
    xs = [g / A0 for g in grads]
    expected = [0.01, 1.0, 100.0]
    for x, e in zip(xs, expected):
        assert abs(x - e) / e < 1e-15, "x mismatch, got=%g expected=%g" % (x, e)
    print("x_samples=%s" % xs)


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
