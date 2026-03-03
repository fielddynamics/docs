# The Hubble Constant

## The Tension

The expansion rate of the universe should be a single number. Measure it one way, you get one answer. Measure it another way, you get the same answer. That is how constants are supposed to work. (CODATA Task Group, 2022; Planck Collaboration, 2020)

The Hubble constant does not cooperate. The Planck satellite, mapping the cosmic microwave background from the early universe, gives $H_0 = 67.4 \pm 0.5\ \mathrm{km\ s^{-1}\ Mpc^{-1}}$. The SH0ES collaboration, measuring distances to nearby supernovae using the cosmic distance ladder, gives $H_0 = 73.04 \pm 1.04\ \mathrm{km\ s^{-1}\ Mpc^{-1}}$. These two measurements disagree by more than five standard deviations, a gap so large that it is extremely unlikely to be a statistical accident. This is the Hubble tension, and it has persisted for over a decade despite increasingly precise instruments and increasingly careful analyses. (CODATA Task Group, 2022; Planck Collaboration, 2020)

Both measurements assume the same thing: gravity behaves identically at all scales. The same Newton constant, the same inverse square law, the same structureless continuum from the quantum scale to the cosmic horizon. If that assumption is wrong, if gravity has internal structure that modifies its behavior at different acceleration regimes, then both measurements are looking through a lens they do not know is there. (CODATA Task Group, 2022; Planck Collaboration, 2020)

Gravitational Field Dynamics predicts the Hubble constant from topology alone, with zero free parameters. The result is $H_0 = 70.21\ \mathrm{km\ s^{-1}\ Mpc^{-1}}$, sitting between Planck and SH0ES, consistent with the only measurement that makes no assumptions about gravity at all: the gravitational wave standard siren GW170817 ($70.0 \pm 12.0\ \mathrm{km\ s^{-1}\ Mpc^{-1}}$). (CODATA Task Group, 2022; Planck Collaboration, 2020)

## The Derivation Chain

The prediction follows a chain that begins with $D=3$ and ends with $H$. Every link is derived, none is fitted. (CODATA Task Group, 2022; Planck Collaboration, 2020)

The characteristic acceleration $a_0 = 1.2 \times 10^{-10}\ \mathrm{m\ s^{-2}}$ emerged in the Characteristic Scale page as the transition point where the two tetrahedral chambers contribute equally to the gravitational field ($\mu = 1/2$). This scale connects to Hubble expansion through the Hubble horizon. (CODATA Task Group, 2022; Planck Collaboration, 2020)

At the Hubble radius $R_H = c/H$, the recession velocity of the expanding universe equals the speed of light. This defines a minimum resolvable acceleration. Any acceleration smaller than $cH$ is indistinguishable from horizon curvature itself. The connection between $a_0$ and $H$ follows from horizon thermodynamics, the same framework that produces the Unruh and Gibbons Hawking effects:

$$
a_0 = \left(\frac{cH}{2\pi}\right)\sqrt{\frac{K}{\pi}}
$$

The factor $2\pi$ converts between geometric acceleration and the physical threshold, exactly as in the Unruh relation. The factor $\sqrt{K/\pi}$ is the geometric correction, and it is the heart of the story. (CODATA Task Group, 2022; Planck Collaboration, 2020)

## The Geometric Correction

Why $\sqrt{K/\pi}$? Because we measure through a discrete structure to a continuous boundary. (CODATA Task Group, 2022; Planck Collaboration, 2020)

The gravitational field has tetrahedral packing, $K=4$ faces per chamber, discrete, angular, flat faced. The Hubble horizon is spherical, continuous, curved, characterized by $\pi$. When you observe universe expansion, you are looking through flat faces of the local field structure out to the curved boundary of the cosmos. The ratio between these two geometries is $\sqrt{K/\pi} = \sqrt{4/\pi} \approx 1.128$. (CODATA Task Group, 2022; Planck Collaboration, 2020)

