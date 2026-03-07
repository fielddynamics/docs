# Rotation Curves & Effective Mass Decoded

Flat rotation curves are evidence of missing field topology, not missing mass. Select any of 175 galaxies below and see how the Gravity Field Dynamics scalar-tensor transition predicts each rotation curve from baryonic mass alone, with no free parameters, alongside MOND and $\Lambda$CDM.

<div class="rc-explorer" data-catalog-url="https://api.fielddynamics.org/v1/sparc/catalog" data-rc-url="https://api.fielddynamics.org/v1/analysis/rotation-curve/photometric" data-default-galaxy="NGC2998">

<div class="rc-controls">
<div class="rc-select-group">
<label class="rc-label" for="rc-galaxy-select">Galaxy</label>
<select id="rc-galaxy-select" class="rc-galaxy-select" disabled>
<option value="">Loading catalog...</option>
</select>
</div>
<span class="rc-time" style="color:#888;font-size:0.82rem;"></span>
</div>

<div class="rc-chart-area">
<div class="rc-chart-wrap" style="position:relative;height:380px;">
<canvas class="rc-main-canvas"></canvas>
</div>
<div class="rc-mass-wrap" style="position:relative;height:320px;margin-top:8px;">
<canvas class="rc-mass-canvas"></canvas>
</div>
</div>

</div>

Every galaxy spins. Stars and gas clouds orbit their galactic center at measurable speeds, and when we plot those speeds against distance from the center, we get what astronomers call a rotation curve. These curves are among the most powerful tools in astrophysics. They tell us how mass is distributed throughout a galaxy.

But there is a problem. When we add up all the visible matter (stars, gas, dust) and calculate how fast things should be orbiting, the numbers do not match. Stars at the outer edges of galaxies are moving far too fast for the visible matter to hold them in orbit. They should be flying off into intergalactic space, yet they are not.

For decades, the leading explanation has been dark matter: an invisible substance that provides the missing gravitational pull. But there is another possibility: that our understanding of gravity itself needs to evolve, particularly in the weak-field regime where these discrepancies appear.

**What the charts will show you is that we do not have a missing mass problem. We have a missing topology problem. The mass was never missing. The field equation was incomplete.** GFD completes it by deriving the gravitational response from the coupling structure of the stellated octahedron. No mass is added. The topology was always there. It just had not been read.

This interactive explorer lets you examine the question for yourself, galaxy by galaxy, across the full SPARC catalog of 175 galaxies with real observational data served live from the Field Dynamics API.

## How to read the rotation curve

The chart above plots observed velocity (white points with error bars) against radius in kiloparsecs. Overlaid are three colored curves, each representing a different gravitational framework's prediction for what the rotation curve should look like. All three take the same baryonic input (gas, stellar disk, and bulge) from SPARC 3.6 micron photometry and attempt to reproduce the observed curve.

**GFD** (green) is Gravity Field Dynamics. Its governing equation is the stellated octahedron field equation, $f(x) = (21x + 13) / (x + 1)$, from which the scalar-tensor transition $g_s = g_t^2 / (a_0 + g_t)$ is derived. The forward solver takes baryonic source acceleration in and total acceleration out via the exact quadratic inverse of the scalar-tensor transition. No interpolation function. No dark matter. No free parameters.

**MOND** (amber) is Modified Newtonian Dynamics. It applies the McGaugh interpolation function to modify Newtonian gravity in the low-acceleration regime. MOND is an empirical prescription: it fits the data well but does not derive its interpolation function from a deeper structure.

**CDM** (purple) is Cold Dark Matter ($\Lambda$CDM). It applies standard Newtonian gravity plus an NFW dark matter halo whose parameters are fit to match the observed velocities. The halo provides the additional gravitational pull needed to explain the flat outer rotation curve.

## The physical picture

Before interpreting the numbers, it helps to understand what the rotation curve is actually showing you physically.

A galaxy is a vortex. Not metaphorically, but structurally. Like water spiraling down a drain, a galaxy has both an interior and an exterior. The interior is the coupling throat of the gravitational field. The exterior is the observable disk where stars and gas orbit.

When the interior is quiet, the exterior rotation matches what the visible matter alone would produce. The effective mass equals the baryons. Everything looks Newtonian.

When the interior is active, it drives the exterior field beyond what the visible matter alone can sustain. Stars orbit faster than the baryons can explain. Not because there is hidden mass, but because the vortex interior is pumping energy into the exterior flow.

