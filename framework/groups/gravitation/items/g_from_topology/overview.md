# G from Topology

## From Polynomial to Prediction

The previous page derived the coupling polynomial

$$
f(K, s) = 1 + sK + K^2
$$

and evaluated it in the three structural regions of the stellated octahedron: 21 in TetA, 17 at the Field Origin, and 13 in TetB. You now hold three integers. This page turns them into the gravitational constant.
Newton gravitational constant

$$
G = 6.674 \times 10^{-11}\ \mathrm{m^3\ kg^{-1}\ s^{-2}}
$$

has been measured with increasing precision since Cavendish torsion balance experiment in 1798. For over two centuries, no theory has calculated its value from first principles. It has always been an empirical input, a number you measure, not a number you derive. The coupling polynomial changes this. Every piece of $G$ has a structural name in the stellated octahedron, and nothing is free.
## The Three Ingredients

The equation for $G$ has three factors, each with a clear topological origin.
**The prefactor: 17/13.** This is the ratio of coupling capacity to spatial structure, the polynomial evaluated at the Field Origin divided by the polynomial evaluated in TetB. At the Field Origin ($s = 0$), the 16 components of the frame transition matrix plus 1 existence condition give 17, this is how many independent ways the two chambers can couple at the point where they meet. In TetB ($s = -1$), the $K \times D = 12$ directed spatial coupling components plus 1 for nondegeneracy give 13, this is the spatial scaffold that supports the coupling. The ratio 17/13 measures the overhead, how much coupling capacity exists relative to the spatial structure that carries it.
**The exponent: $\alpha^{21}$.** The gravitational field couples through 21 levels, the full polynomial $f(K, +1) = 1 + 4 + 16 = 21$. At each level, coupling attenuates by fine structure constant $\alpha \approx 1/137$, which is the topology own scale ratio (derived on the Fine Structure Constant page). Twenty one levels of attenuation gives $\alpha^{21}$. This is why gravity is so weak: not because of some mysterious suppression mechanism, but because the field must traverse every coupling level of the stellated octahedron to complete interaction. Each level costs a factor of $\alpha$. Twenty one levels cost $\alpha^{21} \approx 10^{-45}$.
**The scale: $\hbar c / m_e^2$.** The topology determines every pure number, the integers 17, 13, and 21, and the ratio $1/137$. But pure numbers carry no units. To express $G$ in physical units, $\mathrm{m^3\ kg^{-1}\ s^{-2}}$, you need a dimensional anchor. The natural scale of the stellated octahedron is set by the electron, the particle whose mass and radius are determined by closure topology (as shown on the Electron Mass page). The combination $\hbar c / m_e^2$ has the correct dimensions and provides the bridge from topology to measurement.
## The Equation

Combining the three ingredients:

$$
G = \left(\frac{17}{13}\right)\alpha^{21}\frac{\hbar c}{m_e^2}
$$

Written with the (3+1) structure visible in every component:

$$
G = \frac{(3+1)^2 + 1}{3(3+1) + 1} \times \alpha^{1 + (3+1) + (3+1)^2} \times \frac{\hbar c}{m_e^2}$$

Predicted: $6.666 \times 10^{-11}\ \mathrm{m^3\ kg^{-1}\ s^{-2}}$  
Measured: $6.674 \times 10^{-11}\ \mathrm{m^3\ kg^{-1}\ s^{-2}}$  
Agreement: 0.12% at tree level.

Every number in this equation traces to the stellated octahedron. The 17 is the Hamiltonian interaction space dimension. The 13 is the spatial structure of the inverted sector. The 21 is the geometric series on the simplex boundary. The "1" that appears four times, in 17 = 16 + 1, in 13 = 12 + 1, in the exponent leading term, and implicitly in $\alpha$ derivation, is the Field Origin, the single point where both chambers meet and where time equals zero.
## The Exponent Is Catastrophically Sensitive

The agreement at 21 is not one of many workable values. It is the only value in the vicinity that produces a physically reasonable gravitational constant. Each unit change in the exponent multiplies or divides the prediction by $1/\alpha \approx 137$:

| Exponent | Predicted G | Status |
|---|---|---|
| 20 | $9.1 \times 10^{-9}$ | 137x too large |
| **21** | **$6.67 \times 10^{-11}$** | **0.12% agreement** |
| 22 | $4.9 \times 10^{-13}$ | 137x too small |

Adjacent integers miss by over two orders of magnitude. The polynomial value of $21 = 1 + 4 + 16$ is not approximately right, it is the unique integer that works. Extracting the exponent directly from measured $G$ gives
$$
n = \frac{\log\left[(13/17)\times Gm_e^2/(\hbar c)\right]}{\log(\alpha)} \approx 21.0,$$

confirming that topology selects the correct integer with no room to spare.
## The One Loop Correction

The tree level prediction deviates from measurement by 0.12%. This residual is not noise, it has a precise physical identity.
The Schwinger one loop QED correction is

$$
\frac{\alpha}{2\pi} = 0.116\%,
$$

the same universal correction that shifts the electron magnetic moment from exactly 2 to $2(1 + \alpha/(2\pi))$. The residual in $G$ and the Schwinger correction are the same number because they represent the same physics, the electron self interaction at one loop.
Including it:

$$
G_{1\text{-loop}} = \left(\frac{17}{13}\right)\alpha^{21}\left(1+\frac{\alpha}{2\pi}\right)\frac{\hbar c}{m_e^2} = 6.6742 \times 10^{-11}$$

Measured: $6.6743 \times 10^{-11}$. The residual improves from 0.12% to 0.001%, two orders of magnitude closer, with zero new parameters. The polynomial provides the tree level structure. Quantum electrodynamics provides the quantum corrections. The framework naturally interfaces with the most precise theory in physics and inherits its precision.
## Four Consequences Encoded in One Equation

The equation for $G$ is not just a formula for one constant. It encodes four fundamental relationships, each readable from a different part of the structure:

The **(3+1) in the prefactor** reflects the four sub regions of one coupled face, the minimal simplex structure in $D = 3$ dimensions. The same three dimensionality produces inverse square through field spreading over $4\pi r^2 = K\pi r^2$.
The **bimetric structure in the scale** explains why mass energy conversion involves $c^2$. Two tetrahedra, each maintaining closure at speed $c$, give product $c \times c = c^2$ (as the Mass Energy Equivalence page showed).
The **exponent 21** encodes force hierarchy. Gravity traverses all 21 coupling levels. Electromagnetism traverses 1. The ratio is $\alpha^{20} \approx 10^{-43}$, which is why gravity is $10^{43}$ times weaker than electromagnetism. Not because gravity is mysteriously suppressed, but because it has further to travel through topology.
The **complete equation** combines prefactor, coupling, and scale to yield $G$ to 0.001% at one loop.
One equation. Four readings. Every number is derived from stellated octahedron face structure, evaluated in $K = 4$ and $D = 3$.
