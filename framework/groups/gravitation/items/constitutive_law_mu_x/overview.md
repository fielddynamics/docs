# Constitutive Law μ(x)

## Overview

Every material has a constitutive law. It is the equation that tells you how the material responds when you push on it.
Stretch a spring, and Hooke law tells you the restoring force is proportional to the displacement. Push current through a wire, and Ohm law tells you the voltage is proportional to the current. Heat one end of a metal rod, and Fourier law tells you how fast the heat flows to the other end. In each case, the constitutive law is not the force itself. It is the material response to the force. It encodes the internal structure of the medium, the stiffness of the spring, the resistivity of the wire, and the conductivity of the metal.
The gravitational field is a medium. It carries waves. It has structure. It must have a constitutive law.
That law is:

$$
\mu(x) = \frac{x}{x + 1}
$$

where $x = g/a_0$ is the local gravitational acceleration measured in units of the characteristic scale. This single equation governs how the gravitational field responds to mass at every scale in the universe, from the interior of atoms to the edges of galaxy clusters. It is not chosen from a menu of options. It is not fitted to rotation curves. It is derived from the topology of the stellated octahedron, and every number in it traces back to the two integers $K = 4$ and $D = 3$.
This page explains where it comes from, what it means, and why it is the same equation as the Poisson equation you already know.
## What the Constitutive Law Does

Point a telescope at a spiral galaxy and measure how fast the stars orbit at different distances from the center. Close to the center, where the gravitational field is strong, everything behaves exactly as Newton predicted. The orbital velocity rises, peaks, and should then decline as you move outward, because the mass is concentrated in the center and gravity weakens with distance.
It does not decline. The rotation curve stays flat, all the way out to the farthest measurable stars and gas clouds. The velocity at 50,000 light years from the galactic center is roughly the same as the velocity at 15,000 light years. Newton equation, applied honestly, says this is impossible unless there is far more mass present than we can see.
The standard response is dark matter: an invisible substance, five times more abundant than ordinary matter, arranged in a halo around every galaxy, fine tuned to produce exactly the flat rotation curve we observe. It has never been directly detected.
The constitutive law offers a different explanation. It says the gravitational field has two chambers, TetA and TetB, coupled at the Field Origin. At high accelerations, TetA does all the work and gravity looks Newtonian. At low accelerations, TetB picks up the slack, contributing additional gravitational effect that keeps rotation curves flat. The constitutive law μ(x) governs the handoff between them.
When x is much larger than 1, strong field, well above the characteristic scale $a_0$, the constitutive law gives $\mu \approx 1$. All coupling channels are active. Newton inverse square law holds. This is the regime of the solar system, of laboratory experiments, and of everything humans directly experience.
When x is much smaller than 1, weak field, well below $a_0$, the constitutive law gives $\mu \approx x$. The Newtonian contribution from visible matter accounts for only a fraction of the total gravitational effect. TetB, the dual chamber, provides the rest. This is the regime of the outer edges of galaxies, where rotation curves flatten and the need for dark matter was first inferred.
At $x = 1$, exactly at $a_0$, the constitutive law gives $\mu(1) = 1/2$. This is the Field Origin, the geometric center of the stellated octahedron where the two chambers meet face to face and contribute equally. Half the gravitational effect comes from TetA, half from TetB. The transition is not gradual or approximate. It is the midpoint of the topology.
## Where It Comes From: Three Terms of One Polynomial

The Coupling Polynomial page derived f(K, s) = 1 + sK + K^2, the polynomial that counts how deeply the gravitational field couples at each structural level of the stellated octahedron. Evaluated at K = 4, it gives three structural values: f(+1) = 21 in TetA, f(0) = 17 at the Field Origin, and f(-1) = 13 in TetB.
The constitutive law is what happens when you let this polynomial vary continuously.
Instead of evaluating f at three fixed states, allow the state parameter s to change smoothly with the local acceleration. The Möbius map
$$
s(x) = \frac{x - 1}{x + 1}
$$

