# Coupling Polynomial and Structural States

## Derivation

### Introduction

The Overview tab introduced the coupling polynomial $f(K, s) = 1 + sK + K^2$ by building it from the inside out: one level for existence, one for propagation, one for interaction. You saw how it evaluates to 21, 17, and 13 at the three structural states, and how those three integers propagate through the rest of the framework.

But knowing what a polynomial does is not the same as knowing why it must be that polynomial and no other. A skeptical reader, and every good physicist should be a skeptical reader, will want to see the derivation. Not a motivation, not an analogy, but a proof that the polynomial is forced.

This page provides three independent derivations. Each starts from a different set of premises. Each arrives at $f(K, s) = 1 + sK + K^2$ with $K = 4$ and no free parameters. The fact that three unrelated starting points converge on the same object is, in itself, evidence that the object is correct. But each derivation also teaches you something different about the polynomial's structure, and together they reveal why it is the only polynomial compatible with gravitational physics in three spatial dimensions.

The three derivations are:

The first is geometric. It shows that the polynomial is forced by the combinatorial anatomy of the tetrahedron, specifically by the self-duality visible in Pascal's triangle.

The second is observational. It shows that three independent physical measurements, each well established and uncontroversial, leave no room for any other polynomial.

The third is algebraic. It shows that the polynomial is already present in the standard Hamiltonian of Hassan-Rosen bimetric gravity, waiting to be read.

Each derivation is self-contained. You can read any one of them independently. But the argument is strongest when all three are taken together.

---

### Derivation 1: Self-Duality and Pascal's Row

This derivation starts from the question that most readers ask first: why does the propagation term contain $K$? The number $K = 4$ is the face count of the tetrahedron. But a tetrahedron also has 4 vertices, 6 edges, and 1 body. Why does the face count appear in the polynomial rather than the vertex count, the edge count, or some other geometric quantity?

The answer is that the question contains a false premise. It assumes a choice was made. No choice was made, because no choice exists.

**Pascal's row enumerates the simplex.**

Every simplex in every dimension has its complete geometric anatomy encoded in a single row of Pascal's triangle. For the tetrahedron, which is the simplex in three dimensions, the relevant row is row $K = 4$:

$$\binom{4}{0} = 1, \quad \binom{4}{1} = 4, \quad \binom{4}{2} = 6, \quad \binom{4}{3} = 4, \quad \binom{4}{4} = 1$$

Each entry counts a different type of geometric element. $\binom{4}{0} = 1$ counts the empty set: pure existence, the precondition for anything else. $\binom{4}{1} = 4$ counts the vertices. $\binom{4}{2} = 6$ counts the edges. $\binom{4}{3} = 4$ counts the triangular faces. $\binom{4}{4} = 1$ counts the body, the solid tetrahedron as a whole.

These five numbers are the complete parts list of the tetrahedron. They are not chosen or fitted. They are determined entirely by the value of $K$.

**The tetrahedron is self-dual.**

Now look at the row: 1, 4, 6, 4, 1. It is a palindrome. The first and last entries are equal. More importantly, the second and fourth entries are equal: $\binom{4}{1} = \binom{4}{3} = 4$. The number of vertices equals the number of faces.

This property is called self-duality, and it is rare. The dual of a polyhedron is formed by placing a vertex at the center of each face and connecting adjacent vertices. For most polyhedra, the dual is a different shape. The dual of a cube (8 vertices, 6 faces) is an octahedron (6 vertices, 8 faces). The dual of a dodecahedron (20 vertices, 12 faces) is an icosahedron (12 vertices, 20 faces). In every case, vertices and faces swap counts, and the two numbers are different.

The tetrahedron is the unique exception among regular polyhedra in three dimensions. Its dual is another tetrahedron. Vertices and faces are structurally interchangeable. There is no way, even in principle, to write a formula that uses the face count but not the vertex count, because they are the same number.

**Self-duality forces the trinomial.**

