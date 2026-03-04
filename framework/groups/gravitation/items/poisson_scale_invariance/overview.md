# Poisson Equation and Scale Invariance

## The Scale Problem

A star contains roughly $10^{57}$ atoms. Each atom has its own electron field envelope satisfying field closure. The star as a whole also satisfies field closure. So does the galaxy that contains the star. So does the cluster that contains the galaxy.
If field closure operates at every one of these scales, and it must, because $\det(g) \neq 0$ is a local condition that must hold at every point in spacetime, then the field equation governing gravity must be the same equation at every scale. Not approximately the same. Exactly the same. The equation for gravitational field of an electron (at $10^{-13}\ \mathrm{m}$) must be identical in form to the equation for a galaxy (at $10^{21}\ \mathrm{m}$). This is a span of thirty four orders of magnitude. Why should the same equation hold?
The answer is that every factor in gravitational field equation comes from topological integers, and topological integers do not change with scale. A tetrahedron has four faces whether it is the size of a proton or the size of a galaxy cluster. The number $K=4$ is immune to renormalization. No scale transformation can change the number of faces on a simplex.
## Where 4pi Comes From

The standard Poisson equation of Newtonian gravity is

$$
\nabla^2 \Phi = 4\pi G\rho.
$$

Every physicist knows the $4\pi$. But where does it come from?

The textbook answer is surface area of a sphere: $A = 4\pi r^2$. You integrate gravitational field over a closed surface, apply Gauss law, and $r^2$ in surface area cancels $1/r^2$ decay of field strength, leaving $4\pi GM$ for enclosed mass. This derivation is mathematically correct. But it conceals a puzzle: factor $4\pi$ appears to come from a geometric quantity that depends on radius $r$, yet final equation is universal across all scales. How does a scale dependent quantity produce a scale independent result?
Gravitational Field Dynamics resolves this. The factor $4\pi$ is not fundamentally about surface area. It is about tetrahedral closure.
Field closure requires $K=4$ tetrad basis vectors spanning tangent space completely at every point. These four basis vectors define a tetrahedral ball, a spherical simplex, at each vertex of the field. The boundary of this simplex is a 2 sphere with total solid angle $4\pi$ steradians. A regular tetrahedron inscribed in a sphere divides this total solid angle into four equal parts of $\pi$ steradians each:

$$
4\pi = K \times \pi
$$

This is the same $4\pi$. But derivation is fundamentally different. Standard route goes through surface area (which contains $r$). Topological route goes through simplex number $K=4$ (which contains no scale at all). The factor $4\pi$ is intrinsic to topology of field closure itself. It is number of coupling faces times solid angle per face. No radius appears. Scale invariance is manifest.
## The Complete Poisson Equation

The G from Topology page showed that gravitational constant carries topological prefactor $17/13$. Poisson equation inherits this structure. Combining field normalization $K\pi$ with coupling ratio from polynomial:

$$
\nabla^2 \Phi = K\pi \times \frac{K^2 + 1}{KD + 1} \times G_{\mathrm{bare}} \times \rho$$

Substituting $K=4$ and $D=3$:

$$
\nabla^2 \Phi = 4\pi \times \left(\frac{17}{13}\right) \times G_{\mathrm{bare}} \times \rho$$

Every factor is determined by topological integers. Normalization $4\pi = K\pi$ counts solid angle per coupling face. Ratio $17/13$ compares coupling capacity ($K^2+1$ at Field Origin) to spatial structure ($KD+1$ in observed sector). Bare gravitational constant $G_{\mathrm{bare}}$ carries coupling depth $\alpha^{21}$. None of these depend on radius, mass, or characteristic scale of system. They are structural constants of stellated octahedron.
This is why Poisson equation governs gravitational fields from quantum regime to cosmic regime without modification. The equation is not universal because of an unknown deep principle. It is universal because every number in it is a topological integer, and topological integers do not care what scale you work at. An atom establishes field closure at valence radius. A star establishes field closure at stellar radius. A galaxy establishes field closure at virial radius. At every level, constraint is the same: $K=4$ faces, $D=3$ dimensions, and coupling polynomial $f(K,s)=1+sK+K^2$.
## The Constitutive Law

The Poisson equation above is strong field version. It applies in Newtonian regime where accelerations are large compared to characteristic scale $a_0$. But galaxies rotate in regime where accelerations drop below $a_0$. There, linear Poisson equation fails. Rotation curves remain flat where Newton predicts decline. Standard resolution invokes dark matter. Alternative is to recognize that field equation needs a constitutive law.
A constitutive law governs how a medium responds to a driving force. Ohm law relates current to voltage in a wire. Hooke law relates displacement to force in a spring. In each case, law describes material response, not the force itself. Gravitational constitutive law describes how gravitational field responds to demand placed on it by mass.
In Gravitational Field Dynamics, constitutive law is not chosen by curve fitting. It is derived from field closure. The argument proceeds in three steps.
First, field closure must be lossless, no wakes, no drag, no hysteresis. We observe none of these. Objects move through gravitational fields cleanly. This forces closure process to satisfy detailed balance: rate of resolving new demand equals rate of relaxing resolved states at equilibrium.
Second, field closure must be local, no faster than light coordination. Field couples through its $K=4$ faces at each point, processing only immediate neighborhood.
Third, field has finite capacity. With $K=4$ coupling channels, there is a maximum rate at which field can process gravitational demand. Below acceleration $a_0$, this capacity saturates, not all at once, but one channel at a time, because each channel operates independently.
These three constraints, lossless, local, finite capacity with single channel saturation, yield a unique constitutive law through detailed balance:

$$
\mu(x) = \frac{x}{x+1}
$$

where $x = |\nabla \Phi|/a_0$ is local gravitational acceleration measured in units of characteristic scale. At high accelerations ($x \gg 1$), $\mu \rightarrow 1$ and Newton is recovered. At low accelerations ($x \ll 1$), $\mu \rightarrow x$ and deep field regime produces flat rotation curves without dark matter. At $x=1$, $\mu=1/2$, the Field Origin, where both chambers contribute equally.
This is function that Milgrom discovered empirically in 1983 by fitting galactic rotation curves. For forty years, it has been a free function, chosen from data, not derived from principle. (Milgrom, 1983) Gravitational Field Dynamics derives it as unique equilibrium solution within minimal closure class. The "simple" interpolating function $\mu(x)=x/(x+1)$ is not one option among many. It is only function consistent with lossless, local, single channel closure.
## The Modified Poisson Equation

The complete field equation, valid at all acceleration scales, is AQUAL form with derived constitutive law:

$$
\nabla \cdot [\mu(x)\nabla \Phi] = 4\pi G\rho
$$

This single equation contains all Newtonian gravity (in strong field limit) and all galactic dynamics (in weak field limit). It is not two theories glued together. It is one field equation with one constitutive law, both derived from same topology. Transition between Newton and deep field regime is not a boundary between two theories. It is constitutive response of gravitational field as coupling channels approach saturation.
Scale invariance is preserved because $\mu(x)$ depends only on ratio $x = |\nabla \Phi|/a_0$, and $a_0$ itself is derived from topology through Hubble horizon connection. No factor in equation depends on absolute scale of system. Equation works for atoms, stars, galaxies, and clusters, not because tuned separately at each scale, but because every number in it is a topological constant of stellated octahedron.

## References

Milgrom, M. (1983). A modification of the Newtonian dynamics as a possible alternative to the hidden mass hypothesis. Astrophys. J. 270, 365.
