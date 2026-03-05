# The Coupling Polynomial

## Why We Need It

The Foundations section built the stellated octahedron, two tetrahedral field chambers, eight faces, twelve edges, eight vertices, twenty-eight geometric elements, coupled at the Field Origin. You know what the geometry looks like. You know its symmetries, its face structure, its spin. But knowing the shape of a crystal does not tell you how strongly it scatters light. Knowing the geometry of the gravitational field does not yet tell you how strongly it couples.
The missing piece is depth. When two field regions interact through the stellated octahedron, how many levels does the coupling traverse? Not just that two tetrahedra touch, but how many distinct ways they connect, counted from the inside out. The answer to this question is a single polynomial, and every prediction in the Gravitation section flows from it.
## Building the Polynomial

Think about what must happen for the gravitational field to couple across a single stellated octahedron, starting from the center and working outward.
At the center is the Field Origin, the single point where both chambers meet, where the two metrics are evaluated at the same spacetime event. This is the foundation. Without it, there is no coupling at all. The field either closes here, $\det(g) \neq 0$, or spacetime has failed. This contributes one level: **1**.
From the Field Origin, the field extends outward through the faces of one tetrahedron. Each tetrahedron has $K = 4$ faces, and each face subdivides into $3 + 1 = 4$ sub regions, three spatial and one gravitational, when the dual chamber penetrates it. The field reaches through these face channels. This contributes a second level: **K = 4**.
Finally, both chambers interact fully. Each has $K = 4$ face directions. The complete coupling between them is a $K \times K$ matrix, every face of TetA paired with every face of TetB. This is the frame transition matrix of bimetric gravity, and it has $K^2 = 16$ independent components. This contributes a third level: **K^2 = 16**.
The total coupling depth is:

**f(K) = 1 + K + K^2 = 1 + 4 + 16 = 21**

This is the coupling polynomial. It counts how many levels the gravitational field must traverse to achieve complete coupling between the two sectors. The number 21 is not chosen. It is the geometric series
$$
1 + K + K^2 = \frac{K^3 - 1}{K - 1} = \frac{64 - 1}{3} = 21,
$$

which is the standard simplex boundary sum in $D = 3$ dimensions.

## Why Exactly Three Terms

The polynomial has three terms because the stellated octahedron boundary has three types of geometric cell. Vertices are zero dimensional points. Edges are one dimensional lines. Faces are two dimensional triangles. There is no three dimensional cell on the boundary of a tetrahedron. The interior is the volume the boundary encloses, not a boundary element itself. The polynomial mirrors this: $K^0 = 1$ (point), $K^1 = 4$ (edges and faces), $K^2 = 16$ (face to face pairings). A $K^3$ term would require a three dimensional coupling cell on a two dimensional boundary. It does not exist.
Each coefficient is exactly 1. One Field Origin, not two. One connection per face, not a weighted sum. One matrix entry per pair of frame directions. The polynomial is a geometric series with ratio $K$ and $D = 3$ terms, and geometric series have unit coefficients by definition. Departing from unity would break the simplex identity
$$
f(K) = \frac{K^D - 1}{K - 1},
$$

and the connection to the dimension of space would be lost. There is nothing to adjust.
## The Three Structural States

The coupling polynomial describes full depth when all channels are active. But the stellated octahedron has three distinct structural regions, TetA, the Field Origin, and TetB, and not all channels are active everywhere.
The key is the middle term. The Field Origin (1) exists in all three regions. It is the precondition for coupling anywhere. The bimetric interaction ($K^2$) is symmetric: if TetA couples to TetB, then TetB couples to TetA. Neither the point nor the pairing depends on which sector you stand in. But the face channels ($K$) have direction. They represent propagation through one sector faces, and propagation requires spatial extent. At the Field Origin, where $r = 0$, there is no spatial extent. In TetB, the orientation is reversed.
This gives the polynomial a state parameter $s$ that modifies only the middle term:

**f(K, s) = 1 + sK + K^2**

Evaluated in each structural region:

| Region | State s | Polynomial | Value |
|---|---|---|---|
| TetA (our sector) | s = +1 | 1 + 4 + 16 | **21** |
| Field Origin (coupling boundary) | s = 0 | 1 + 0 + 16 | **17** |
| TetB (dual sector) | s = -1 | 1 - 4 + 16 | **13** |

Three regions, three integers: 21, 17, 13. These are the three numbers that appear in the gravitational constant $G$. They are not fitted to data. They are the coupling polynomial evaluated in the three structural regions of the stellated octahedron.
## The Arithmetic Mean Lock

The three structural values are not independent. They are locked by an algebraic identity:

$$
\frac{21 + 13}{2} = \frac{34}{2} = 17
$$

The Field Origin value is exactly the arithmetic mean of the TetA and TetB values. This is not a numerical coincidence. It holds for any polynomial of the form $1 + sK + K^2$. The three values are equally spaced: $21 - 17 = 17 - 13 = K = 4$. They are as rigidly constrained as three equally spaced marks on a ruler. Move one, and you break all three.
This lock means the framework has no room to adjust its integers. If any of the three values were off by even one unit, the arithmetic mean identity would fail, the polynomial would no longer be a geometric series, and the connection to the dimension of space would be severed. The topology either works completely or it fails completely. There are no dials.
## What Each Integer Means