does exactly this. It maps the acceleration ratio $x \in [0,\infty)$ onto the state parameter $s \in [-1,+1)$, with $s = 0$ at $x = 1$, the Field Origin. This map is not chosen. It is the unique Möbius transformation satisfying three closure constraints: s must equal -1 at zero acceleration (TetB endpoint), +1 at infinite acceleration (TetA endpoint), and 0 at the transition (Field Origin). Three constraints fix three parameters. The map is determined.
Composing the polynomial with this map gives the capacity function:

$$
f(x) = \frac{21x + 13}{x + 1}
$$

This is f(K, s) evaluated continuously across all accelerations. It ranges from 13 (deep field, TetB dominant) to 21 (strong field, TetA dominant), passing through 17 at x = 1.
The constitutive law is the normalization of this capacity to the unit interval:

$$
\mu(x) = \frac{f(x) - 13}{8} = \frac{x}{x + 1}
$$

The denominator 8 = 2K = 2^D is the total range of the polynomial. The result is a number between 0 and 1 that measures what fraction of the stellated octahedron total coupling capacity is active at a given acceleration. At the Field Origin, half the capacity is used. In the Newtonian regime, nearly all of it. In the deep field regime, almost none.
This is what μ(x) is. It is the normalized capacity of the coupling polynomial, evaluated continuously across all gravitational states.
## The Three Terms and What Each One Does

The polynomial f(k, s) = 1 + sk + k^2 has three terms. Each has a distinct geometric identity in the stellated octahedron and a distinct role in producing the constitutive law.
**The k^2 = 16 term sets the range.** This is the face coupling channel count: four faces on TetA times four sub channels per face, where TetB vertices subdivide TetA faces by the medial triangle theorem. The k^2 term is state independent. It contributes 16 regardless of the acceleration. It is what keeps the polynomial positive everywhere (without it, f could go negative at s = -1) and what sets the span of 8 = 2K between the TetA and TetB endpoints. In the bimetric parameterization of Hassan and Rosen, this term maps to beta_2 = 16, and it contributes 96 out of 98 of the total interaction energy at proportional background. (Hassan and Rosen, 2012) The face coupling dominates.
**The sk term provides the flow.** This is the only state dependent part. Through the Mobius map, it becomes the signal that moves the capacity function between its endpoints as the acceleration changes. At the Field Origin, sk = 0. No flow. The capacity sits at its midpoint, f = 17, mu = 1/2. In the deep field regime, sk approaches -4 and pushes f down toward 13. In the Newtonian regime, sk approaches +4 and pushes f up toward 21. Without this term, f = 17 everywhere and the constitutive law would give mu = 1/2 at all accelerations. There would be no dynamics, no transition, and no galaxy rotation curves. The sk term is what makes gravity change character with acceleration.
**The k^0 = 1 term produces saturation.** This is the Field Origin itself, the single point at the geometric center of the stellated octahedron where all eight compression vectors cancel. In the language of surface chemistry, it is one adsorption site. One site gives Langmuir saturation: mu = x/(1 + x). The "1" in the denominator of the constitutive law is this term. If the Field Origin counted as c sites instead of 1, the denominator would be (x + c) and the transition would occur at x = c rather than x = 1. One Field Origin, one site, transition at unit acceleration ratio. The saturation is topological.
All three terms are necessary. None is sufficient alone. The constitutive law requires the complete coupling polynomial to produce the specific functional form mu = x/(x + 1).
## The Partition Function

The constitutive law is not a correction to Newtonian gravity. It is a partition function.
At every radius in a galaxy, the total gravitational acceleration g splits into two parts:

**TetA fraction: mu(x) = x / (x + 1)**  
**TetB fraction: 1 - mu(x) = 1 / (x + 1)**

The sum is always 1. Always 100% of the field. This is not a modification. It is a decomposition. The gravitational field has two chambers, and the constitutive law tells you how much of the total effect each chamber carries at a given acceleration.
This decomposition has a striking symmetry. Replace x with 1/x in the constitutive law:

$$
\mu(1/x) = \frac{1/x}{1/x + 1} = \frac{1}{x + 1} = 1 - \mu(x)
$$

