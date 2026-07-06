# CW Facade Automation Toolkit - Extended Overview

This repository is a public open-source foundation for facade, curtain wall, CAD, PDF, DWG, Excel, STEP, Rhino, Trimble, SolidWorks and construction-file automation workflows.

## Main areas

- CAD layout, page setup, selection and publishing workflows.
- PDF drawing package splitting, merging, text marking, page extraction and cleanup.
- DWG text, block and attribute extraction examples.
- MTO and BOM summary utilities.
- Revision comparison utilities.
- STEP/STP annotation checking and file existence checks.
- Excel schedule checking and cell highlighting workflows.
- File replacement, sorting and moving workflows.
- Rhino block counting and STEP-to-Make2D workflow templates.
- Trimble Connect model export workflow notes.
- SolidWorks sheet-metal DXF workflow notes.
- Athena/profile workflow notes.

## Documentation

- `docs/project_structure.md` - folder and naming structure.
- `docs/script_catalog.md` - catalog of scripts.
- `docs/roadmap.md` - project roadmap.
- `docs/privacy_and_sanitization.md` - public repository safety rules.
- `docs/codex_oss_application.md` - notes for the Codex OSS application.

## Quick start

```bash
pip install -r requirements.txt
python scripts/example_mto_from_csv.py
python scripts/example_revision_compare.py
```

## Purpose

The goal is to make practical automation more accessible to facade planners, engineers and CAD users, while keeping private project data outside the public repository.