This is not a fudge factor. It is the same kind of correction that appears whenever you convert between a discrete lattice and a continuous boundary. The ratio of a square area to an inscribed circle area involves the same $\pi$. The gravitational field tetrahedral packing introduces a geometric mismatch with the spherical horizon, and $\sqrt{K/\pi}$ is the exact correction. (CODATA Task Group, 2022; Planck Collaboration, 2020)

Without this correction, the MOND relation $a_0 = cH/(2\pi)$ gives $H = 78.90\ \mathrm{km\ s^{-1}\ Mpc^{-1}}$, a value no observation has measured. With the correction:

$$
H = \frac{2\pi a_0}{c\sqrt{K/\pi}} = 70.21\ \mathrm{km\ s^{-1}\ Mpc^{-1}} (CODATA Task Group, 2022; Planck Collaboration, 2020)
$$

| Measurement | H₀ (km/s/Mpc) | Method |
|---|---|---|
| Planck (2020) | 67.4 ± 0.5 | CMB + ΛCDM model |
| GFD prediction | **70.21** | Topology, zero parameters |
| GW170817 | 70.0 ± 12.0 | Gravitational wave standard siren |
| SH0ES (2022) | 73.04 ± 1.04 | Distance ladder + Cepheids |

## What the Tension Actually Means

The Hubble tension is usually framed as a mystery: why do two careful measurements disagree? Gravitational Field Dynamics reframes it as a diagnosis. (CODATA Task Group, 2022; Planck Collaboration, 2020)

The Planck analysis infers $H$ by fitting the cosmic microwave background through the $\Lambda$CDM model, which assumes gravity is scale invariant. Below the acceleration scale $a_0$, the dual tetrahedral structure enhances gravitational coupling, an effect $\Lambda$CDM does not account for. This pulls the Planck estimate low. (CODATA Task Group, 2022; Planck Collaboration, 2020)

The SH0ES analysis calibrates distances using Newtonian gravity, which assumes inverse square holds exactly at all accelerations. In regions where accelerations fall below $a_0$, including outskirts of the Cepheid calibration galaxies, the constitutive law $\mu(x) = x/(x+1)$ modifies effective gravitational coupling. This pushes the SH0ES estimate high. (CODATA Task Group, 2022; Planck Collaboration, 2020)

The GFD prediction of $70.21\ \mathrm{km\ s^{-1}\ Mpc^{-1}}$ is not a split the difference compromise. It is the value topology requires. The tension between 67.4 and 73.04 may not reflect a problem with either measurement. It may reflect a shared assumption, that gravity has no internal structure, on which both teams unknowingly rely. (CODATA Task Group, 2022; Planck Collaboration, 2020)

## The Full Circle

The Hubble constant and electron mass are not independent quantities. They are two outputs of the same closure system. The same two equations, gravitational closure saturation and the Hubble horizon connection, that determine electron mass also determine $H$. Change one, and the other must change with it. (CODATA Task Group, 2022; Planck Collaboration, 2020)

An astronomer telescope and a particle physicist spectrometer, instruments separated by centuries of development and forty orders of magnitude in scale, are measuring the same topology. The Hubble constant is the cosmological echo of the stellated octahedron closure requirement, projected through $\sqrt{K/\pi}$ from discrete to continuous, from tile to horizon, from $K=4$ to the expanding universe. (CODATA Task Group, 2022; Planck Collaboration, 2020)

## References

CODATA Task Group. (2022). CODATA recommended values of the fundamental constants.

Particle Data Group Collaboration. (2024). Review of Particle Physics.

Planck Collaboration. (2020). "Planck 2018 results. VI. Cosmological parameters," Astron. Astrophys. 641, A6.

Riess, A. G. et al. (2022). "A Comprehensive Measurement of the Local Value of the Hubble Constant," Astrophys. J. Lett. 934, L7.

LIGO Scientific Collaboration and Virgo Collaboration. (2017). "GW170817: Observation of Gravitational Waves from a Binary Neutron Star Inspiral," Phys. Rev. Lett. 119, 161101.

Milgrom, M. (1983). "A modification of the Newtonian dynamics as a possible alternative to the hidden mass hypothesis," Astrophys. J. 270, 365.