Whatever fraction is processed by TetA at acceleration x is processed by TetB at acceleration 1/x. This is the complement symmetry of the stellated octahedron: the two chambers are perfect duals of each other, related by inversion through the Field Origin. Whatever is Newtonian at one scale is field dominated at the reciprocal scale.
What standard cosmology calls dark matter is, in this framework, the TetB fraction. It is not a particle. It is not invisible mass. It is the gravitational field second chamber doing its share of the work. And it is fully determined: given the observed rotation curve on one side of the partition, the constitutive law uniquely determines the other side.
## The Screening Equation

The equation x(1 - mu) = mu looks like a constraint that must be imposed on the constitutive law. It is not. It is an algebraic identity.
Start from $\mu = x/(x + 1)$. Then $1 - \mu = 1/(x + 1)$. Multiply: $x \times 1/(x + 1) = x/(x + 1) = \mu$. The screening equation is satisfied automatically, by the algebra of the normalization, not by any external requirement.
This identity has a physical reading: signal times remaining capacity equals used capacity. The acceleration ratio x is the signal. The remaining capacity (1 - mu) is how much room the field has left. The used capacity mu is how much is already engaged. The equation says these three quantities are in balance at every point in the field. This is detailed balance, the same equilibrium condition that governs chemical kinetics, Langmuir adsorption, and every other saturation process in physics. The gravitational field obeys it because field closure is lossless: no wakes, no drag, no hysteresis.
## The Constitutive Law Is the Poisson Equation

This is the central connection, and it is worth stating carefully.

The Poisson Equation page derived the gravitational field equation from topological integers:

$$
\nabla^2 \Phi = K\pi \times \frac{K^2 + 1}{KD + 1} \times G_{\text{bare}} \times \rho = 4\pi \times \left(\frac{17}{13}\right) \times G_{\text{bare}} \times \rho$$

Every factor in that equation comes from the coupling polynomial. The 4pi = Kpi is the solid angle partition by K = 4 tetrahedral faces. The 17 = f(K, 0) is the coupling capacity at the Field Origin. The 13 = f(K, -1) is the observable capacity at the spatial projection. The ratio 17/13 is f sampled at two fixed structural states: s = 0 and s = -1.
Now consider the MOND field equation with the constitutive law:

$$
\nabla \cdot [\mu(x)\nabla \Phi] = 4\pi G\rho
$$

This equation evaluates f continuously, not at two fixed points, but across all acceleration states through the Möbius map. The constitutive law $\mu = (f - 13)/8$ sweeps the capacity function through its entire range as the acceleration varies from point to point.
These are not two different equations. They are two projections of the same polynomial.
The Poisson equation samples the coupling polynomial at two fixed structural states, the Field Origin and the spatial projection, and packages the result as a constant prefactor 4pi(17/13)G_bare. The constitutive law evaluates the same polynomial continuously, letting the state parameter vary with the local acceleration. One is a snapshot. The other is a film. Both are images of f(K, s) = 1 + sK + K^2.
To see this concretely, take the MOND equation in spherical symmetry. It reduces to $\mu(g/a_0)\,g = GM/r^2$. Substitute $\mu = x/(x + 1)$ with $x = v^2/(ra_0)$:

$$
\frac{v^4}{v^2 + ra_0} = \frac{GM}{r}
$$

which rearranges to:

$$
v^4 = GM \times (g + a_0)
$$

This is the local field equation. It contains all of Newtonian gravity (when $g \gg a_0$, the equation gives $v^4 \approx GM \times g$, which is the standard virial relation) and all of the deep field regime (when $g \ll a_0$, it gives $v^4 \approx GM \times a_0$, which is the baryonic Tully Fisher relation $M \propto v^4$). The constitutive law bridges them with one continuous function.
The mass decode formula falls out immediately:

$$
M = \frac{rv^4}{G(a_0r + v^2)}
$$