Each integer has a physical interpretation that recurs throughout the Gravitation section:

**21** is full coupling depth, the total number of levels the gravitational field attenuates through. It becomes the exponent in $G$, because coupling weakens by fine structure constant $\alpha$ at each level: $G$ contains $\alpha^{21}$.
**17** is coupling capacity at the Field Origin, the $K^2 = 16$ components of the frame transition matrix plus 1 for the existence condition. It becomes the numerator of topological prefactor $17/13$ in $G$.
**13** is spatial structure of the inverted sector, the $K \times D = 12$ directed spatial coupling components plus 1 for nondegeneracy. It becomes the denominator.
The ratio $17/13$ compares coupling capacity to spatial structure. The exponent 21 measures depth. Together they give
$$
G = \left(\frac{17}{13}\right)\alpha^{21}\frac{\hbar c}{m_e^2},
$$

a formula in which every number is a reading of the stellated octahedron.
## The Polynomial Was Already Written Down

There is an equation that every student of general relativity learns in their first year of graduate school. It is not controversial. It is not speculative. It appears in every textbook on tetrad gravity, from Misner, Thorne and Wheeler (1973) to Carroll (2004) to Rovelli (2004). The equation is:

$$
g_{\mu\nu} = \eta_{ab} \, e^a_\mu \, e^b_\nu
$$

It says: the metric of spacetime is built from three ingredients. A flat reference metric $\eta_{ab}$, which encodes how directions couple. A tetrad field $e^a_\mu$, which provides the local frame, the four legs that span the tangent space at each point. And a non-degeneracy condition, $\det(e) \neq 0$, which guarantees that the tetrad actually spans. Without it, the metric is singular. Spacetime fails.

For a century, this equation has been treated as a definition. A way to rewrite the metric in terms of tetrads. A change of variables. You learn it, you use it, you move on.

But look at what the equation contains.

**The non-degeneracy condition.** One constraint: $\det(e) \neq 0$. The field either closes or it does not. This is binary. It contributes one structural element.

That is $k^0 = 1$.

**The tetrad.** Four legs: $e^a_\mu$ where $a$ runs from 0 to 3. One leg for time, three for space. Four independent directions that span the tangent space. This is the frame, the structure that tells you which directions exist at each point.

That is $k^1 = K = 4$.

**The flat metric.** $\eta_{ab}$ carries two indices, each running from 0 to 3. It is a $K \times K$ matrix, 16 components that encode how every direction couples to every other direction. In flat spacetime, most of these are zero (the off-diagonal entries vanish). In curved spacetime, the full metric $g_{\mu\nu}$ fills all 16 slots. The flat metric is the template; the connection structure has $K^2 = 16$ slots available.

That is $k^2 = K^2 = 16$.

Now count the structural types. Not the components, every relativist counts components. Count the *types of structure* present in the equation:

$$
1 + K + K^2 = 1 + 4 + 16 = 21
$$

That is the coupling polynomial.

The tetrad equation of general relativity, written down by Einstein in 1928 and used by every gravitational physicist since, contains exactly three structural types: a constraint, a frame, and a connection. Their count is $1 + K + K^2$. The coupling polynomial is not imported into gravity from outside. It is the structural content of the equation that *defines* the gravitational field in the tetrad formalism.

No one noticed because no one was counting types. The standard question is: how many independent components does $g_{\mu\nu}$ have? The answer is 10 (a symmetric $4 \times 4$ matrix). That is the right answer to that question. But it is the answer to a different question than the one the coupling polynomial asks.

The polynomial asks: how many *levels of structure* does the gravitational field traverse to achieve complete coupling? One level for existence. One level for the frame. One level for the connection. Three levels, with $1$, $K$, and $K^2$ elements respectively. The total depth is 21.

This is why the polynomial has exactly three terms. The boundary of a tetrahedron has three types of geometric cell: vertices (zero-dimensional, $k^0$), edges (one-dimensional, $k^1$), and faces (two-dimensional, $k^2$). There is no three-dimensional cell on the boundary of a three-dimensional object. The tetrad equation has three types of structure for the same reason the tetrahedron has three types of boundary element. Both are descriptions of closure in $D = 3$ spatial dimensions.

The polynomial was always there. It was written in 1928 as $g_{\mu\nu} = \eta_{ab} \, e^a_\mu \, e^b_\nu$. It took a century to read it as $1 + K + K^2$.

## What You Now Have

One polynomial. Three structural states. Three integers. From here, the next pages derive the gravitational constant, the constitutive law, the covariant action, and resulting predictions, all from $f(K, s) = 1 + sK + K^2$ and two integers $K = 4$, $D = 3$. The geometry was built in Foundations. The polynomial reads it. Everything that follows is reading.
