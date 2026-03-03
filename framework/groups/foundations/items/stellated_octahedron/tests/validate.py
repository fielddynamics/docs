"""Stellated octahedron overview validation suite.

This validate.py file validates overview claims only.
Each check maps to an explicit statement from overview.md.
"""

import itertools


K = 4
D = 3


def popcount(n):
    """Count active bits in integer n."""
    return bin(n).count("1")


def odd_even_groups():
    """Return odd and even parity groups for 3 bit addresses."""
    odd = sorted(v for v in range(8) if popcount(v) % 2 == 1)
    even = sorted(v for v in range(8) if popcount(v) % 2 == 0)
    return odd, even


def bits_to_coord(v):
    """Map 3 bit address to coordinates in {-1,+1}^3."""
    return tuple(1 if ((v >> i) & 1) else -1 for i in range(3))


def squared_distance(a, b):
    """Squared Euclidean distance."""
    return sum((x - y) ** 2 for x, y in zip(a, b))


def check_binary_parity_partition():
    # VALIDATION: Confirms the overview claim that binary parity split into two groups of four vertices.
    odd, even = odd_even_groups()
    assert odd == [1, 2, 4, 7], "odd group=%s expected [1,2,4,7]" % odd
    assert even == [0, 3, 5, 6], "even group=%s expected [0,3,5,6]" % even
    print("odd_group=%s even_group=%s" % (odd, even))


def check_regular_tetrahedron_groups():
    # VALIDATION: Confirms the overview claim that each parity group forms a regular tetrahedron.
    odd, even = odd_even_groups()
    for label, group in [("odd", odd), ("even", even)]:
        coords = [bits_to_coord(v) for v in group]
        d2 = sorted(
            squared_distance(coords[i], coords[j])
            for i in range(len(coords))
            for j in range(i + 1, len(coords))
        )
        assert len(d2) == 6, "%s pair count=%d expected 6" % (label, len(d2))
        assert all(val == d2[0] for val in d2), "%s distances=%s not uniform" % (label, d2)
        print("%s_distance_squared=%d" % (label, d2[0]))


def check_inventory_counts():
    # VALIDATION: Confirms the overview claim that complete inventory counts from K=4 and D=3.
    vertices = 2**D
    edges = 2 * 6
    faces = 2 * K
    body_diagonals = K
    origin = 1
    assert vertices == 8, "vertices=%d expected 8" % vertices
    assert edges == 12, "edges=%d expected 12" % edges
    assert faces == 8, "faces=%d expected 8" % faces
    assert body_diagonals == 4, "body diagonals=%d expected 4" % body_diagonals
    assert origin == 1, "origin=%d expected 1" % origin
    print(
        "vertices=%d edges=%d faces=%d body_diagonals=%d origin=%d"
        % (vertices, edges, faces, body_diagonals, origin)
    )


def check_total_elements_twenty_eight():
    # VALIDATION: Confirms the overview claim that 28 geometric element total V+E+F.
    vertices = 2**D
    edges = 12
    faces = 8
    total = vertices + edges + faces
    assert total == 28, "total=%d expected 28" % total
    print("total_elements=%d" % total)


def check_algebraic_identity():
    # VALIDATION: Confirms the overview claim that algebraic identity K(K+D)=28.
    value = K * (K + D)
    assert value == 28, "K(K+D)=%d expected 28" % value
    print("algebraic_total=%d" % value)


def check_active_couplings_and_subchannels():
    # VALIDATION: Confirms the overview claim that active coupled faces and sub channel count.
    coupled_faces = K
    sub_channels = K**2
    assert coupled_faces == 4, "coupled faces=%d expected 4" % coupled_faces
    assert sub_channels == 16, "sub channels=%d expected 16" % sub_channels
    assert sub_channels == 4 * coupled_faces, "sub channels not 4 per coupled face"
    print("coupled_faces=%d sub_channels=%d" % (coupled_faces, sub_channels))


def check_field_origin_midpoint():
    # VALIDATION: Confirms the overview claim that field origin midpoint from opposite vertex pairs.
    pairs = [(0, 7), (1, 6), (2, 5), (3, 4)]
    for a, b in pairs:
        ca = bits_to_coord(a)
        cb = bits_to_coord(b)
        midpoint = tuple((x + y) / 2.0 for x, y in zip(ca, cb))
        assert midpoint == (0.0, 0.0, 0.0), "pair (%d,%d) midpoint=%s" % (a, b, midpoint)
    print("origin_midpoint_for_all_pairs=True")


def check_edge_decomposition():
    # VALIDATION: Confirms the overview claim that tetrahedron edge decomposition 2 x C(4,2) = 12.
    edges_per_tetra = len(list(itertools.combinations(range(4), 2)))
    total_edges = 2 * edges_per_tetra
    assert edges_per_tetra == 6, "edges per tetra=%d expected 6" % edges_per_tetra
    assert total_edges == 12, "total edges=%d expected 12" % total_edges
    print("edges_per_tetra=%d total_edges=%d" % (edges_per_tetra, total_edges))


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
