# The Coupling Polynomial

## Why We Need It

The Foundations section built the stellated octahedron, two tetrahedral field chambers, eight faces, twelve edges, eight vertices, twenty-eight geometric elements, coupled at the Field Origin. You know what the geometry looks like. You know its symmetries, its face structure, its spin. But knowing the shape of a crystal does not tell you how strongly it scatters light. Knowing the geometry of the gravitational field does not yet tell you how strongly it couples. (Einstein, 1915; Hassan and Rosen, 2012; Milgrom, 1983)

The missing piece is depth. When two field regions interact through the stellated octahedron, how many levels does the coupling traverse? Not just that two tetrahedra touch, but how many distinct ways they connect, counted from the inside out. The answer to this question is a single polynomial, and every prediction in the Gravitation section flows from it. (Einstein, 1915; Hassan and Rosen, 2012; Milgrom, 1983)

## Building the Polynomial

Think about what must happen for the gravitational field to couple across a single stellated octahedron, starting from the center and working outward. (Einstein, 1915; Hassan and Rosen, 2012; Milgrom, 1983)

At the center is the Field Origin, the single point where both chambers meet, where the two metrics are evaluated at the same spacetime event. This is the foundation. Without it, there is no coupling at all. The field either closes here, $\det(g) \neq 0$, or spacetime has failed. This contributes one level: **1**. (Einstein, 1915; Hassan and Rosen, 2012; Milgrom, 1983)

From the Field Origin, the field extends outward through the faces of one tetrahedron. Each tetrahedron has $K = 4$ faces, and each face subdivides into $3 + 1 = 4$ sub regions, three spatial and one gravitational, when the dual chamber penetrates it. The field reaches through these face channels. This contributes a second level: **K = 4**. (Einstein, 1915; Hassan and Rosen, 2012; Milgrom, 1983)

Finally, both chambers interact fully. Each has $K = 4$ face directions. The complete coupling between them is a $K \times K$ matrix, every face of TetA paired with every face of TetB. This is the frame transition matrix of bimetric gravity, and it has $K^2 = 16$ independent components. This contributes a third level: **K^2 = 16**. (Einstein, 1915; Hassan and Rosen, 2012; Milgrom, 1983)

The total coupling depth is:

**f(K) = 1 + K + K^2 = 1 + 4 + 16 = 21**

This is the coupling polynomial. It counts how many levels the gravitational field must traverse to achieve complete coupling between the two sectors. The number 21 is not chosen. It is the geometric series (Einstein, 1915; Hassan and Rosen, 2012; Milgrom, 1983)

$$
1 + K + K^2 = \frac{K^3 - 1}{K - 1} = \frac{64 - 1}{3} = 21,
$$

which is the standard simplex boundary sum in $D = 3$ dimensions.

## Why Exactly Three Terms

The polynomial has three terms because the stellated octahedron boundary has three types of geometric cell. Vertices are zero dimensional points. Edges are one dimensional lines. Faces are two dimensional triangles. There is no three dimensional cell on the boundary of a tetrahedron. The interior is the volume the boundary encloses, not a boundary element itself. The polynomial mirrors this: $K^0 = 1$ (point), $K^1 = 4$ (edges and faces), $K^2 = 16$ (face to face pairings). A $K^3$ term would require a three dimensional coupling cell on a two dimensional boundary. It does not exist. (Einstein, 1915; Hassan and Rosen, 2012; Milgrom, 1983)

Each coefficient is exactly 1. One Field Origin, not two. One connection per face, not a weighted sum. One matrix entry per pair of frame directions. The polynomial is a geometric series with ratio $K$ and $D = 3$ terms, and geometric series have unit coefficients by definition. Departing from unity would break the simplex identity (Einstein, 1915; Hassan and Rosen, 2012; Milgrom, 1983)

$$
f(K) = \frac{K^D - 1}{K - 1},
$$

and the connection to the dimension of space would be lost. There is nothing to adjust. (Einstein, 1915; Hassan and Rosen, 2012; Milgrom, 1983)

## The Three Structural States

The coupling polynomial describes full depth when all channels are active. But the stellated octahedron has three distinct structural regions, TetA, the Field Origin, and TetB, and not all channels are active everywhere. (Einstein, 1915; Hassan and Rosen, 2012; Milgrom, 1983)

The key is the middle term. The Field Origin (1) exists in all three regions. It is the precondition for coupling anywhere. The bimetric interaction ($K^2$) is symmetric: if TetA couples to TetB, then TetB couples to TetA. Neither the point nor the pairing depends on which sector you stand in. But the face channels ($K$) have direction. They represent propagation through one sector faces, and propagation requires spatial extent. At the Field Origin, where $r = 0$, there is no spatial extent. In TetB, the orientation is reversed. (Einstein, 1915; Hassan and Rosen, 2012; Milgrom, 1983)

