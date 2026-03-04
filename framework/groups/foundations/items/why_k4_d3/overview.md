# Why k = 4 and d = 3

We live in three dimensions of space and one of time. This is so familiar that it barely registers as a fact. We reach forward, sideways, and up, three independent directions, and we move through time. Every human experience, every physical measurement, every experiment ever conducted takes place in this 3+1 dimensional arena.
But why three? Physics does not answer this question by default. General relativity works in any number of dimensions. String theory proposes ten or eleven. The equations do not care. Three spatial dimensions are treated as an observation, something we measure and accept, like the charge of the electron or the speed of light.
The previous page established that the gravitational field must close: it must form a complete enclosure at every point, with no missing directions and no open faces. Two questions follow immediately. How many faces does closure require? And is three the only number of spatial dimensions where the field topology is self consistent?
The answer to the first comes from classical geometry. The answer to the second comes from a single equation in combinatorics. Together, they lock in the two structural constants of the entire framework, and they show that three is not arbitrary. It is the unique number of spatial dimensions in which the gravitational field can close into a self consistent topology. The proof requires one equation, and the geometry that results determines everything that follows.
## The Simplex Theorem

In one dimension, two points bracket an interval. In two dimensions, three points form a triangle enclosing area. In three dimensions, four points, provided they are not all in the same plane, form a tetrahedron enclosing volume. You cannot do better. Three points in three dimensional space define a flat triangle with no interior volume. It takes four to fence off a region.

This is the simplex theorem: in $d$ spatial dimensions, the minimum number of boundary faces required to enclose a region is $d + 1$. For our three dimensional space, that gives $3 + 1 = 4$. This number is written as $k = 4$. It is not chosen. It is not fitted to data. It is the geometric minimum for enclosure in three dimensions.

The remarkable fact is that this same number appears independently across every major formalism in gravitational physics, derived by different research groups, in different decades, for different purposes.

## The Formalisms

| Formalism | What $k = 4$ represents | Source |
|---|---|---|
| ADM formalism | 4 constraint equations (1 energy + 3 momentum) | Arnowitt, Deser, Misner (1962) |
| Tetrad gravity | 4 orthonormal basis vectors spanning tangent space | Einstein (1928), Cartan, MTW |
| Loop Quantum Gravity | 4 faces of the quantum tetrahedron | Rovelli and Vidotto (2014) |
| Regge calculus | 4 vertices of the 3 simplex | Regge (1961) |
| LIGO observation | $2$ polarisations = $10 - 2k$ constraints - $k$ gauge | Abbott et al. (2017) |

Five independent lines of physics. One number. The simplex theorem explains why: four is the minimum for three dimensional enclosure, and every formalism that describes gravity in three spatial dimensions inherits this minimum.

## The Uniqueness Equation

Four faces require three spatial dimensions. But why three? Could the universe have had two spatial dimensions, or five, or eleven?
There is an equation that answers this. It asks: in how many dimensions can two simplices exactly partition the vertices of a hypercube? A simplex in $d$ dimensions has $d + 1$ vertices, so two simplices have $2(d + 1)$ vertices. A hypercube in $d$ dimensions has $2^d$ vertices. The equation is:

$$

2(d + 1) = 2^d

$$

Check it dimension by dimension. At $d = 1$: the left side gives $4$, the right side gives $2$. No match. At $d = 2$: left gives $6$, right gives $4$. No match. At $d = 3$: left gives $8$, right gives $8$. Match. At $d = 4$: left gives $10$, right gives $16$. No match. At $d = 5$: left gives $12$, right gives $32$. The gap only widens.
The left side grows linearly. The right side grows exponentially. They meet exactly once, at $d = 3$, and never again. This is not a near miss or an approximation. It is an exact integer equation with a unique positive solution.
This single equation fixes both structural constants simultaneously. $D = 3$ gives the spatial dimensions. $K = D + 1 = 4$ gives the closure constant. From these two integers, the entire framework follows: the stellated octahedron from binary vertex encoding, the coupling polynomial from face geometry, the constitutive law from capacity normalisation, the complete gravitational action from topological counting. Zero free parameters enter at any step.
## What the Equation Means

The equation $2(d + 1) = 2^d$ is asking something precise: in which dimensions does the discrete geometry of the simplex fit exactly inside the discrete geometry of the hypercube? In three dimensions, two tetrahedra have exactly eight vertices, and a cube has exactly eight vertices. The two tetrahedra partition the cube perfectly, with no vertices left over and none missing. This is the binary parity partition: the eight cube vertices split into two groups of four by counting active bits (odd popcount versus even popcount), and each group forms a regular tetrahedron. The two tetrahedra interlock to form the stellated octahedron.

In any other number of dimensions, the partition fails. There are too few cube vertices or too many simplex vertices. The geometry does not close. Only in three dimensions does everything fit, and the structure that results, the stellated octahedron, is the subject of the next page.
