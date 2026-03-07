# Cosmology

The cosmology endpoints return plot-ready data bundles for two established results where the GFD covariant completion matches published observational data. Each endpoint is a single GET call that returns observations, the GFD covariant result (derived from the SST action with zero free parameters), and comparison baselines.

## Tully-Fisher Velocity Evolution

**GET** `/v1/cosmology/tully-fisher`

Returns the GFD covariant result for how galaxy rotation velocities evolve with redshift, compared to IFU (Integral Field Unit) kinematic observations from six independent surveys and the LCDM baseline of no evolution. The relation $v(z)/v(0) = [H(z)/H_0]^{0.17}$ is derived from the scalar-tensor action of the GFD covariant completion with zero free parameters. The exponent 0.17 is not fitted to the data. All nine IFU measurements fall within the derived curve and its 6.2% topological measurement cage band.

```python
import requests

resp = requests.get(
    "https://api.fielddynamics.org/v1/cosmology/tully-fisher"
)
data = resp.json()

# data["observations"]          -> 9 IFU velocity ratio measurements
# data["sins_highlight"]        -> SINS BX442 galaxy at z=2.18 (+27%)
# data["gfd_curve"]["z"]        -> redshift array (SST covariant derived)
# data["gfd_curve"]["ratio"]    -> v(z)/v(0) from SST action
# data["gfd_curve"]["upper"]    -> upper band (6.2% cage)
# data["gfd_curve"]["lower"]    -> lower band (6.2% cage)
# data["lcdm_curve"]["ratio"]   -> LCDM baseline (flat at 1.0)
# data["theory"]["exponent"]    -> 0.17 (from SST action)
# data["cosmology"]             -> H0, omega_m, omega_l used
```

<div class="api-demo-section" data-endpoint="https://api.fielddynamics.org/v1/cosmology/tully-fisher" data-method="GET" data-chart-type="tully-fisher">
<div style="display:flex;align-items:center;gap:12px;margin:16px 0 12px 0;">
<button class="api-demo-run-btn" type="button">Run</button>
<span class="api-demo-time" style="color:#888;font-size:0.82rem;"></span>
</div>
<div class="api-demo-chart-wrap" style="position:relative;height:400px;margin-bottom:24px;display:none;">
<canvas class="api-demo-canvas"></canvas>
</div>
</div>

### Query parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `z_max` | float | 4.0 | Maximum redshift for the GFD curve (0.1 to 20) |
| `n_points` | int | 200 | Number of points in the GFD curve (10 to 2000) |
| `H0` | float | 70.0 | Hubble constant in km/s/Mpc (50 to 100) |
| `omega_m` | float | 0.30 | Matter density parameter (0.01 to 0.99) |

### Response fields

| Field | Description |
|-------|-------------|
| `observations[]` | Array of 9 IFU velocity ratio measurements |
| `observations[].z` | Redshift of the observation |
| `observations[].ratio` | Measured velocity ratio v(z)/v(0) |
| `observations[].err` | Measurement uncertainty |
| `observations[].source` | Publication reference |
| `observations[].survey` | Survey name (DEEP2, IMAGES, KMOS3D, SINS, ZFIRE) |
| `observations[].instrument` | Instrument used |
| `observations[].telescope` | Telescope facility |
| `sins_highlight` | Single highlighted observation: SINS BX442 at z=2.18 |
| `gfd_curve.z` | Redshift array for the GFD covariant curve |
| `gfd_curve.ratio` | v(z)/v(0) values derived from the SST action |
| `gfd_curve.upper` | Upper bound of the 6.2% measurement cage |
| `gfd_curve.lower` | Lower bound of the 6.2% measurement cage |
| `lcdm_curve.z` | Redshift array for the LCDM baseline |
| `lcdm_curve.ratio` | LCDM prediction (constant 1.0, no evolution) |
| `theory.exponent` | Exponent 0.17, derived from the SST covariant action (not fitted) |
| `theory.equation` | Human-readable equation string |
| `theory.cage_pct` | Measurement cage percentage (6.2%) |
| `cosmology.H0` | Hubble constant used in the computation |
| `cosmology.omega_m` | Matter density parameter used |
| `cosmology.omega_l` | Dark energy density parameter used |

---

## Hubble Constant

**GET** `/v1/cosmology/hubble-constant`

Returns six independent measurements of the Hubble constant from different observational techniques (Planck CMB, BAO, GW170817 standard siren, TRGB, SH0ES Cepheids, megamaser distances) and the GFD geometric derivation (tree-level 70.21, one-loop 70.29 km/s/Mpc with a 6.2% band spanning 66.2 to 74.7). The GFD result follows from $H = 2\pi a_0 / (c \sqrt{k/\pi})$ with $k = 4$ and requires no fitted parameters. All six independent measurements fall within the GFD band.

```python
import requests

resp = requests.get(
    "https://api.fielddynamics.org/v1/cosmology/hubble-constant"
)
data = resp.json()

# data["measurements"]          -> 6 independent H0 measurements
# data["measurements"][0]["method"]  -> e.g. "Planck (CMB)"
# data["measurements"][0]["h0"]      -> e.g. 67.4
# data["measurements"][0]["err"]     -> e.g. 0.5
# data["gfd"]["tree_level"]     -> 70.21 km/s/Mpc
# data["gfd"]["one_loop"]       -> 70.29 km/s/Mpc
# data["gfd"]["band_low"]       -> 66.15 (lower bound of 6.2% band)
# data["gfd"]["band_high"]      -> 74.65 (upper bound of 6.2% band)
```

<div class="api-demo-section" data-endpoint="https://api.fielddynamics.org/v1/cosmology/hubble-constant" data-method="GET" data-chart-type="hubble-constant">
<div style="display:flex;align-items:center;gap:12px;margin:16px 0 12px 0;">
<button class="api-demo-run-btn" type="button">Run</button>
<span class="api-demo-time" style="color:#888;font-size:0.82rem;"></span>
</div>
<div class="api-demo-chart-wrap" style="position:relative;height:360px;margin-bottom:24px;display:none;">
<canvas class="api-demo-canvas"></canvas>
</div>
</div>

### Response fields

| Field | Description |
|-------|-------------|
| `measurements[]` | Array of 6 independent H0 measurements |
| `measurements[].method` | Measurement technique name |
| `measurements[].h0` | Measured Hubble constant (km/s/Mpc) |
| `measurements[].err` | Symmetric error (when available) |
| `measurements[].err_low` | Lower asymmetric error (when available) |
| `measurements[].err_high` | Upper asymmetric error (when available) |
| `measurements[].ref` | Publication reference |
| `measurements[].year` | Publication year |
| `measurements[].survey` | Survey or collaboration name |
| `measurements[].instrument` | Instrument used |
| `measurements[].telescope` | Telescope facility |
| `measurements[].color` | Suggested plot color for this measurement |
| `gfd.tree_level` | GFD tree-level H0 derivation (70.21 km/s/Mpc) |
| `gfd.one_loop` | GFD one-loop H0 derivation (70.29 km/s/Mpc) |
| `gfd.range_pct` | Measurement cage range (6.2%) |
| `gfd.band_low` | Lower bound of the GFD derived band |
| `gfd.band_high` | Upper bound of the GFD derived band |
| `gfd.equation` | Human-readable equation string |
| `gfd.a0` | Acceleration scale used (1.2e-10 m/s^2) |
| `gfd.k` | Topological parameter (k=4) |