Think of ping pong balls floating in a water vortex. The balls follow the rotation faithfully. You can weigh them, measure their speed, and compute how much mass would be needed to produce that speed under ordinary conditions. But the answer will be too high, because the balls are not the source of the rotation. The drain is.

Postulating invisible ping pong balls to account for the anomalous motion misdiagnoses the system. The correct diagnostic is to measure the power differential between the field and its tracers.

In a galaxy, baryons play the role of the ping pong balls. The coupling throat plays the role of the drain. And the mass deficit $\Delta M_{\text{eff}}(r)$ measures the power output of the drain, not a shortfall of tracers.

The mass decoder returns the same equation in both regimes. When the interior is quiet, the effective mass matches the baryons. When the interior is active, the mass deficit reveals how much power the vortex interior is contributing to the exterior field. A small galaxy like CamB is not failing to account for its mass. It is a galaxy with a very active drain.

## Velocity decoded to effective mass

With the vortex picture in mind, the bar chart answers a straightforward question: how much mass does each framework need to explain what we observe?

At every observed radius, we can work backwards from the measured velocity to decode the dynamical mass enclosed within that radius. This decoded mass is computed directly from the kinematics using the GFD mass decoder:

$$M_{\text{dec}}(r) = \frac{r\,v^4}{G\,(a_0\,r + v^2)}$$

This decoded mass is derived from the observed kinematics and the GFD constitutive law. It represents what the rotation curve implies when gravity obeys the scalar-tensor transition rather than the Newtonian inverse-square law.

Each framework also has its own forward model that predicts how much enclosed mass there should be at a given radius. The bar chart shows the ratio of each framework's predicted mass to the decoded mass. A ratio of 1x means perfect agreement.

## What you will notice

**GFD derives its results from topology. MOND arrives at similar mass ratios empirically.** Despite producing different velocity curves, both frameworks converge on similar effective mass ratios at each radius. This convergence is significant. MOND was discovered in 1983 by fitting rotation curve data with no knowledge of the stellated octahedron or the coupling polynomial. The fact that an empirical prescription, found independently through decades of observational work, agrees with a topologically derived framework on the decoded mass is strong corroborating evidence. It suggests that modified gravity is capturing something real about the weak-field regime, and that GFD identifies the structural reason why.

The exact ratio depends on the galaxy. For large spirals it sits near 1x to 2x: the baryonic mass accounts for nearly all of the observed dynamics. For low-surface-brightness or dwarf galaxies like CamB, the ratio climbs to 50x or 80x. This does not indicate a failure. It reflects the deep-field regime where a small amount of baryonic matter drives a disproportionately large gravitational response. Recall the vortex analogy: a small drain can sustain a large rotation. The field is amplifying the baryonic source, not supplementing it with hidden mass.

**CDM sits far higher.** In CDM, gravity is Newtonian, so the only way to explain the observed velocities is to add invisible mass in the form of a dark matter halo surrounding the galaxy. The CDM bar therefore reflects the total enclosed mass (baryonic plus dark matter), which is necessarily larger than the baryonic decoded mass. For a galaxy like NGC2998, CDM may sit at 5x to 15x while GFD and MOND hover near 1x. For a dwarf galaxy like CamB, CDM can reach 800x or more while GFD and MOND sit at 50x to 80x. The gap between CDM and the modified gravity frameworks is always present, and it represents the dark matter halo that CDM requires.

For some dwarf galaxies where the best-fit NFW halo is poorly constrained, the API falls back to cosmological abundance matching to ensure CDM always produces a physically motivated prediction.

## Why this matters

Modified gravity and dark matter offer fundamentally different answers to the same question. Dark matter adds invisible mass to preserve Newtonian gravity. GFD changes the gravitational response by completing the field equation with the topology it was missing.

MOND demonstrated decades ago that the modified gravity approach works empirically. GFD explains why it works: the gravitational field couples through a stellated octahedron whose channel structure varies with acceleration. The constitutive law is not a fit. It is the topology's output.

The decoded mass provides a common anchor. Every bar on the chart is measured against it, making the comparison between frameworks honest and direct. When you select a galaxy and watch the three curves overlay the same observations, you are looking at one of the most consequential open questions in physics: is the universe filled with invisible matter, or does gravity itself have a richer topology than Newton imagined?
