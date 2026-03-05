# Electron Mass

## Why This Matters

The electron mass is one of the most precisely known quantities in physics: $m_e = 9.109 \times 10^{-31}\ \mathrm{kg}$. Every atom, every chemical bond, every beam of light absorbed or emitted by matter depends on this number. Yet no theory has explained why it takes this value. The Standard Model treats it as a free parameter, a Yukawa coupling measured from experiment and inserted by hand. String theory cannot predict it. Loop quantum gravity does not address it. In every framework that exists, the electron mass is an input. It is given, not derived.

Gravitational Field Dynamics derives it. The electron mass is the unique mass for which gravitational field closure at the quantum scale is consistent with the observed transition acceleration. It links three domains of physics through a single equation: quantum mechanics ($\hbar$), gravity ($G$), and electromagnetism ($\alpha$). The bridge between them is one topological integer: $K = 4$.

## The Two Equations

The derivation uses two independent equations and one identity. Each comes from a different part of the framework, and none uses the electron mass as an input.

**Equation 1: Closure saturation.** The tetrad $e^a_\mu$ has two indices: the frame index $a$ and the coordinate index $\mu$, each running from 0 to 3. The metric construction $g_{\mu\nu} = \eta_{ab}\,e^a_\mu\,e^b_\nu$ couples geometry to frame structure through summation over both indices, engaging all $K \times K = 16$ components. Gravity is isotropic: no frame direction is privileged, so full coupling requires all $K^2 = 16$ channels simultaneously. This means the gravitational acceleration at the closure tile boundary is amplified by the full coupling factor:

$$
a_0 = K^2 \frac{Gm}{r^2}
$$

This is not a postulate. It is the condition that the topologically amplified gravitational acceleration at the closure tile boundary matches the transition scale $a_0$, whose measured value is given in Equation 2.

**Equation 2: The transition acceleration.** The transition acceleration $a_0 \approx 1.22 \times 10^{-10}\ \mathrm{m/s^2}$ was identified empirically by Milgrom (1983) from the point in galaxy rotation curves where Newtonian dynamics breaks down. It has since been measured consistently across hundreds of galaxies spanning five decades in mass, from gas-rich dwarfs to massive spirals. Within this framework, $a_0$ is not a free parameter; it is derivable from the Hubble constant through horizon thermodynamics (see the Characteristic Scale page). For the present derivation, we take its measured value directly:

$$
a_0 = 1.22 \times 10^{-10}\ \mathrm{m/s^2}
$$

This keeps the electron mass derivation independent of the $a_0$ derivation, so each can be verified on its own terms.

**The mass closure identity.** The classical electron radius $r_e = e^2/(4\pi\epsilon_0 m_e c^2)$ can be rewritten using $\alpha = e^2/(4\pi\epsilon_0 \hbar c)$ as:

$$
m = \frac{\alpha \hbar}{rc}
$$

This is not a new equation. It is the definition of the classical electron radius expressed as a mass. Physically, it says: mass is the energy cost of completing one electromagnetic closure cycle at speed $c$ across a tile of radius $r$, with $\alpha$ measuring the strength of the coupling. It is the bridge between the electromagnetic description (charge, permittivity) and the gravitational description (tile size, topology) of the same particle.

## The Derivation

There are two unknowns: the tile radius $r$ and the mass $m$. There are two equations and one identity. The system is exactly determined.

**Step 1.** Substitute the mass closure identity into the closure saturation equation. Replace $m$ with $\alpha\hbar/(rc)$:

$$
a_0 = K^2 \frac{G}{r^2} \cdot \frac{\alpha\hbar}{rc} = \frac{K^2 G \alpha \hbar}{r^3 c}
$$

**Step 2.** Solve for $r$:

$$
r^3 = \frac{K^2 G \alpha \hbar}{a_0 \, c}
$$

$$
r = \left(\frac{K^2 G \alpha \hbar}{a_0 \, c}\right)^{1/3}
$$

**Step 3.** Insert the measured value $a_0 = 1.22 \times 10^{-10}\ \mathrm{m/s^2}$:

$$
r = \left(\frac{K^2 G \alpha \hbar}{a_0 \, c}\right)^{1/3}
$$

Using $K = 4$, $G = 6.674 \times 10^{-11}$, $\alpha = 1/137.036$, $\hbar = 1.055 \times 10^{-34}$, $c = 2.998 \times 10^8$, and $a_0 = 1.22 \times 10^{-10}$:

$$
r = 2.82\ \mathrm{fm}
$$

**Step 4.** Recover the mass from the closure identity:

$$
m = \frac{\alpha \hbar}{rc} = \frac{(7.297 \times 10^{-3})(1.055 \times 10^{-34})}{(2.82 \times 10^{-15})(2.998 \times 10^8)}
$$