The coupling polynomial is $f(K, s) = 1 + sK + K^2$, a trinomial with three terms. Why three terms, and not five? Pascal's row has five entries. Why doesn't the polynomial have five terms, one for each type of geometric element?

Because self-duality collapses the row. The vertices and faces contribute the same count ($K = 4$), so there is no need for separate vertex and face terms. They enter the polynomial as a single propagation term, $sK$, which refers to both simultaneously and inseparably.

If the tetrahedron were not self-dual, if vertices and faces had different counts, the propagation sector would need two terms: one for vertex channels and one for face channels. The polynomial would split from a trinomial into something more complicated, and the clean three-part structure of existence, propagation, and interaction would break. Self-duality is not a nice property of the polynomial. It is a load-bearing structural requirement. Without it, the polynomial cannot close as a trinomial.

**Self-duality constrains $K$.**

This immediately constrains the value of $K$. At $K = 3$, Pascal's row gives $\binom{3}{1} = 3$ and $\binom{3}{2} = 3$. Vertices and edges are equal, not vertices and faces. The dual pairing is between the wrong types of element. At $K = 5$, Pascal's row gives $\binom{5}{1} = 5$ and $\binom{5}{3} = 10$. The self-duality breaks entirely. Vertices and faces have different counts, and the propagation term becomes ambiguous.

Only at $K = 4$ does the vertex-face duality hold, with edges ($\binom{4}{2} = 6$) as the distinct middle element. And only at $K = 4$ does the closure condition $2(D+1) = 2^D$ have a solution. These are not independent facts. The closure condition and the self-duality are two expressions of the same constraint: the tetrahedron is the unique simplex whose combinatorial structure permits a closed, unambiguous coupling polynomial.

**The interaction term absorbs the full row.**

The first term of the polynomial is $1 = \binom{4}{0}$, the first entry of Pascal's row. The second term is $K = \binom{4}{1}$, the second entry. What about the third term, $K^2 = 16$?

The sum of the full row is:

$$\binom{4}{0} + \binom{4}{1} + \binom{4}{2} + \binom{4}{3} + \binom{4}{4} = 1 + 4 + 6 + 4 + 1 = 16 = 2^4$$

The interaction term $K^2$ equals the sum of the entire row, which counts every simplicial subset of the tetrahedron: every possible combination of vertices, edges, faces, and the body, including the empty set. The interaction term does not pick out any single depth of the simplex. It absorbs the full combinatorial content of the chamber into one number.

And the equality $K^2 = 2^K$ is, once again, the closure condition. It holds only at $K = 4$. At $K = 3$, $K^2 = 9$ but $2^K = 8$. At $K = 5$, $K^2 = 25$ but $2^K = 32$. The interaction term equals the Pascal row sum if and only if the closure condition is satisfied.

**The self-duality cascades through every power.**

The self-duality of the tetrahedron does not stop at the face-vertex level. It propagates upward through every power of $K$, and at each level it prevents the polynomial from developing additional structure that would need to be resolved.

$K^0 = 1$. There is no ambiguity. Existence is singular.

$K^1 = 4$. Faces or vertices? Both. The tetrahedron is self-dual, so the distinction does not exist.

$K^2 = 16$. This can be read as 16 subchannels within one face, or as 4 faces times 4 triforce channels across the whole structure. Both give 16, because $K^2 = K \times K$ and the two factors of $K$ can be assigned either way. Self-duality at the $K^1$ level cascades into indistinguishability at the $K^2$ level.

$K^3 = 64$. All three recursion levels complete. Every distinction at every level has been absorbed. The triforce subdivision is exhaustive. This is the full field closure count.

At every power, the self-duality of the tetrahedron ensures there is one number, not two. If any of these ambiguities could not be resolved, the polynomial would need additional terms to separate the options. The fact that it remains a clean trinomial at every level is a direct consequence of $K = 4$ being the unique self-dual simplex closure.

**Summary of Derivation 1.**

