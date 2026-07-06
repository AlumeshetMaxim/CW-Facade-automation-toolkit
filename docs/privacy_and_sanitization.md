# Privacy and Sanitization Policy

This repository is public and must contain only non-confidential examples.

## Do not commit

- Real client DWG, PDF, STEP, IFC, Excel or fabrication files.
- Internal project folders or network paths.
- Customer names, addresses, contract data or commercial information.
- Real production package data.
- Company-specific credentials, tokens or API keys.
- Any file that belongs to a private construction project unless it was explicitly approved for public release.

## Allowed public content

- Generic Python automation scripts.
- Simplified examples with fake or sample data.
- Documentation explaining workflows in a general way.
- Public helper functions for CAD, PDF, Excel and MTO automation.
- Generic screenshots only if they do not expose project/client data.

## Sanitization rules

Before committing a script:

1. Replace hard-coded project paths with generic placeholders.
2. Replace real customer/project names with `Example Project` or `Sample Project`.
3. Move configurable values into constants, command-line arguments or config files.
4. Keep only general workflow logic.
5. Test that no real paths remain in the file.

## Recommended folder placeholders

```text
./input
./examples
./reports
./output
```

## Purpose

The purpose of this repository is to show practical automation methods for facade, curtain wall and construction workflows while keeping private company and project information protected.
