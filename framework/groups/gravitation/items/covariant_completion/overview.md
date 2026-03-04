# Covariant Completion

## Overview

In the previous page, you saw how the discrete topology of the stellated octahedron is mapped by the coupling polynomial $f(K, s) = 1 + sK + K^2$. You saw how evaluating this polynomial across the three structural states locks the fundamental integers $21$, $17$, and $13$ into the gravitational constant.
But a geometry and a polynomial do not constitute a field theory. You cannot predict orbits, compute lensing, or model the early universe with integers alone. For that, the discrete topology must be translated into the language of continuous spacetime. You need an action: a single expression whose variation yields the equations of motion for every field in the theory.
The Covariant Action of Gravity Field Dynamics (GFD) is that translation. It is a fully covariant scalar-tensor framework with zero free parameters, where every term and every numerical prefactor is a direct projection of the coupling polynomial.
## The Four Terms of the Action

The complete GFD action consists of exactly four terms:

$$
S = \int d^4x \sqrt{-g}\left[\frac{R}{16\pi G} - \frac{a_0^2}{8\pi G}F(y) - \frac{1}{4}e^{-2\Phi/c^2}F_{\mu\nu}F^{\mu\nu} + \mathcal{L}_{\text{matter}}\right]
$$

Each term has one specific job, and each carries a prefactor determined directly by the stellated octahedron.

**$R/(16\pi G)$, the Curvature Term.** This is standard general relativity. The Ricci scalar $R$ governs the shape of spacetime: how clocks tick, rulers stretch, and light bends. The prefactor $16\pi G = K^2 \cdot \pi \cdot G_{\text{eff}}$ contains the $K^2 = 16$ face-coupling channels, the solid angle per face $\pi$, and the effective gravitational constant. The full coupling hierarchy is preserved inside $G$ through the exponent $21 = f(K, +1)$, the numerator $17 = f(K, 0)$, and the denominator $13 = f(K, -1)$. The curvature term carries the topology compressed into a single constant.

**$-a_0^2/(8\pi G)\,F(y)$, the Scalar Sector.** This governs how the scalar field $\Phi$ responds to matter. The prefactor $8\pi G = 2^D \cdot \pi \cdot G_{\text{eff}}$ contains $2^D = 8$, the vertex-space cardinality of the stellated octahedron. No free functions remain. The topology fixes the prefactor, and the kinetic functional $F(y)$ is fixed by the structural levels of the polynomial.

**$-\frac{1}{4} e^{-2\Phi/c^2} F_{\mu\nu}F^{\mu\nu}$, the Electromagnetic Coupling.** Photons do not see the bare metric. They see an effective metric modified by the disformal factor $e^{-2\Phi/c^2}$. Without this term, lensing would produce only half the observed deflection. The factor of $2$ in the exponent has the same structural origin as the $2$ in $E = mc^2$: it counts the two tetrahedra. Photons must couple to the full dual tetrahedral potential, ensuring the PPN parameter $\gamma = 1$ exactly (consistent with the Cassini bound of $2.1 \pm 2.3 \times 10^{-5}$), and guaranteeing that lensing mass equals dynamical mass.

**$\mathcal{L}_{\text{matter}}$, Matter.** Ordinary matter, minimally coupled to the metric. Stars, gas, dust, everything on the right side of Einstein's equations. (Einstein, 1915) There is no modification, no coupling to the scalar field, and no violation of the equivalence principle.
### The Prefactors Are the Topology

Every numerical prefactor in the action traces to the coupling polynomial evaluated at $K = 4$ and $D = 3$. The curvature term carries $16\pi G$. The scalar sector carries $8\pi G$. The electromagnetic coupling carries $1/4$. These three numbers, $16$, $8$, $4$, form a geometric sequence: $K^2$, $2^D$, $K$. Each is the polynomial's weight at its respective structural level. The ratio between consecutive prefactors is always $2$, distinguishing a single-chamber quantity from a dual-chamber quantity in the stellated octahedron.
The gravitational constant $G$ itself carries the full coupling hierarchy: the exponent $21$ (depth), the prefactor $17/13$ (coupling capacity over spatial structure), and the dimensional anchor $\hbar c/m_e^2$ (scale).
## The Scalar Sector and the Energy Functional