The coupling polynomial $f(K, s) = 1 + sK + K^2$ is the unique trinomial whose coefficients are drawn from Pascal's row $K = 4$: the first entry (existence), the second entry (propagation), and the row sum (interaction). The trinomial structure is forced by the self-duality of the tetrahedron, which collapses vertex and face counts into a single propagation term. The value $K = 4$ is forced by the closure condition $K^2 = 2^K$, which is equivalent to the self-duality requirement. No other polynomial is compatible with these constraints.

---

### Derivation 2: Three Physical Constraints

This derivation starts from the other direction. Instead of asking what the geometry allows, it asks what the observations require. Three well-established physical facts, each from a different domain of physics, independently force $K = 4$ and the three-term polynomial structure.

**Constraint 1: Gravitational wave polarizations.**

The LIGO and Virgo collaborations measured the gravitational waves from binary neutron star merger GW170817 and determined that the signal contains exactly two tensor polarizations. This is an observational fact, not a theoretical preference.

The metric tensor $g_{\mu\nu}$ is a symmetric $4 \times 4$ matrix with 10 independent components. Physical degrees of freedom equal total components minus constraints minus gauge freedoms. Observing exactly 2 polarizations requires:

$$10 - 2K = 2$$

which gives $K = 4$. The number of tetrad legs is fixed by the number of gravitational wave polarizations. This is the only value of $K$ consistent with the LIGO measurement. A universe with $K = 3$ would produce a different polarization count. A universe with $K = 5$ would produce yet another. The measurement selects $K = 4$ uniquely.

**Constraint 2: The simplex theorem.**

In $D$ spatial dimensions, exactly $D + 1$ points are required to enclose a bounded region. This is a theorem of geometry, not an assumption of the framework. Fewer points cannot form a closed boundary. Additional points are redundant for enclosure.

In three spatial dimensions, the minimum enclosing solid has $K = D + 1 = 3 + 1 = 4$ vertices and $K = 4$ faces. This is the tetrahedron. Any coupling structure that operates in three-dimensional space must have $K = 4$ channels, because the tetrahedron is the minimal closed solid and its face count sets the channel count.

Note that this constraint and Constraint 1 arrive at $K = 4$ from completely independent premises. The LIGO measurement is observational, from gravitational wave astronomy. The simplex theorem is geometric, from pure mathematics. Their agreement is not a coincidence. It is a consistency check: the number of gravitational wave polarizations is consistent with gravity operating in three spatial dimensions. If these two constraints gave different values of $K$, the framework would be falsified.

**Constraint 3: Ghost-free bimetric coupling.**

The Boulware-Deser ghost is the most dangerous pathology in any theory that gives the graviton a mass. It is an unphysical degree of freedom with negative kinetic energy, and its presence would render a theory physically meaningless. Hassan and Rosen proved that the ghost can be eliminated if and only if the interaction between the two metric sectors takes a specific algebraic form: a potential built from elementary symmetric polynomials of the frame transition matrix $S^a_b$.

The ghost-free condition requires two things. First, two vierbein fields (tetrad fields) must exist, one for each metric sector. This is the bimetric structure: TetA and TetB. Second, the two tetrads must couple through a common point where their interaction satisfies a symmetric vielbein condition. Geometric analysis shows that this coupling point must lie at the center of a dual tetrahedral structure where both tetrads meet with opposite orientations.

This is exactly the Field Origin of the stellated octahedron: the point where TetA and TetB interpenetrate. The ghost-free condition does not merely permit the dual tetrahedral structure. It requires it.

**From constraints to polynomial.**

Each constraint forces one term of the polynomial:

The existence term ($1$) is the Field Origin, the common coupling point where both tetrads meet and where the non-degeneracy condition $\det(e) \neq 0$ must hold. Without this term, there is no coupling at all and the bimetric interaction fails. This is required by Constraint 3.

The propagation term ($K = 4$) represents the face channels through which the field extends outward from the origin. The tetrahedron has $K = 4$ faces because the simplex in three dimensions has $D + 1 = 4$ boundary elements. This is required by Constraint 2.

