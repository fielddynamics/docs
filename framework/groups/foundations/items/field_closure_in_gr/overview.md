# Field Closure in GR

Field closure is not something added to general relativity. It is something general relativity has always required. This page shows where it already lives, in five independent formalisms, each developed by different research groups across six decades, all enforcing the same geometric condition.

## The Metric Condition

The most familiar form is the simplest. In standard general relativity, the metric tensor $g$ describes the geometry of spacetime at every point. For Einstein's field equations to have meaning, the metric must be invertible: its determinant must never vanish. This is written $\det(g) \ne 0$. (Einstein, 1915)

Without this condition, the mathematics breaks. You cannot raise or lower indices. You cannot define distances, angles, or causal structure. You cannot write down the Einstein equations themselves. Every textbook states this requirement, usually in a brief aside, and moves on. It is treated as a technicality, a condition you verify and forget.

But consider what it actually says. The determinant of the metric vanishes when the four basis directions at a point become degenerate: when one direction collapses, or two directions align, or the local frame loses a dimension. $\det(g) \ne 0$ is the demand that four independent directions remain intact at every point, at every moment, everywhere in the universe. That is field closure.

## Five Formalisms, One Condition

General relativity can be written in several equivalent mathematical languages. Each one expresses the closure condition differently, but the geometric content is the same.
**Metric GR** (Einstein, 1915). The metric tensor must be non degenerate: $\det(g) \ne 0$. Four independent directions must span the tangent space at every point.

**Tetrad gravity** (Einstein, 1928; Cartan, 1922). The metric decomposes into four basis vectors, the tetrad, as $g = \eta\,e\,e$. The closure condition becomes $\det(e) \ne 0$: four linearly independent legs must stand at every point. The tetrad is not an abstraction. It is the local frame of the equivalence principle, made explicit. Its four legs are the four directions that field closure protects.

**ADM formalism** (Arnowitt, Deser, Misner 1962). Spacetime is sliced into spatial hypersurfaces evolving in time. The field equations decompose into four constraint equations: one Hamiltonian constraint governing the temporal direction, and three momentum constraints governing the three spatial directions. 1 + 3 = 4. These four constraints are the four coupling channels through which each spatial slice maintains consistency with its neighbours. If any constraint fails, the geometry is not preserved under evolution. Closure fails.

**Regge calculus** (Regge 1961). Curved spacetime is approximated by flat simplices glued along shared faces. In three spatial dimensions, the fundamental simplex is the tetrahedron: four vertices, four faces, enclosing volume. The curvature lives at the hinges where simplices meet. Each tetrahedron is a discrete unit of closed geometry, the lattice version of the same condition that det(g) != 0 enforces in the continuum.

**Loop Quantum Gravity** (Rovelli, Vidotto 2014). At the Planck scale, geometry is quantised. The quantum of three dimensional space is the quantum tetrahedron, defined by four face normal vectors satisfying the Barbieri closure condition: the four normals must sum to zero. This is the discrete quantum version of the same requirement. Four faces. Closed boundary. No gaps.

## The Pattern

| Formalism | Closure condition | What k = 4 counts |
|---|---|---|
| Metric GR | $\det(g) \ne 0$ | 4 independent tangent directions |
| Tetrad gravity | $\det(e) \ne 0$ | 4 basis vectors (tetrad legs) |
| ADM formalism | 4 constraints satisfied | 1 temporal + 3 spatial channels |
| Regge calculus | Simplex closes | 4 faces of the tetrahedron |
| Loop Quantum Gravity | Barbieri condition | 4 face normals summing to zero |

Five formalisms. Five languages. One geometric fact: at every point in three dimensional space, four independent directions must close around a volume. The number four is not a coincidence that appears across these frameworks. It is a single requirement, field closure, expressed in five different mathematical dialects.

## What This Means for the Framework

Gravity Field Dynamics does not introduce field closure as a new postulate. It recognises that general relativity has been enforcing it all along, in every formalism, at every scale, from the continuum metric to the quantum tetrahedron. The contribution of this framework is not to add a new condition. It is to take the condition seriously: to follow it from $\det(g) \ne 0$ through to its geometric consequences, and to ask what structure the closure produces when you let the geometry speak for itself.
The answer, two interlocking tetrahedra forming the stellated octahedron, is not imposed. It is what you get when four faces close in three dimensions and stability demands two chambers rather than one. Every formalism listed above contains this structure implicitly. This framework makes it explicit.

## References

Einstein, A. (1915). Die Feldgleichungen der Gravitation. Sitzungsber. Preuss. Akad. Wiss. 844.

Einstein, A. (1928). Riemann Geometrie mit Aufrechterhaltung des Begriffes des Fernparallelismus. Sitzungsber. Preuss. Akad. Wiss. Phys. Math. Kl. 217, 224.

Cartan, E. (1922). Sur une generalisation de la notion de courbure de Riemann et les espaces a torsion. C. R. Acad. Sci. (Paris) 174, 593.
