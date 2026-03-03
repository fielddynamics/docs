# Field Dynamics Documentation

Framework first documentation suite for Gravity Field Dynamics.

## How to Cite

Use the repository citation for now.

Primary citation target:

1. This documentation and software repository, for framework implementation details and version specific behavior.

If you publish related work before journal papers exist, cite in this order:

1. Public preprint or manuscript record, if available.
2. Repository citation from `CITATION.cff` with version and access date.

Example text:

```text
Framework implementation details and versioned documentation are cited from the Field Dynamics Documentation repository.
```

## Repository Purpose

This repository serves the documentation app and framework content for Field Dynamics.

## Local Run

```bash
pip install -r requirements.txt
python app.py
```

Then open:

- `http://localhost:5000/`
- `http://localhost:5000/framework/`

## Main Structure

- `framework/` content tree used by the framework navigator
- `sparc/` preserved SPARC data folder
- `templates/` Jinja templates for the docs UI
- `static/` styles and static assets
- `app.py` Flask entrypoint

## Citation Files

- `CITATION.cff` machine readable citation metadata for GitHub and reference tools.

## License

See `LICENSE` for terms.