The interaction term ($K^2 = 16$) represents the full bimetric coupling: every face of TetA paired with every face of TetB, giving a $K \times K = 4 \times 4 = 16$ component frame transition matrix. This is required by Constraint 3 and consistent with Constraint 1.

No additional terms are possible. A $K^3$ term would require a three-dimensional coupling cell on a two-dimensional boundary, which does not exist. More concretely, the simplex theorem (Constraint 2) establishes $K = 4$ as the minimum for three-dimensional enclosure, and LIGO (Constraint 1) confirms $K = 4$ as the actual value. A polynomial with additional terms beyond $K^2$ would require a higher value of $K$ or a higher-dimensional coupling structure, both of which are excluded.

No terms can be removed. Without the existence term, the non-degeneracy condition fails. Without the propagation term, the field cannot extend through spatial channels. Without the interaction term, the bimetric coupling cannot operate.

The polynomial $f(K, s) = 1 + sK + K^2$ with $K = 4$ is the unique solution that satisfies all three constraints simultaneously.

**The state parameter $s$ is also forced.**

Of the three terms, the existence term ($1$) is a point with no spatial extent. Reversing orientation does nothing to a point. The interaction term ($K^2$) is a symmetric relationship: if TetA couples to TetB, then TetB couples to TetA regardless of direction. Neither of these terms can change between structural regions.

The propagation term ($K$) is different. It has direction. It represents the field extending through one sector's faces, and reversing the sector reverses the direction. The ghost-free condition establishes exactly two sectors with opposite orientations (TetA and TetB) and one coupling boundary between them (the Field Origin). This gives three structural configurations: propagation aligned with TetA ($s = +1$), propagation at the boundary ($s = 0$, no spatial extent for propagation), and propagation aligned with TetB ($s = -1$).

Under parity, even powers of $K$ are unchanged while odd powers change sign. The propagation term $K^1$ is the sole odd power. The state parameter $s$ is therefore the parity signature of the propagation direction: $+1$ for one orientation, $-1$ for the other, $0$ at the parity-neutral boundary.

Three structural regions, one state parameter modifying one term. No fourth configuration exists, because the ghost-free condition permits only two sectors and one boundary.

**Summary of Derivation 2.**

Three independent physical constraints, gravitational wave polarizations ($K = 4$), the simplex theorem ($K = D + 1 = 4$), and ghost-free bimetric coupling (requiring a dual tetrahedral structure with a shared origin), uniquely determine $f(K, s) = 1 + sK + K^2$ with $K = 4$. No term can be added, no term can be removed, and no coefficient can be changed without violating at least one constraint.

---

### Derivation 3: Component Counting in the Bimetric Hamiltonian

This derivation does not argue that the polynomial should exist. It shows that it already does, written into the standard formalism of bimetric gravity.

**The vierbein and its components.**

The vierbein (tetrad) $e^a_\mu$ is the fundamental variable of tetrad gravity. It connects the coordinate basis $dx^\mu$ to the orthonormal frame basis $\theta^a$. It carries two indices: a frame index $a \in \{0, 1, 2, 3\}$ labeling the four orthonormal directions (one timelike, three spacelike), and a coordinate index $\mu \in \{0, 1, 2, 3\}$ labeling the four spacetime coordinates.

The total number of vierbein components is $K \times K = 4 \times 4 = 16 = K^2$. The spacetime metric is reconstructed via $g_{\mu\nu} = \eta_{ab}\, e^a_\mu\, e^b_\nu$, where $\eta_{ab} = \text{diag}(1, -1, -1, -1)$ is the Minkowski metric. The summation over frame indices activates all $K^2 = 16$ coupling channels.

**The Hassan-Rosen interaction Hamiltonian.**

In bimetric gravity, two vierbein fields $E^a_\mu$ and $L^a_\mu$ describe the two metric sectors. The frame transition matrix $S^a_b = (E^{-1})^a_\mu\, L^\mu_b$ measures how each leg of one tetrad projects onto each leg of the other through the coupling point. It is a $4 \times 4$ matrix with 16 components.