The heart of the scalar sector is the kinetic functional $F(y)$, where $y = |\nabla\Phi|^2/a_0^2$ is the dimensionless squared acceleration. This functional is not a phenomenological guess. It is the exact energy equivalent of the coupling polynomial, and the derivation is short enough to present in full.
### From Polynomial to Energy Functional

The Constitutive Law page shows that the Mobius map $s(x) = (x - 1)/(x + 1)$ makes the coupling polynomial $f(K,s) = 1 + sK + K^2$ continuous in the acceleration ratio $x = |\nabla\Phi|/a_0$. Composing the polynomial with this map gives the capacity function $f(x) = (21x + 13)/(x + 1)$, and normalizing by the total range $2K = 8$ yields the constitutive law:

$$
\mu(x) = \frac{x}{x + 1}
$$

The AQUAL identity (Bekenstein and Milgrom, 1984) relates the energy functional to the constitutive law by integration. If $\mu(\sqrt{y}) = dF/dy$, then $F$ is the antiderivative:

$$
F(y) = \int_0^y \mu(\sqrt{t})\,dt
$$

Substituting $\mu(x) = x/(x + 1)$ with $x = \sqrt{t}$ and changing variables to $u = \sqrt{t}$, so that $dt = 2u\,du$:

$$
F(y) = 2\int_0^{\sqrt{y}} \frac{u^2}{u + 1}\,du = 2\int_0^{\sqrt{y}} \left(u - 1 + \frac{1}{u + 1}\right) du
$$
Evaluating:

$$
F(y) = 2\left[\frac{u^2}{2} - u + \ln(u + 1)\right]_0^{\sqrt{y}} = y - 2\sqrt{y} + 2\ln(1 + \sqrt{y})
$$
Every coefficient traces to the coupling polynomial. The leading $y$ comes from the $K^2$ face coupling. The $-2\sqrt{y}$ comes from the state dependent $sK$ flow, with the coefficient $2$ counting the two tetrahedra. The $2\ln(1 + \sqrt{y})$ comes from the $K^0 = 1$ Field Origin, again with coefficient $2$ from the dual structure. The polynomial determines $\mu$, and $\mu$ determines $F$ uniquely.
The three terms of this result correspond strictly to the three structural levels of the coupling polynomial $f(K, s) = 1 + sK + K^2$:

**$y$, the Full Interaction Level.** This is the $K^2 = 16$ term, representing the face-to-face coupling between TetA and TetB. It is quadratic in the field gradient and dominates at high accelerations where all 16 coupling channels are active.
**$-2\sqrt{y}$, the Face Propagation Level.** This is the $sK = 4$ term, representing state-dependent flow. The negative sign parallels the structural state $s = -1$, where partially occupied propagation channels represent an energy cost. The coefficient $2$ counts the two tetrahedra. At intermediate accelerations near $a_0$, this term competes with the quadratic to drive the transition between regimes.
**$2\ln(1+\sqrt{y})$, the Field Origin Level.** This is the $K^0 = 1$ term, the irreducible coupling point where both tetrahedra meet. It is logarithmic, never zero, and always present, exactly as field closure ($\det(e) \neq 0$) demands. The coefficient $2$ reflects the dual tetrahedral structure. In the deep field regime ($y \ll 1$), this term dominates, producing the amplification that flattens rotation curves.
## From Energy to Response: The Constitutive Law

The route from an energy functional to a field response is a standard operation in physics. Hooke's law states that elastic potential energy determines the restoring force via differentiation. Ohm's law dictates that dissipated power relates to current and voltage. Energy gives the dynamics, and the derivative of that energy gives the response.
Standard variational calculus (specifically the AQUAL identity established by Bekenstein and Milgrom) requires that the response function $\mu$ and the energy functional $F(y)$ be related by differentiation:

$$
\mu(\sqrt{y}) = \frac{dF}{dy}
$$

Differentiating our unique topological energy functional $F(y)$ yields the constitutive law:

$$
\mu(x) = \frac{x}{1+x}
$$

where $x = \sqrt{y} = |\nabla\Phi|/a_0$. This equation tells you exactly how the gravitational field responds to mass at every acceleration. The three terms of $F(y)$ are simply the three levels of the polynomial written in the language of energy. The constitutive law is that same polynomial normalized for coupling capacity.
## The Two Field Equations

Varying the complete action with respect to the scalar field $\Phi$ in the spherically symmetric, static limit yields two working equations. They are not independent postulates bolted together. They emerge from a single variational principle.
The first is the Poisson equation:

$$
\nabla^2\Phi = 4\pi G\rho
$$

This source equation determines the Newtonian potential, utilizing the CODATA value of $G$ which already contains the topological ratio $17/13$.
The second is the Scalar-Tensor Transition:

$$
g_s = \frac{g_t^2}{a_0 + g_t}
$$

This relates the source acceleration $g_s$ to the total acceleration $g_t$ governing circular orbits. At high acceleration ($g_t \gg a_0$), the denominator is dominated by $g_t$ and $g_s \to g_t$: Newtonian gravity. At low acceleration ($g_t \ll a_0$), the denominator is dominated by $a_0$ and $g_t \to \sqrt{g_s \cdot a_0}$: the deep field regime where rotation curves flatten.
Because both relations are algebraic, they form the Inverse Pipeline. This allows baryonic mass to be decoded directly from observed rotation curves without a dark matter halo, using the mass decode formula:

$$
M_{\text{dec}}(r) = \frac{rv^4}{G(a_0 r + v^2)}
$$

## Limit Checks

The action recovers established physics in the appropriate limits.

**High-acceleration ($y \gg 1$).** $F(y) \to y$. The constitutive law gives $\mu \to 1$. The scalar sector becomes indistinguishable from a minimally coupled scalar, and the full action reduces to standard general relativity plus a decoupled scalar. Gravity is strictly Newtonian.
**Low-acceleration ($y \ll 1$).** The leading contribution to $F$ is $\frac{2}{3}y^{3/2}$. This nonlinear kinetic term enforces the deep field behavior $g_t \to \sqrt{g_s \cdot a_0}$, recovering the baryonic Tully-Fisher relation $M \propto v^4$. The field amplifies weak sources.
The logarithmic term smoothly handles the crossover. There is no sharp boundary or patching of two theories.
The disformal coupling ensures $\gamma = 1$ to the precision of the Cassini bound ($2.1 \pm 2.3 \times 10^{-5}$), and the lensing deflection is the full general relativistic value $\theta = 4GM/(rc^2)$. The factor of $2$ beyond the Newtonian value, which GR predicts and observations confirm, is built into the action through the disformal exponent $-2\Phi/c^2$.
## What You Now Have

A fully covariant field theory derived strictly from geometry. Four terms in the action, each with a topological identity: curvature ($16\pi G$), scalar sector ($8\pi G$), electromagnetic coupling ($1/4$), and matter. Three structural levels in the kinetic functional $F(y) = y - 2\sqrt{y} + 2\ln(1+\sqrt{y})$. Two field equations. One topology. Zero free parameters.
The preceding pages demonstrated that the Poisson equation and the coupling polynomial are two projections of the same geometric truth. The Covariant Action is the final projection: the topology fully integrated into a relativistic framework.
The Scalar-Tensor Completion page examines the action's field equations in detail. The Bimetric Locking page shows how the same coupling polynomial, evaluated at its static skeleton, locks the five free parameters of bimetric gravity to the integer set $\{1, 0, 16, 0, 1\}$. The action you hold here and the bimetric potential derived there are projections of the same geometric object onto different energy scales.
Four terms. Three structural levels. Two field equations. One topology. Zero free parameters.

## References

Einstein, A. (1915). Die Feldgleichungen der Gravitation. Sitzungsber. Preuss. Akad. Wiss. 844.

Bekenstein, J. D. and Milgrom, M. (1984). Does the missing mass problem signal the breakdown of Newtonian gravity? Astrophys. J. 286, 7.
