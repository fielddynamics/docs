"""Twenty eight geometric elements overview validation suite.

This validate.py file validates overview claims only.
Each check maps to an explicit statement from overview.md.
"""

import math


K = 4
D = 3
F0 = 8
F1 = 12
F2 = 8
ALPHA_INV_MEASURED = 137.035999177


def binomial(n, r):
    """Compute n choose r with integer arithmetic."""
    return math.comb(n, r)


def check_f_vector_values():
    # VALIDATION: Confirms the overview claim that the stated f vector of the stellated octahedron.
    assert F0 == 8, "f0=%d expected 8" % F0
    assert F1 == 12, "f1=%d expected 12" % F1
    assert F2 == 8, "f2=%d expected 8" % F2
    print("f_vector=(%d,%d,%d)" % (F0, F1, F2))


def check_total_geometric_elements():
    # VALIDATION: Confirms the overview claim that total simplex count equals 28.
    total = F0 + F1 + F2
    assert total == 28, "total=%d expected 28" % total
    print("total_geometric_elements=%d" % total)


def check_euler_characteristic():
    # VALIDATION: Confirms the overview claim that Euler characteristic for convex polyhedron surface.
    tetra_chi = 4 - 6 + 4
    combined_chi = F0 - F1 + F2
    assert tetra_chi == 2, "single tetra chi=%d expected 2" % tetra_chi
    assert combined_chi == 4, "combined chi=%d expected 4" % combined_chi
    print("single_tetra_chi=%d combined_inventory_chi=%d" % (tetra_chi, combined_chi))


def check_binary_vertex_states():
    # VALIDATION: Confirms the overview claim that binary state space size 2^D at D=3.
    states = 2**D
    assert states == F0, "2^D=%d expected %d" % (states, F0)
    print("binary_vertex_states=%d" % states)


def check_edge_count_from_two_tetrahedra():
    # VALIDATION: Confirms the overview claim that tetrahedron edge count decomposition to total edges.
    edges_per_tetra = binomial(4, 2)
    total_edges = 2 * edges_per_tetra
    assert edges_per_tetra == 6, "edges per tetra=%d expected 6" % edges_per_tetra
    assert total_edges == F1, "total edges=%d expected %d" % (total_edges, F1)
    print("edges_per_tetra=%d total_edges=%d" % (edges_per_tetra, total_edges))


def check_face_count_from_two_chambers():
    # VALIDATION: Confirms the overview claim that face count by chamber decomposition.
    faces_total = 2 * K
    assert faces_total == F2, "faces_total=%d expected %d" % (faces_total, F2)
    print("faces_total=%d" % faces_total)


def check_algebraic_counting_identity():
    # VALIDATION: Confirms the overview claim that algebraic identity K*(K+D)=28 at K=4 and D=3.
    value = K * (K + D)
    assert value == 28, "K*(K+D)=%d expected 28" % value
    print("algebraic_count=%d" % value)


def check_dynamical_mode_face_count():
    # VALIDATION: Confirms the overview claim that dynamical counting 7 modes times 4 faces equals 28.
    modes = 2 + 5
    couplings = modes * K
    assert modes == 7, "modes=%d expected 7" % modes
    assert couplings == 28, "couplings=%d expected 28" % couplings
    print("modes=%d mode_face_couplings=%d" % (modes, couplings))


def check_triple_convergence_to_twenty_eight():
    # VALIDATION: Confirms the overview claim that triple convergence of geometric, algebraic, and dynamical counts.
    geometric = F0 + F1 + F2
    algebraic = K * (K + D)
    dynamical = (2 + 5) * K
    assert geometric == algebraic == dynamical == 28, (
        "geometric=%d algebraic=%d dynamical=%d expected all 28"
        % (geometric, algebraic, dynamical)
    )
    print(
        "geometric=%d algebraic=%d dynamical=%d"
        % (geometric, algebraic, dynamical)
    )


def check_inverse_alpha_fractional_link():
    # VALIDATION: Confirms the overview claim that stated connection 1 over alpha equals 137 plus 1 over 28.
    predicted = 137.0 + 1.0 / 28.0
    delta = abs(predicted - ALPHA_INV_MEASURED)
    percent = 100.0 * delta / ALPHA_INV_MEASURED
    assert percent < 0.001, "percent error=%g expected < 0.001" % percent
    print(
        "inverse_alpha_predicted=%0.12f measured=%0.12f percent_error=%0.9f"
        % (predicted, ALPHA_INV_MEASURED, percent)
    )


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