This gives the polynomial a state parameter $s$ that modifies only the middle term:

**f(K, s) = 1 + sK + K^2**

Evaluated in each structural region:

| Region | State s | Polynomial | Value |
|---|---|---|---|
| TetA (our sector) | s = +1 | 1 + 4 + 16 | **21** |
| Field Origin (coupling boundary) | s = 0 | 1 + 0 + 16 | **17** |
| TetB (dual sector) | s = -1 | 1 - 4 + 16 | **13** |

Three regions, three integers: 21, 17, 13. These are the three numbers that appear in the gravitational constant $G$. They are not fitted to data. They are the coupling polynomial evaluated in the three structural regions of the stellated octahedron. (Einstein, 1915; Hassan and Rosen, 2012; Milgrom, 1983)

## The Arithmetic Mean Lock

The three structural values are not independent. They are locked by an algebraic identity:

$$
\frac{21 + 13}{2} = \frac{34}{2} = 17
$$

The Field Origin value is exactly the arithmetic mean of the TetA and TetB values. This is not a numerical coincidence. It holds for any polynomial of the form $1 + sK + K^2$. The three values are equally spaced: $21 - 17 = 17 - 13 = K = 4$. They are as rigidly constrained as three equally spaced marks on a ruler. Move one, and you break all three. (Einstein, 1915; Hassan and Rosen, 2012; Milgrom, 1983)

This lock means the framework has no room to adjust its integers. If any of the three values were off by even one unit, the arithmetic mean identity would fail, the polynomial would no longer be a geometric series, and the connection to the dimension of space would be severed. The topology either works completely or it fails completely. There are no dials. (Einstein, 1915; Hassan and Rosen, 2012; Milgrom, 1983)

## What Each Integer Means

Each integer has a physical interpretation that recurs throughout the Gravitation section:

**21** is full coupling depth, the total number of levels the gravitational field attenuates through. It becomes the exponent in $G$, because coupling weakens by fine structure constant $\alpha$ at each level: $G$ contains $\alpha^{21}$. (Einstein, 1915; Hassan and Rosen, 2012; Milgrom, 1983)

**17** is coupling capacity at the Field Origin, the $K^2 = 16$ components of the frame transition matrix plus 1 for the existence condition. It becomes the numerator of topological prefactor $17/13$ in $G$. (Einstein, 1915; Hassan and Rosen, 2012; Milgrom, 1983)

**13** is spatial structure of the inverted sector, the $K \times D = 12$ directed spatial coupling components plus 1 for nondegeneracy. It becomes the denominator. (Einstein, 1915; Hassan and Rosen, 2012; Milgrom, 1983)

The ratio $17/13$ compares coupling capacity to spatial structure. The exponent 21 measures depth. Together they give (Einstein, 1915; Hassan and Rosen, 2012; Milgrom, 1983)

$$
G = \left(\frac{17}{13}\right)\alpha^{21}\frac{\hbar c}{m_e^2},
$$

a formula in which every number is a reading of the stellated octahedron. (Einstein, 1915; Hassan and Rosen, 2012; Milgrom, 1983)

## What You Now Have

One polynomial. Three structural states. Three integers. From here, the next pages derive the gravitational constant, the constitutive law, the covariant action, and resulting predictions, all from $f(K, s) = 1 + sK + K^2$ and two integers $K = 4$, $D = 3$. The geometry was built in Foundations. The polynomial reads it. Everything that follows is reading. (Einstein, 1915; Hassan and Rosen, 2012; Milgrom, 1983)

## References

Einstein, A. (1915). "Die Feldgleichungen der Gravitation," Sitzungsber. Preuss. Akad. Wiss. 844.

Bekenstein, J. D. and Milgrom, M. (1984). "Does the missing mass problem signal the breakdown of Newtonian gravity?," Astrophys. J. 286, 7.

Milgrom, M. (1983). "A modification of the Newtonian dynamics as a possible alternative to the hidden mass hypothesis," Astrophys. J. 270, 365.

Hassan, S. F. and Rosen, R. A. (2012). "Bimetric gravity from ghost free massive gravity," J. High Energy Phys. 02, 126.

Will, C. M. (2014). "The Confrontation between General Relativity and Experiment," Living Rev. Relativ. 17, 4.

Abbott, B. P. et al. (2017). "GW170817: Observation of Gravitational Waves from a Binary Neutron Star Inspiral," Phys. Rev. Lett. 119, 161101.