The Hassan-Rosen interaction Hamiltonian is:

$$H_{\text{int}} = m^2 \sqrt{g} \sum_{n=0}^{4} \beta_n\, e_n(S)$$

where $e_n(S)$ are the elementary symmetric polynomials in the eigenvalues of $S$. Each polynomial $e_n$ counts $n$-fold index contractions of the frame transition matrix:

$e_0(S) = 1$. This is the existence condition: the determinant is nonzero, the coupling point exists, and the matrix $S$ is well defined.

$e_1(S) = \text{Tr}(S) = \sum_a S^a_a$. This is a single-index sum over $K = 4$ frame directions. It counts propagation: how the field extends through each of the four tetrad legs.

$e_2(S) = \frac{1}{2}\left[(\text{Tr}\,S)^2 - \text{Tr}(S^2)\right]$. This is a pairwise contraction involving $K^2$ terms. It counts the bimetric interaction: how every pair of frame directions couples across the two sectors.

The pattern is immediate. The first three elementary symmetric polynomials contain, respectively, 1 component, $K$ components, and terms involving $K^2$ components. That is the coupling polynomial: $1 + K + K^2$.

This is not pattern matching. The elementary symmetric polynomials $e_0$, $e_1$, and $e_2$ are defined by their index structure, and their index structure mirrors the coupling hierarchy: existence (zero indices), propagation (one index), interaction (two indices). The coupling polynomial is a direct transcription of the index counting in the bimetric Hamiltonian.

**The coupled face matrix is the frame transition matrix.**

The Overview tab described the coupled face matrix $C_{ab}$ of the stellated octahedron: row index $a$ labels a face of TetA, column index $b$ labels a face of TetB, and the entry $C_{ab}$ measures the coupling amplitude between those faces at the Field Origin.

The Hassan-Rosen frame transition matrix $S^a_b$ does the same thing: row index $a$ labels a vierbein leg of the first metric, column index $b$ labels a vierbein leg of the second metric, and the entry measures how one leg projects onto the other.

These are the same matrix, once you recognize that vierbein legs and tetrahedral faces are the same structural object. This identification is not a postulate. It follows from a result proved by Barbieri: at each four-valent node of the gravitational field, the closure constraint $\sum_i \vec{N}_i = 0$ on four face normals uniquely defines a tetrahedron from the spatial triad. Each vierbein leg therefore labels a face direction. The Lorentz index on $S$ and the face index on $C$ label the same geometric entity.

With this identification in hand, the block decomposition of $S$ into its $(3+1) \times (3+1)$ structure:

$S^0_0$: 1 component, the time-face to time-face coupling.

$S^0_j$ and $S^i_0$: $3 + 3 = 6$ components, the cross-couplings between time and spatial faces.

$S^i_j$: 9 components, the spatial-face to spatial-face couplings.

is exactly the ADM decomposition of the bimetric interaction into lapse, shift, and spatial triad. The $(3+1)$ structure of the vierbein is the face structure of the tetrahedron. Hassan and Kocic require compatible $(3+1)$ decompositions for both metrics, which means the block structure of $S$ is identically the face-pairing structure of the stellated octahedron.

**What the three integers count in the Hamiltonian.**

With the identification established, the three structural states of the coupling polynomial correspond to named quantities in the bimetric Hamiltonian:

$f = 17$ at the Field Origin ($s = 0$): the complete frame transition matrix $S^a_b$ provides 16 coupling channels, and the non-degeneracy condition $\det(e) \neq 0$ adds 1 for the existence of $S$ itself. Total: $16 + 1 = 17$. This is the coupling capacity: the dimensionality of the Hamiltonian interaction space.

$f = 13$ in TetB ($s = -1$): the coupling projects onto spatial dimensions. Each of the $K = 4$ face channels projects onto $D = 3$ spatial dimensions, giving $K \times D = 12$ directed spatial coupling components, plus 1 for non-degeneracy. Total: $12 + 1 = 13$. This is the spatial structure: the number of directed spatial coupling modes.

