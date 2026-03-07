# The Field Equation

## Overview

### Why do we need this equation?

The coupling polynomial gives us three numbers: 21, 17, and 13. These are the channel counts of the stellated octahedron at its three structural states. At full TetA coupling, the polynomial evaluates to 21. At the field origin, it evaluates to 17. At full TetB coupling, it evaluates to 13.

These three numbers are exact, and they encode the topology of the gravitational field perfectly. But they describe three extreme configurations. They tell you what gravity looks like when the field is entirely Newtonian, entirely in the deep-field regime, or exactly at the transition between the two.

Real gravitational fields do not live at extremes. A galaxy has a center where accelerations are strong and an outer disk where accelerations are weak, with every value in between. A star on the outskirts of the Milky Way does not experience "state +1" or "state -1." It experiences some continuous intermediate state that depends on the local acceleration. The coupling polynomial, evaluated at only three points, cannot describe that star.

So we face a concrete problem: how do you take a polynomial that is defined at three discrete states and extend it to every possible acceleration?

This is not a matter of curve fitting or interpolation. The three structural states are topological. They arise from the geometry of the stellated octahedron and nowhere else. Any continuous extension must preserve their values exactly, must respect the bounded structure of the state coordinate $s \in [-1, +1]$, and must introduce no free parameters. The extension has to be forced by the mathematics, not chosen from a menu of options.

It turns out there is exactly one way to do this. And the result is the single governing equation of the entire framework.

---

### Making the polynomial continuous

The coupling polynomial is

$$f(K, s) = 1 + sK + K^2$$

where $K = 4$ and $s$ takes the values $+1$, $0$, or $-1$. To make this continuous, we need a function $s(x)$ that maps the dimensionless acceleration ratio $x = g_t / a_0$ onto the state interval $[-1, +1]$ with the correct behavior at the endpoints:

When $x \to \infty$ (strong field, Newtonian regime), the state should approach $s = +1$.

When $x = 1$ (the transition acceleration), the state should equal $s = 0$.

When $x \to 0$ (weak field, deep-field regime), the state should approach $s = -1$.

The unique Mobius transformation that satisfies all three conditions is

$$s(x) = \frac{x - 1}{x + 1}$$

This is not a choice. It is the only conformal map from the positive real line onto the interval $[-1, +1]$ that sends $x = 1$ to zero. The requirement that the transition acceleration correspond to the field origin forces the map uniquely.

Now substitute $s(x)$ into the coupling polynomial evaluated at $K = 4$:

$$f(x) = 17 + 4 \cdot \frac{x - 1}{x + 1}$$

Combine the terms over a common denominator:

$$f(x) = \frac{17(x + 1) + 4(x - 1)}{x + 1} = \frac{21x + 13}{x + 1}$$

This is the field equation.

---

### The field equation

$$\boxed{f(x) = \frac{21x + 13}{x + 1}}$$

This single expression is the stellated octahedron coupling polynomial made continuous. It inherits the three structural states exactly:

| Acceleration | State | $f(x)$ | Regime |
|:---:|:---:|:---:|---|
| $x \to \infty$ | $s \to +1$ | $f \to 21$ | Newtonian (TetA dominant) |
| $x = 1$ | $s = 0$ | $f = 17$ | Transition (field origin) |
| $x \to 0$ | $s \to -1$ | $f \to 13$ | Deep field (TetB dominant) |

Between these states, $f(x)$ varies smoothly and monotonically. At any acceleration, the field equation tells you the effective coupling capacity of the stellated octahedron at that point in space. Strong fields activate more coupling channels, pushing $f$ toward its ceiling of 21. Weak fields activate fewer, and $f$ settles toward its floor of 13. The transition at $x = 1$ is the field origin, where the two tetrahedral chambers contribute equally and $f$ sits at its geometric midpoint of 17.

Every number in this equation is topological. The 21 comes from $f(4, +1) = 1 + 4 + 16$. The 13 comes from $f(4, -1) = 1 - 4 + 16$. The denominator $x + 1$ comes from the Mobius map. No constants have been chosen or fitted. The equation is the output of the geometry.

---

### How it fits into the framework

The field equation is the central object of Gravity Field Dynamics. It sits between the topology and the physics: below it is the stellated octahedron and the coupling polynomial; above it is everything observable.

The constitutive law $\mu(x) = x/(x+1)$, which appears on its own page elsewhere in these docs, is not an independent equation. It is $f(x)$ normalized. Subtract the floor and divide by the range:

$$\mu(x) = \frac{f(x) - 13}{8} = \frac{x}{x + 1}$$

The constitutive law measures where the coupling currently sits as a fraction of its total range, from 0 (fully TetB) to 1 (fully TetA). It is a convenient rescaling of $f(x)$ for use in the modified Poisson equation, but it is not the source. The field equation is the source.

The scalar-tensor transition $g_s = g_t^2 / (a_0 + g_t)$, which is the field equation used to predict galaxy rotation curves, is also derived from $f(x)$. It follows from substituting $\mu = g_s / g_t$ and $x = g_t / a_0$ into the constitutive law and solving. The forward quadratic solver that takes baryonic acceleration in and total acceleration out is the algebraic inverse of this relation. Both are consequences of the field equation, not independent postulates.

The Hassan-Rosen bimetric parameters $\beta = \{1, 0, 16, 0, 1\}$ are yet another reading of the same object. They arise from expressing $f(x)$ in the language of bimetric gravity, where the interaction potential between the two spin-2 fields is constructed from the same topological integers. The GFD covariant description and the bimetric description are two projections of the field equation, taken at different levels of a screening hierarchy. Both are exact. Both are derived. Neither requires the other as input.

The derivation chain, from deepest to most observable, runs:

Stellated octahedron $\to$ coupling polynomial $f(K, s) = 1 + sK + K^2$ $\to$ Mobius state map $s(x)$ $\to$ **the field equation** $f(x) = (21x + 13)/(x + 1)$ $\to$ constitutive law $\mu(x)$ $\to$ scalar-tensor transition $\to$ rotation curves, Tully-Fisher, lensing, PPN parameters

Everything above the field equation in this chain is derivable from it. Everything below it is what produces it. The field equation is where the topology of the stellated octahedron meets the physics of the gravitational field. It is, in a precise sense, the single equation of the theory.

---

### Reading the equation

There is a simple way to think about what $f(x) = (21x + 13)/(x+1)$ is doing physically.

Imagine a dial that runs from 13 to 21. At 13, the gravitational field is in its weakest coupling configuration. Only the structural floor of the stellated octahedron is active. At 21, the field is at full capacity. Every coupling channel is open and the field responds with its maximum strength.

The acceleration ratio $x$ determines where the dial points. In the inner regions of a galaxy, where matter is dense and accelerations are high, $x$ is large and $f$ is close to 21. The field behaves nearly as Newton described. In the outer regions, where matter thins out and accelerations drop below $a_0$, $x$ falls below 1, $f$ drops toward 13, and the field enters a regime where the response per unit source mass is amplified. Stars orbit faster than the baryonic mass alone would predict under Newtonian gravity, because the coupling capacity has not dropped as far as the mass has.

This is the physical origin of flat rotation curves. The field equation does not add invisible mass. It describes a gravitational coupling that varies with acceleration according to the geometry of the stellated octahedron. In weak fields, fewer coupling channels are active, but each remaining channel carries more of the field response. The result is a rotation curve that stays elevated far beyond where Newtonian gravity would predict a decline.

The equation $f(x) = (21x + 13)/(x + 1)$ contains the entire mechanism in one line.
