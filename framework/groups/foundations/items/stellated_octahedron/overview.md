# The Stellated Octahedron

The previous nine pages constructed the gravitational field envelope piece by piece: field closure selected the simplex, the simplex fixed K = 4 and D = 3, the dual chamber requirement doubled the structure, and the 28 geometric elements catalogued every component. This page presents the complete object.
![Figure 1, Stellated octahedron [interactive:fig1_dual_tetrahedral_field_chamber.html]](/framework/assets/foundations/stellated_octahedron/stellated_octahedron.png)

Figure 1. The dual tetrahedral field chamber. Four million points are sampled uniformly in local frame coordinates and tested against the half space inequalities $L_i(p)$ defined in the text. Points that satisfy the TetA bounds are shown in cyan, those satisfying TetB in red, and those inside both, the shared octahedral Field Origin, in gold. No mesh or curve fitting is used. Each face of TetA is subdivided into three exposed corners and one inverted core where the opposing vertex penetrates, giving $4 \times 4 = 16$ geometric channels.

Two tetrahedra, interlocked, sharing a single centre. One points up, one points down. Every vertex of one sits at the centre of a face of the other. The blue field chamber and the gold field chamber interpenetrate completely, coupled at the Field Origin where both meet. This is the stellated octahedron, and it is the topology of the gravitational field at every point in spacetime.

## What You Are Looking At

A tetrad is a set of four vector fields. In the local orthonormal frame, the spatial components of a regular tetrad point along four directions: the four face normals of a tetrahedron. These directions can be written as four linear projections of the local coordinates:

$$
v_1 = x + y + z, \quad v_2 = x - y - z, \quad v_3 = -x + y - z, \quad v_4 = -x - y + z
$$

The primary field chamber (TetA) is the region where all four projections are bounded:

$$
\text{TetA}: \quad \max(v_1, v_2, v_3, v_4) \leq 1
$$

The inverted dual (TetB) satisfies the opposite inequality:

$$
\text{TetB}: \quad \max(-v_1, -v_2, -v_3, -v_4) \leq 1
$$

Their intersection is the central octahedral region, the Field Origin. Their union is the stellated octahedron.

These three elements, a tetrad, its dual, and the coupling point where they meet, are not new theoretical postulates. They are implicit in every tetrad-based formulation of bimetric gravity. What has not previously been extracted is the consequence of their combinatorial geometry.

Figure 1 shows the result of evaluating these half-space inequalities at four million randomly sampled points in local frame coordinates. No mesh is constructed; the geometry emerges from the boundaries alone. On each face of TetA, the penetration by TetB's opposing vertex subdivides the surface into four sub-regions: three spatial corners and one central inverted core. This $3 + 1$ subdivision, repeated across all four faces, produces exactly $4 \times 4 = 16$ independent boundary channels. The channel count is visible in the figure before it is proven in the derivation.

Eight vertices, four per tetrahedron, split by binary parity into two groups of four. Twelve edges, six per tetrahedron, all the same length, forming the structural skeleton. Eight triangular faces, four per chamber, defining the chamber geometry. Four coupled faces between TetA and TetB carrying the active interaction. And at the centre, the Field Origin, where both chambers meet and all four body diagonals cross. These are the 28 geometric elements catalogued on the previous page, now assembled into one object.
## Why Two Chambers, Not One

A single tetrahedron would satisfy the simplex theorem, four faces enclosing a volume. But a single chamber is not self consistent. Four independent lines of argument, two from textbook physics and two from the modern gravity literature, all require a second tetrahedron with opposite orientation:

**Stability.** A lone tetrahedron has a preferred direction, an apex pointing somewhere. This asymmetry produces a ghost: a field mode with negative kinetic energy that would destabilise the vacuum. A second chamber with opposite orientation cancels the asymmetry.
**Spinor structure.** Fermions require the SL(2,C) double cover of the Lorentz group. Rotate a fermion by 360 degrees and it does not return to its original state; a full 720 degree rotation is needed. Each tetrahedron realises one sheet of the double cover. The stellated octahedron is what makes 720 degree periodicity geometric.
**Chirality.** Ashtekar's formulation decomposes gravity into self dual and anti self dual halves, left handed and right handed components that cannot be superimposed. Full field closure requires both. Each half corresponds to one chamber. (Ashtekar, 1986)
**Bimetric gravity.** Hassan and Rosen ghost free theory requires two dynamical metrics, each decomposed into its own tetrad field: $g = E^{T}\eta E$ and $f = L^{T}\eta L$. The spatial triad of each tetrad can be interpreted as a tetrahedral frame. Two tetrads, two tetrahedra, coupled through a single interaction potential with five coefficients $\beta_0$ through $\beta_4$. The stellated octahedron is the geometric picture this structure suggests when drawn.
No other arrangement satisfies all four requirements simultaneously. Tetrahedra placed side by side break the central symmetry. Tetrahedra sharing an apex fail to provide the full spinor doubling. Only two tetrahedra of opposite orientation sharing a common centre, the stellated octahedron, has both the dual structure needed for stability and the shared coupling point needed for bimetric interaction. The structure is not chosen. It is required.
## The Complete Inventory

| Element | Count | Physical identity |
|---|---|---|
| Vertices | 8 = 2^D | Binary state space {0,1}^3 |
| Edges | 12 = 2 x C(K,2) | Lorentz generators / spin connection |
| Faces | 8 = 2K | Geometric chamber faces, 4 per chamber |
| Coupled faces | 4 = K | Active TetA TetB face couplings |
| Temporal | 2 | Point inward toward Field Origin |
| Spatial | 6 | Point outward into space |
| Sub channels | 16 = K^2 | 4 per coupled face |
| Body diagonals | 4 = K | Coupling axes through Field Origin |
| Field Origin | 1 | Centre where both chambers meet |
| **Total elements** | **28 = V+E+F** | **K(K+D) = 4 x 7** |

Everything in this table is determined by two integers: K = 4 and D = 3. Those two integers are themselves determined by a single equation: 2(D+1) = 2^D. One equation, one geometry, zero free parameters.
## What Comes Next

The Foundations section is complete. You now hold the full geometry of the gravitational field envelope, its vertices, edges, faces, sub channels, coupling axes, spin, and the characteristic scale where the two chambers balance. Nothing has been fitted to data. Everything follows from field closure in three spatial dimensions.

The Gravitation section reads this geometry. The coupling polynomial f(K, s) = 1 + Ks + K^2 will encode how deeply the field couples at each structural level. The constitutive law mu(x) = x/(x+1) will emerge as normalised capacity. The scalar tensor action will provide the covariant field equations. And the predictions, the gravitational constant, the fine structure constant, galactic rotation curves, will follow from the same 28 elements you have just counted, with nothing added and nothing adjusted.

## References

Ashtekar, A. (1986). New Variables for Classical and Quantum Gravity. Phys. Rev. Lett. 57, 2244.