$$
m = 9.11 \times 10^{-31}\ \mathrm{kg}
$$

The measured electron mass is $9.109 \times 10^{-31}\ \mathrm{kg}$. The derivation recovers it to 0.1%.

No electron mass was used as an input. The only inputs are $\alpha$, $\hbar$, $G$, $c$, $a_0$, and $K = 4$. The electron mass fell out of the algebra.

## Three Roads to One Village

What makes this result compelling is not one derivation but three. The characteristic tile size $r = 2.82\ \mathrm{fm}$ can be reached from three independent domains of physics. Each uses different constants. Each is independent of the others. All three arrive at the same number.

**Route 1: Electromagnetic stability.** Consider a charged sphere of radius $r$ carrying charge $e$. The energy stored in its electric field is $U_{\mathrm{EM}} = e^2/(4\pi\epsilon_0 r)$. As the sphere shrinks, this energy grows. At some radius, the field energy equals the particle's rest mass energy $m_e c^2$. Below that radius, the electric field carries more energy than the particle itself, and pair production becomes possible. That radius is the classical electron radius:

$$
r_e = \frac{e^2}{4\pi\epsilon_0 m_e c^2} = 2.818\ \mathrm{fm}
$$

This is a textbook calculation dating to Lorentz. It uses electromagnetism ($e$, $\epsilon_0$) and special relativity ($c$). No gravity. No cosmology. No topology. It is the electromagnetic stability boundary of the electron.

**Route 2: Gravitational topology.** At what radius does the topologically coupled gravitational acceleration equal the transition scale $a_0$? The tetrad's $K^2 = 16$ coupling channels amplify the Newtonian gravitational acceleration $Gm/r^2$ by a factor of $K^2$, because full isotropic coupling engages all 16 components of the tetrad field simultaneously. Setting this equal to $a_0$:

$$
K^2 \frac{Gm_e}{r^2} = a_0
$$

and solving gives:

$$
r = K\sqrt{\frac{Gm_e}{a_0}} = 4 \times \sqrt{\frac{(6.674 \times 10^{-11})(9.109 \times 10^{-31})}{1.22 \times 10^{-10}}} = 2.82\ \mathrm{fm}
$$

This route uses gravity ($G$), cosmology ($a_0$), and topology ($K = 4$). No electromagnetism. The factor $K$ appears linearly because $K^2$ enters the acceleration and solving for $r$ extracts the square root.

**Route 3: Closure topology.** This is the derivation shown above. It uses $\alpha$, $\hbar$, $G$, $a_0$, $K$, and $c$, but not the electron mass. It recovers both $r = 2.82\ \mathrm{fm}$ and $m = 9.11 \times 10^{-31}\ \mathrm{kg}$.

| Route | Constants used | Result | Domain |
|---|---|---|---|
| 1: EM stability | $e$, $\epsilon_0$, $m_e$, $c$ | $r = 2.818\ \mathrm{fm}$ | Electromagnetism |
| 2: Gravitational topology | $G$, $K$, $m_e$, $a_0$ | $r = 2.82\ \mathrm{fm}$ | Gravity and cosmology |
| 3: Closure topology | $\alpha$, $\hbar$, $G$, $a_0$, $K$, $c$ | $r = 2.82\ \mathrm{fm}$, $m = 9.11 \times 10^{-31}\ \mathrm{kg}$ | Gravity, QM, EM, topology |

Routes 1 and 2 agree to 0.21%. Route 3 recovers the electron mass to 0.1% of the measured value. The convergence is specific to the electron: for the muon, the routes disagree by a factor of three thousand. For the proton, by eighty thousand. Only for the electron do electromagnetic stability and gravitational topology meet at the same scale. This uniqueness is the signature of field closure. The electron is not special because we chose it. It is the particle whose electromagnetic stability boundary coincides with the gravitational closure tile.

## What This Means

An astronomer measures recession speeds of distant galaxies through a telescope. A particle physicist measures electron deflection in a magnetic field. These experiments use different instruments, scales, and methods. Yet the transition acceleration $a_0$, measured from galaxy rotation curves, and the electron mass, measured in laboratory experiments, are connected by one equation through topology in three-dimensional space. When $a_0$ is itself derived from the Hubble constant (see the Characteristic Scale page), the chain extends from the cosmological horizon to the electron. One topology, one integer, zero free parameters.

When three roads lead to the same village, the village is real. The electron mass is not an arbitrary parameter that happens to take its value. It is the unique mass for which field closure works, the one value that makes the gravitational field self-consistent from the Planck scale to the Hubble horizon, through one topology, with one integer, and zero free parameters.

## References

Milgrom, M. (1983). "A modification of the Newtonian dynamics as a possible alternative to the hidden mass hypothesis," *Astrophys. J.* 270, 365.
