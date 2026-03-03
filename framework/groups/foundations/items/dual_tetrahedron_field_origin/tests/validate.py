"""Dual tetrahedron and field origin overview validation suite.

This validate.py file validates overview claims only.
Each check maps to an explicit statement from overview.md.
"""

import itertools


K = 4
D = 3
ODD_GROUP = [1, 2, 4, 7]
EVEN_GROUP = [0, 3, 5, 6]


def popcount(n):
    """Count active bits in integer n."""
    return bin(n).count("1")


def bits_to_coord(v):
    """Map 3 bit vertex index to cube coordinates in {-1, +1}^3."""
    return tuple(1 if ((v >> i) & 1) else -1 for i in range(3))


def squared_distance(a, b):
    """Squared Euclidean distance."""
    return sum((x - y) ** 2 for x, y in zip(a, b))


def edge_set(vertices):
    """Undirected edge set for complete graph on given vertices."""
    edges = set()
    for a, b in itertools.combinations(sorted(vertices), 2):
        edges.add((a, b))
    return edges


def check_parity_partition_groups():
    # VALIDATION: Confirms the overview claim that parity partition into odd and even popcount groups.
    odd = sorted(v for v in range(8) if popcount(v) % 2 == 1)
    even = sorted(v for v in range(8) if popcount(v) % 2 == 0)
    assert odd == ODD_GROUP, "odd group=%s expected=%s" % (odd, ODD_GROUP)
    assert even == EVEN_GROUP, "even group=%s expected=%s" % (even, EVEN_GROUP)
    print("odd_group=%s even_group=%s" % (odd, even))


def check_group_sizes():
    # VALIDATION: Confirms the overview claim that each parity group has exactly four vertices.
    assert len(ODD_GROUP) == 4, "odd size=%d expected 4" % len(ODD_GROUP)
    assert len(EVEN_GROUP) == 4, "even size=%d expected 4" % len(EVEN_GROUP)
    print("odd_size=%d even_size=%d" % (len(ODD_GROUP), len(EVEN_GROUP)))


def check_each_group_is_regular_tetrahedron():
    # VALIDATION: Confirms the overview claim that regular tetrahedron property from equal pairwise distances.
    for name, group in [("odd", ODD_GROUP), ("even", EVEN_GROUP)]:
        coords = [bits_to_coord(v) for v in group]
        d2_values = sorted(
            squared_distance(coords[i], coords[j])
            for i in range(len(coords))
            for j in range(i + 1, len(coords))
        )
        assert len(d2_values) == 6, "%s pair count=%d expected 6" % (name, len(d2_values))
        assert all(d == d2_values[0] for d in d2_values), (
            "%s distances not uniform: %s" % (name, d2_values)
        )
        print("%s_group_distance_squared=%d" % (name, d2_values[0]))


def check_vertex_disjoint_complete_partition():
    # VALIDATION: Confirms the overview claim that chambers are vertex disjoint and cover all cube vertices.
    odd_set = set(ODD_GROUP)
    even_set = set(EVEN_GROUP)
    assert odd_set.isdisjoint(even_set), "groups must be vertex disjoint"
    assert sorted(odd_set | even_set) == list(range(8)), "partition does not cover all vertices"
    print("partition_complete=True")


def check_edge_disjoint_chambers():
    # VALIDATION: Confirms the overview claim that chamber edge sets are disjoint as stated in overview.
    odd_edges = edge_set(ODD_GROUP)
    even_edges = edge_set(EVEN_GROUP)
    overlap = odd_edges & even_edges
    assert len(odd_edges) == 6, "odd edge count=%d expected 6" % len(odd_edges)
    assert len(even_edges) == 6, "even edge count=%d expected 6" % len(even_edges)
    assert not overlap, "edge overlap found=%s" % sorted(overlap)
    print("odd_edges=%d even_edges=%d overlap=%d" % (len(odd_edges), len(even_edges), len(overlap)))


def check_body_diagonal_pairs_midpoint_origin():
    # VALIDATION: Confirms the overview claim that listed opposite vertex pairs have midpoint at field origin.
    pairs = [(0, 7), (1, 6), (2, 5), (3, 4)]
    for a, b in pairs:
        ca = bits_to_coord(a)
        cb = bits_to_coord(b)
        midpoint = tuple((x + y) / 2.0 for x, y in zip(ca, cb))
        assert midpoint == (0.0, 0.0, 0.0), "pair (%d,%d) midpoint=%s" % (a, b, midpoint)
    print("body_diagonal_midpoints_at_origin=True")


def check_all_vertex_vectors_cancel_to_zero():
    # VALIDATION: Confirms the overview claim that vector cancellation of all eight cube corners at origin.
    sx = sy = sz = 0
    for v in range(8):
        x, y, z = bits_to_coord(v)
        sx += x
        sy += y
        sz += z
    assert (sx, sy, sz) == (0, 0, 0), "sum vector=(%d,%d,%d) expected (0,0,0)" % (sx, sy, sz)
    print("vector_sum=(%d,%d,%d)" % (sx, sy, sz))


def check_structural_inventory_from_k_d():
    # VALIDATION: Confirms the overview claim that structural inventory relations from K and D.
    vertices = 2**D
    edges = K * D
    elements = K * D + 1
    channels = K**2
    assert vertices == 8, "vertices=%d expected 8" % vertices
    assert edges == 12, "edges=%d expected 12" % edges
    assert elements == 13, "elements=%d expected 13" % elements
    assert channels == 16, "channels=%d expected 16" % channels
    print("vertices=%d edges=%d elements=%d channels=%d" % (vertices, edges, elements, channels))


def check_total_edge_count_two_tetrahedra():
    # VALIDATION: Confirms the overview claim that two tetrahedra produce total edge count twelve.
    total = len(edge_set(ODD_GROUP)) + len(edge_set(EVEN_GROUP))
    assert total == 12, "total edges=%d expected 12" % total
    print("total_chamber_edges=%d" % total)


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