$f = 21$ in TetA ($s = +1$): all channels are active. The 16 components of the bimetric interaction, plus 4 from propagation through the $(3+1)$ face channels, plus 1 for existence. Total: $16 + 4 + 1 = 21$. This is the full coupling depth: the complete hierarchy from existence through propagation to interaction.

Every integer in the gravitational constant traces to a named quantity in published bimetric gravity. The 16 is the frame transition matrix component count (Hassan and Rosen, 2012). The 17 is the Hamiltonian interaction space dimension (Hassan and Kocic, 2018). The 28 phase-locking channels come from the constraint algebra. The framework does not invent new mathematics. It reads existing mathematics through the lens of the stellated octahedron.

**Empirical verification of $K^2 = 16$.**

The coupling polynomial's interaction term $K^2 = 16$ predicts that the MOND acceleration scale $a_0$ and the gravitational coupling at the electron scale should be related by a factor of exactly 16. Specifically, the ratio $a_0 / (G m_e / r_e^2)$ should equal $K^2$.

Direct calculation using CODATA 2022 values gives:

$$\frac{a_0}{G m_e / r_e^2} = \frac{1.22 \times 10^{-10}}{7.66 \times 10^{-12}} = 15.93$$

This agrees with the topological requirement of 16 to within 0.4\%. The interaction term is not a numerical coincidence. It is the channel count of the bimetric interaction, verified empirically.

**Summary of Derivation 3.**

The coupling polynomial $f(K) = 1 + K + K^2$ is already written into the Hassan-Rosen bimetric Hamiltonian. The elementary symmetric polynomials $e_0$, $e_1$, $e_2$ contain 1, $K$, and $K^2$ components respectively, mirroring the three terms of the polynomial exactly. The coupled face matrix of the stellated octahedron is identically the frame transition matrix of bimetric gravity, as established by the Barbieri closure constraint and the ADM decomposition. Every structural integer in the framework corresponds to a named, published quantity in the bimetric literature. The polynomial was not imported into gravity from outside. It was already there.

---

### Three Paths, One Polynomial

The three derivations arrive at $f(K, s) = 1 + sK + K^2$ with $K = 4$ from entirely independent starting points.

The geometric derivation (Derivation 1) shows that the polynomial is forced by the combinatorial anatomy of the tetrahedron. The self-duality visible in Pascal's row $K = 4$ collapses vertex and face counts into a single propagation term, producing a trinomial. The closure condition $K^2 = 2^K$ locks the interaction term to the Pascal row sum. No other simplex admits this structure.

The observational derivation (Derivation 2) shows that the polynomial is forced by three physical measurements and theorems. LIGO polarizations determine $K = 4$. The simplex theorem determines $K = D + 1 = 4$. Ghost-free bimetric coupling requires a dual tetrahedral structure with a shared origin. Together these fix the polynomial uniquely, with no room for additional or missing terms.

The algebraic derivation (Derivation 3) shows that the polynomial is already present in the standard formalism of bimetric gravity. The elementary symmetric polynomials of the frame transition matrix mirror the three terms. The coupled face matrix of the stellated octahedron is the frame transition matrix. The three structural integers correspond to named quantities in the published Hamiltonian.

These are not three ways of saying the same thing. The first is a theorem about simplicial geometry. The second is a constraint from gravitational wave observations and mathematical physics. The third is a reading of an existing formalism. Their convergence on a single polynomial is the strongest form of the argument: the coupling polynomial is not merely consistent with the geometry, the observations, and the algebra. It is the unique object that satisfies all three simultaneously.

From this polynomial, the next page derives the field equation: the continuous function $f(x) = (21x + 13)/(x + 1)$ that extends the three structural states to every possible acceleration. From the field equation, the constitutive law, the scalar-tensor transition, the gravitational constant, and all observable predictions follow. The polynomial is where the derivation chain begins. Everything else is reading.
