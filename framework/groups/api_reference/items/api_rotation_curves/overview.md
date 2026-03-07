# Rotation Curves

The rotation curve endpoints compute predicted circular velocities for a named SPARC galaxy under one or more gravitational frameworks. Two methods are available, each as its own route.

## Photometric

**POST** `/v1/analysis/rotation-curve/photometric`

Uses SPARC tabulated velocity columns (`v_gas`, `v_disk`, `v_bul`) derived from deprojected surface brightness imaging. One data point per observed radius. No analytic function assumed. The word "photometric" refers to the origin of the mass model: light measurement.

```python
import requests

resp = requests.post(
    "https://api.fielddynamics.org/v1/analysis/rotation-curve/photometric",
    json={
        "galaxy_name": "NGC3198",
        "frameworks": ["gfd"]
    }
)
data = resp.json()

# data["observed"]["radius_kpc"]       -> observed radii
# data["observed"]["v_obs_km_s"]       -> observed velocities
# data["results"][0]["v_predicted_km_s"] -> GFD prediction
# data["decode"]["m_decoded_msun"]     -> decoded baryonic mass
```

<div class="api-demo-section" data-endpoint="https://api.fielddynamics.org/v1/analysis/rotation-curve/photometric" data-body='{"galaxy_name":"NGC3198","frameworks":["gfd"]}'>
<div style="display:flex;align-items:center;gap:12px;margin:16px 0 12px 0;">
<button class="api-demo-run-btn" type="button">Run</button>
<span class="api-demo-time" style="color:#888;font-size:0.82rem;"></span>
</div>
<div class="api-demo-chart-wrap" style="position:relative;height:340px;margin-bottom:24px;display:none;">
<canvas class="api-demo-canvas"></canvas>
</div>
</div>

| Response field | Description |
|-------|-------------|
| `observed.radius_kpc` | Observed radii from SPARC (N points) |
| `observed.v_obs_km_s` | Observed circular velocities |
| `observed.e_v_obs_km_s` | Velocity measurement errors |
| `results[].framework` | Framework name (`gfd`, `mond`, `newtonian`, `cdm`) |
| `results[].radius_kpc` | Radii for predicted curve (same as observed) |
| `results[].v_predicted_km_s` | Framework velocity prediction |
| `results[].residuals.per_point_km_s` | Per-point velocity residuals |
| `results[].residuals.rms_km_s` | RMS of velocity residuals |
| `decode.v_obs_smooth_km_s` | Observed velocities after 6.2% Gaussian smoothing |
| `decode.m_decoded_msun` | Enclosed baryonic mass decoded via GFD inverse |
| `decode.residuals[]` | Per-framework mass residuals (M_decoded minus M_forward) |

## Parametric

**POST** `/v1/analysis/rotation-curve/parametric`

Uses analytic functional forms (Hernquist bulge, exponential disk, exponential gas) with parameters derived from SPARC catalog metadata. Smooth by construction. Evaluated on a 500-point grid. The word "parametric" refers to the method: the mass model is an analytic function whose parameters are derived from catalog scalars.

```python
import requests

resp = requests.post(
    "https://api.fielddynamics.org/v1/analysis/rotation-curve/parametric",
    json={
        "galaxy_name": "NGC3198",
        "frameworks": ["gfd"]
    }
)
data = resp.json()

# data["results"][0]["radius_kpc"]      -> 500-point fine grid
# data["results"][0]["v_predicted_km_s"] -> GFD prediction on fine grid
# data["baryonic"]["mass_model"]        -> derived model parameters
```

<div class="api-demo-section" data-endpoint="https://api.fielddynamics.org/v1/analysis/rotation-curve/parametric" data-body='{"galaxy_name":"NGC3198","frameworks":["gfd"]}'>
<div style="display:flex;align-items:center;gap:12px;margin:16px 0 12px 0;">
<button class="api-demo-run-btn" type="button">Run</button>
<span class="api-demo-time" style="color:#888;font-size:0.82rem;"></span>
</div>
<div class="api-demo-chart-wrap" style="position:relative;height:340px;margin-bottom:24px;display:none;">
<canvas class="api-demo-canvas"></canvas>
</div>
</div>

| Response field | Description |
|-------|-------------|
| `results[].radius_kpc` | 500-point fine radial grid |
| `results[].v_predicted_km_s` | Smooth framework prediction |
| `results[].v_newtonian_km_s` | Newtonian (baryonic only) velocity on fine grid |
| `results[].residuals.per_point_km_s` | Residuals interpolated to observed radii |
| `baryonic.mass_model` | Derived parametric model (disk, gas, bulge masses and scale radii) |
| `decode` | Same decode block as photometric (always included) |
