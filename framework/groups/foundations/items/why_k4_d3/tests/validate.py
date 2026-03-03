"""Why k = 4 and d = 3 overview validation suite.

This validate.py file validates overview claims only.
Each check maps to an explicit statement from overview.md.
"""

K = 4
D = 3


def simplex_face_count(d):
    """Minimum simplex boundary count in d dimensions."""
    return d + 1


def uniqueness_lhs(d):
    """Left side of uniqueness equation 2(d+1)."""
    return 2 * (d + 1)


def uniqueness_rhs(d):
    """Right side of uniqueness equation 2^d."""
    return 2**d


def popcount(n):
    """Count active bits in integer n."""
    return bin(n).count("1")


def check_simplex_theorem_k_from_d():
    # VALIDATION: Confirms the overview claim that simplex theorem mapping d=3 to k=d+1=4.
    k_from_d = simplex_face_count(D)
    assert k_from_d == K, "k_from_d=%d expected %d" % (k_from_d, K)
    print("d=%d k=%d" % (D, k_from_d))


def check_uniqueness_equation_at_d3():
    # VALIDATION: Confirms the overview claim that exact match of uniqueness equation at d=3.
    lhs = uniqueness_lhs(D)
    rhs = uniqueness_rhs(D)
    assert lhs == rhs == 8, "lhs=%d rhs=%d expected 8" % (lhs, rhs)
    print("d3_lhs=%d d3_rhs=%d" % (lhs, rhs))


def check_uniqueness_equation_nearby_dimensions():
    # VALIDATION: Confirms the overview claim that mismatch for nearby dimensions listed in overview.
    mismatches = []
    for d in [1, 2, 4, 5]:
        lhs = uniqueness_lhs(d)
        rhs = uniqueness_rhs(d)
        if lhs == rhs:
            raise AssertionError("unexpected equality at d=%d" % d)
        mismatches.append((d, lhs, rhs))
    print("nearby_dimension_mismatches=%s" % mismatches)


def check_uniqueness_positive_integer_solution():
    # VALIDATION: Confirms the overview claim that uniqueness of positive integer solution over a broad search.
    solutions = [d for d in range(1, 33) if uniqueness_lhs(d) == uniqueness_rhs(d)]
    assert solutions == [3], "solutions=%s expected [3]" % solutions
    print("positive_integer_solutions=%s" % solutions)


def check_linear_exponential_divergence_after_d3():
    # VALIDATION: Confirms the overview claim that linear versus exponential divergence after d=3.
    previous_gap = None
    for d in range(4, 11):
        gap = uniqueness_rhs(d) - uniqueness_lhs(d)
        assert gap > 0, "gap must be positive at d=%d, got=%d" % (d, gap)
        if previous_gap is not None:
            assert gap > previous_gap, "gap should grow from d=%d to d=%d" % (d - 1, d)
        previous_gap = gap
    print("gap_at_d10=%d" % previous_gap)


def check_two_simplices_match_cube_vertices():
    # VALIDATION: Confirms the overview claim that two simplices and cube vertex counts coincide only at d=3.
    simplex_vertices = 2 * (D + 1)
    cube_vertices = 2**D
    assert simplex_vertices == cube_vertices == 8, (
        "simplex_vertices=%d cube_vertices=%d expected 8" % (simplex_vertices, cube_vertices)
    )
    print("two_simplices_vertices=%d cube_vertices=%d" % (simplex_vertices, cube_vertices))


def check_binary_parity_partition_counts():
    # VALIDATION: Confirms the overview claim that 3-bit parity split yields two groups of four vertices.
    even = []
    odd = []
    for v in range(8):
        if popcount(v) % 2 == 0:
            even.append(v)
        else:
            odd.append(v)
    assert len(even) == 4, "even count=%d expected 4" % len(even)
    assert len(odd) == 4, "odd count=%d expected 4" % len(odd)
    assert sorted(even + odd) == list(range(8)), "partition does not cover all vertices"
    print("even_vertices=%s odd_vertices=%s" % (even, odd))


def check_parity_classes_form_tetra_vertex_counts():
    # VALIDATION: Confirms the overview claim that each parity class has four vertices, matching tetrahedron vertex count.
    target = D + 1
    even_count = sum(1 for v in range(8) if popcount(v) % 2 == 0)
    odd_count = sum(1 for v in range(8) if popcount(v) % 2 == 1)
    assert even_count == target, "even_count=%d expected %d" % (even_count, target)
    assert odd_count == target, "odd_count=%d expected %d" % (odd_count, target)
    print("parity_class_size=%d target=d_plus_1=%d" % (even_count, target))


def check_tetrahedron_requires_four_points():
    # VALIDATION: Confirms the overview claim that simplex enclosure claim that 3 points give no volume while 4 non coplanar points do.
    # Three points define a triangle in z=0 plane.
    p0 = (0.0, 0.0, 0.0)
    p1 = (1.0, 0.0, 0.0)
    p2 = (0.0, 1.0, 0.0)
    # Add a fourth point off plane to form tetrahedron.
    p3 = (0.0, 0.0, 1.0)

    # Tetra volume is |det(v1, v2, v3)|/6.
    v1 = (p1[0] - p0[0], p1[1] - p0[1], p1[2] - p0[2])
    v2 = (p2[0] - p0[0], p2[1] - p0[1], p2[2] - p0[2])
    v3 = (p3[0] - p0[0], p3[1] - p0[1], p3[2] - p0[2])
    det = (
        v1[0] * (v2[1] * v3[2] - v2[2] * v3[1])
        - v1[1] * (v2[0] * v3[2] - v2[2] * v3[0])
        + v1[2] * (v2[0] * v3[1] - v2[1] * v3[0])
    )
    volume = abs(det) / 6.0
    assert volume > 0.0, "tetra volume should be positive, got %g" % volume
    print("tetra_volume=%g" % volume)


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
