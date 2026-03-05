# Electron Spin

## Overview

The previous pages established that the stellated octahedron has two field chambers, eight faces, and four coupled faces where the chambers interpenetrate. The coupling polynomial $f(K,s) = 1 + sK + K^2$ evaluated at three structural states gives 21, 17, and 13, equally spaced by $K = 4$ coupling levels. This page shows that the same structure determines the intrinsic angular momentum of matter: electron spin $\hbar/2$.

No new ingredients are introduced. Everything that follows uses the stellated octahedron, the polynomial, and one fact from quantum mechanics: the quantum of angular momentum is $\hbar$.


## The Vortex Through the Throat

Picture the stellated octahedron not as a static crystal but as a dynamic flow. The gravitational field circulates through the structure like fluid through an hourglass. It flows through the four coupled faces at the centre, the throat, where the two chambers meet. This is the Field Origin, the single point of maximal symmetry where both field chambers are present simultaneously.

The coupling polynomial tracks this flow:

| Region | State $s$ | Polynomial | Value |
|---|---|---|---|
| TetA (our sector) | $s = +1$ | $1 + 4 + 16$ | 21 |
| Field Origin (throat) | $s = 0$ | $1 + 0 + 16$ | 17 |
| TetB (dual sector) | $s = -1$ | $1 - 4 + 16$ | 13 |

Three regions, three integers, equally spaced by $K = 4$:

$$
21 - 17 = 17 - 13 = K = 4
$$

The full vortex spans from 21 through 17 to 13 and back, a complete cycle through both chambers. Each transition crosses exactly four coupling levels, corresponding to the four coupled faces at the throat. The vortex passes through these four active channels on each half of its cycle.


## Two Polarisations, One Observed

The stellated octahedron has two field chambers: TetA and TetB. These are two orientations of the same structure, related by spatial inversion. In the language of field theory, they are two polarisations.

A complete vortex cycle traverses both polarisations. It flows from TetA through the coupled faces to TetB, and back again. The full cycle carries one quantum of angular momentum: $\hbar$.

But a massive particle does not have access to both polarisations. It exists within 3+1 spacetime. It occupies one sector. The ADM decomposition of general relativity (Arnowitt, Deser and Misner 1962) assigns the particle to one field chamber, one half of the structure. The other half is the dual sector: topologically required for consistency (ghost freedom demands it, spinor closure demands it, parity symmetry demands it), but not directly accessible from within the particle's own spacetime.

This is not a limitation of the theory. It is a consequence of what it means to be massive and localised. The gravitational field has two chambers. A massive particle couples to one.

Two polarisations exist. One is observed.


## The Derivation

A full vortex cycle through the stellated octahedron carries angular momentum $\hbar$. The cycle spans both field chambers: from $s = +1$ to $s = -1$ and back. The total span is $2K = 8$ coupling levels.

The observable half-cycle spans one chamber: from $s = +1$ (depth 21) to $s = 0$ (depth 17). This is $K = 4$ coupling levels out of $2K = 8$ total. The observable fraction is:

$$
\frac{K}{2K} = \frac{1}{2}
$$

A massive particle in 3+1 spacetime carries the angular momentum of the half-cycle it occupies:

$$
S = \frac{1}{2} \times \hbar = \frac{\hbar}{2}
$$

This is electron spin.

The factor of $1/2$ is not postulated. It is the ratio of the observable sector to the full vortex cycle, determined by the polynomial's structure and the 3+1 decomposition of spacetime.


## Why One Half and Not Some Other Fraction

The polynomial $f(K,s) = 1 + sK + K^2$ is symmetric about $s = 0$. The Field Origin sits exactly at the midpoint between the two sectors:

$$
\frac{f(K,+1) + f(K,-1)}{2} = \frac{21 + 13}{2} = 17 = f(K,0)
$$

This arithmetic mean lock is not a numerical coincidence. It holds for any polynomial of this form. The midpoint divides the structure into two exactly equal halves. There is no room for $1/3$ or $1/5$ or any other fraction. The symmetry of the polynomial forces the split to be $1/2$, and the split is what determines spin.

If the polynomial were asymmetric, if the three structural states were not equally spaced, the spin value would differ. But equal spacing is guaranteed by the polynomial's structure: the middle term $sK$ changes by $K$ when $s$ changes by 1. The spacing is $K$ in both directions. The halves are equal by algebra, not by choice.


## Comparison with Existing Approaches

The spin quantum number $\hbar/2$ has been established through three independent routes in the history of physics:

| Approach | How spin-1/2 arises |
|---|---|
| Pauli (1927) | Postulated to explain the Stern-Gerlach experiment (Stern and Gerlach 1922) |
| Dirac (1928) | Emerges from requiring simultaneous consistency of quantum mechanics and special relativity |
| This framework | Emerges from the vortex structure of the stellated octahedron: one observable polarisation of a two-polarisation topology |

Pauli postulated spin to fit data. Dirac derived it from mathematical consistency. This framework derives it from the geometry of gravitational field closure. Three different starting points arrive at the same value.

The distinction is in what the $1/2$ means. In Pauli's formulation, it is an empirical fact. In Dirac's, it is a consequence of the algebra of gamma matrices. Here, it is the observable fraction of a vortex cycle through a dual field chamber, the half of the hourglass that 3+1 spacetime has access to.


## What This Means

Spin-1/2 is not a property that particles happen to possess. It is a consequence of existing within one sector of a two-sector gravitational topology. The stellated octahedron has two field chambers. A full vortex cycle traverses both. A massive particle, bound to 3+1 spacetime, traverses one. Half the cycle, half the angular momentum.

The same integers that determine $K = 4$ and $D = 3$ determine the spin. The same polynomial that gives the coupling depth gives the spin fraction. No new parameters are introduced. The framework that derives $G$ from depth and $\alpha$ from breadth derives spin from the observable fraction of the vortex cycle.

One structure. Read in three directions. Three constants.


## References

Arnowitt, R., Deser, S. and Misner, C. W. (1962). "The dynamics of general relativity," in *Gravitation: An Introduction to Current Research*, Wiley.

Dirac, P. A. M. (1928). "The quantum theory of the electron," *Proc. R. Soc. Lond. A* 117, 610.

Pauli, W. (1927). "Zur Quantenmechanik des magnetischen Elektrons," *Z. Phys.* 43, 601.

Stern, O. and Gerlach, W. (1922). "Der experimentelle Nachweis der Richtungsquantelung im Magnetfeld," *Z. Phys.* 9, 349.
