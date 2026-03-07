# Galaxy Catalog

The SPARC data endpoints provide access to the full catalog of 175 galaxies from the Spitzer Photometry and Accurate Rotation Curves database (Lelli, McGaugh, Schombert 2016).

## Single Galaxy

**GET** `/v1/sparc/{name}`

Returns the full rotation curve data and metadata for a single galaxy. This is the primary data retrieval endpoint: pass a galaxy name and receive all tabulated columns from the SPARC database.

```python
import requests

resp = requests.get(
    "https://api.fielddynamics.org/v1/sparc/NGC3198"
)
galaxy = resp.json()

# galaxy["name"]                    -> "NGC3198"
# galaxy["distance_mpc"]            -> 13.8
# galaxy["luminosity_3_6um"]        -> 38.279
# galaxy["disk_scale_length_kpc"]   -> 3.14
# galaxy["data"]["radius_kpc"]      -> [0.32, 0.64, ...]
# galaxy["data"]["v_obs_km_s"]      -> [51.0, 84.0, ...]
```

<div class="api-demo-section api-demo-catalog" data-endpoint="https://api.fielddynamics.org/v1/sparc/NGC3198" data-method="GET">
<div style="display:flex;align-items:center;gap:12px;margin:16px 0 12px 0;">
<button class="api-demo-run-btn" type="button">Run</button>
<span class="api-demo-time" style="color:#888;font-size:0.82rem;"></span>
</div>
<div class="api-demo-table-wrap" style="display:none;margin-bottom:24px;">
<h4 class="api-demo-table-title" style="color:#e8e8e8;font-size:0.95rem;margin:0 0 8px 0;"></h4>
<table class="api-demo-meta-table" style="margin-bottom:16px;">
<thead><tr></tr></thead>
<tbody><tr></tr></tbody>
</table>
<div class="api-demo-data-scroll" style="max-height:400px;overflow-y:auto;border:1px solid #333;border-radius:6px;">
<table class="api-demo-data-table">
<thead><tr></tr></thead>
<tbody></tbody>
</table>
</div>
</div>
</div>

### Response fields

| Field | Description |
|-------|-------------|
| `name` | Galaxy identifier |
| `distance_mpc` | Distance in megaparsecs |
| `inclination_deg` | Disk inclination angle |
| `luminosity_3_6um` | Spitzer 3.6 micron luminosity (10^9 L_sun) |
| `disk_scale_length_kpc` | Exponential disk scale length |
| `hi_mass_1e9_msun` | Neutral hydrogen mass (10^9 M_sun) |
| `quality` | Data quality flag (1 = best) |
| `points` | Number of rotation curve measurements |
| `data.radius_kpc` | Galactocentric radii |
| `data.v_obs_km_s` | Observed circular velocities |
| `data.e_v_obs_km_s` | Velocity measurement errors |
| `data.v_gas_km_s` | Gas contribution to rotation curve |
| `data.v_disk_km_s` | Disk contribution to rotation curve |
| `data.v_bul_km_s` | Bulge contribution to rotation curve |

## Catalog

**GET** `/v1/sparc/catalog`

Returns summary metadata for all 175 galaxies. Use this to browse the database or filter by quality or Hubble type before fetching individual galaxies.

```python
import requests

resp = requests.get(
    "https://api.fielddynamics.org/v1/sparc/catalog"
)
catalog = resp.json()

# catalog["galaxies"]  -> list of 175 galaxy metadata objects
# catalog["count"]     -> 175
```

### Optional query parameters

| Parameter | Description |
|-----------|-------------|
| `quality` | Filter by quality flag (1, 2, or 3) |
| `hubble_type` | Filter by Hubble type code |