Given observed velocities v at radius r, this extracts the baryonic mass directly, without assuming any mass model and without invoking dark matter. It is a closed form expression because $\mu = x/(x + 1)$ has an algebraic inverse: $x = \mu/(1 - \mu)$. No other proposed interpolation function gives an exact decode. The standard form $\mu = x/\sqrt{1 + x^2}$ requires a square root in its inverse. The RAR form $\mu = 1 - e^{-\sqrt{x}}$ requires a logarithm. Only the topological form is algebraic, because only the topological form comes from normalizing a polynomial.
## Why This Particular Function

In 1983, Mordehai Milgrom noticed that galactic rotation curves all deviate from Newtonian predictions at the same characteristic acceleration, regardless of the galaxy size, mass, or type. He proposed modifying Newton second law below this scale, introducing an interpolation function mu(x) that must approach 1 for strong fields and x for weak fields. He did not specify its exact form. For forty years, the MOND community debated which function to use. (Milgrom, 1983)
Several candidates emerged. The standard form mu = x/sqrt(1 + x^2). The simple form mu = x/(x + 1). The RAR form mu = 1 - exp(-sqrt(x)). The n family mu = x/(1 + x)^(1/n). All satisfy Milgrom asymptotic requirements. All fit rotation curves reasonably well. The data progressively favored the simple form, but without a theoretical reason to prefer it, the choice remained empirical.
Gravitational Field Dynamics provides the reason. The simple form is the unique constitutive law that emerges from normalizing the coupling polynomial of the stellated octahedron. It is not one option among many. It is the only function consistent with the K = 4 topology. And it possesses a suite of structural properties that no other candidate shares: Langmuir saturation from the single Field Origin, an algebraic Mobius inverse, a screening equation that is an identity rather than a constraint, a closed form kinetic functional for the Bekenstein Milgrom action, complement symmetry mu(x) + mu(1/x) = 1, and exact round trip invertibility between the TetA and TetB velocity curves.
Milgrom discovered the right answer empirically. (Milgrom, 1983) The stellated octahedron explains why it is right.
## Scale Invariance

The Poisson Equation page showed that every factor in the gravitational field equation traces to topological integers that do not change with scale. The constitutive law inherits this property.
The factor 4pi = Kpi comes from field closure requiring K = 4 tetrad basis vectors. These four vectors partition the total solid angle into four equal parts of pi steradians each. No radius appears. The factor 17/13 comes from evaluating the coupling polynomial at two structural states. Both 17 and 13 are integers determined by K = 4 and D = 3. The constitutive law mu(x) = x/(x + 1) depends only on the dimensionless ratio x = g/a0, not on any absolute scale.
An atom establishes field closure at its valence radius. A star establishes field closure at its stellar radius. A galaxy establishes field closure at its virial radius. At each level, the topology is the same: K = 4 faces, D = 3 dimensions, and the coupling polynomial f(K, s) = 1 + sK + K^2. The constitutive law does not change between these scales because it is a function of topological integers, and topological integers do not care how big you are. A tetrahedron has four faces whether it is the size of a proton or the size of a galaxy cluster.
This is why the same equation governs gravitational fields from 10^-13 meters to 10^23 meters. Not because of an unknown deep principle. Because every number in the equation is a reading of the stellated octahedron, and those readings are the same at every scale.
## What You Now Have

One constitutive law, derived from the coupling polynomial, not fitted to data. Three terms, each with a geometric identity: the face coupling sets the range, the state dependent flow moves the pointer, and the Field Origin produces saturation. The result is a partition function that divides the gravitational field between two chambers, predicts flat rotation curves without dark matter, reproduces the Tully Fisher relation in the deep field limit, recovers Newton exactly in the strong field limit, and is the same equation as the Poisson equation read continuously rather than at two fixed points.
The Scalar Tensor Completion page takes this constitutive law and embeds it in a covariant action. The Bimetric Locking page shows what happens when both chambers are dynamical. Everything that follows is the constitutive law applied to increasingly precise observational tests.
One equation. Two chambers. Zero free parameters.

## References

Hassan, S. F. and Rosen, R. A. (2012). Bimetric gravity from ghost free massive gravity. J. High Energy Phys. 02, 126.

Milgrom, M. (1983). A modification of the Newtonian dynamics as a possible alternative to the hidden mass hypothesis. Astrophys. J. 270, 365.
