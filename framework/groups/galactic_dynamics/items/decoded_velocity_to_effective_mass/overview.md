# Decoded Velocity to Effective Mass

Interactive viewer for the GFD inverse mass decode pipeline.

The decode takes observed circular velocities and, using only the GFD interpolating function and Newton's constants, algebraically extracts the enclosed baryonic mass at each radius. No mass model is assumed, iterated, or optimised. The result can then be compared against independent photometric baryonic mass estimates.

## Pipeline

1. Observed velocities are smoothed with 6.2% Gaussian diffraction
2. The smoothed curve is interpolated onto a 500-point fine grid
3. The GFD interpolating function mu(x) = x/(x+1) is algebraically inverted
4. Decoded mass is interpolated back to observed radii

## Features

- Galaxy selector across the full SPARC catalog
- Decoded mass vs forward baryonic mass comparison
- Per-framework mass residuals (M_decoded - M_forward)
- Surface density and acceleration ratio profiles

## Scientific context

The decoded mass is the physical output of the inverse pipeline. If GFD correctly describes the gravitational dynamics, the decoded mass at each radius should match the baryonic mass inferred from photometry. The velocity match is by construction and is not the claim; the science is in the mass comparison.
