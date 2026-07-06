# Script Catalog

This catalog describes the public, sanitized automation scripts in this repository.

The original internal scripts were created for real facade, curtain wall and CAD/BIM workflows. For this public repository, company paths, project folders and confidential project data are removed or replaced with generic placeholders.

## CAD / BricsCAD / AutoCAD automation

| Script | Purpose |
|---|---|
| `scripts/cad/setup_layouts_by_frame.py` | Detects drawing frames in layouts and applies print/window settings. |
| `scripts/cad/auto_publish_active_dwg_hidden.py` | Publishes the active DWG using a hidden CAD instance so the user can keep working. |
| `scripts/cad/draw_glass_with_insert_pads.py` | Draws glass rectangles and insert/pad positions from Excel/CSV input. |
| `scripts/cad/publish_dwgs_to_pdf_and_merge.py` | Batch-publishes DWG files to PDF and optionally merges results. |
| `scripts/cad/mtext_to_text.py` | Converts MTEXT objects into plain TEXT entities while cleaning formatting codes. |
| `scripts/cad/export_selected_text_count_to_excel.py` | Exports selected TEXT/MTEXT values to Excel with counts. |
| `scripts/cad/publish_layouts_one_click.py` | Publishes all layouts of the current DWG to individual PDFs. |
| `scripts/cad/apply_standard_page_setup.py` | Creates and applies a standard Page Setup to all layouts. |
| `scripts/cad/move_layouts_to_model.py` | Copies paper-space layout content back into Model Space. |

## DWG extraction / quantity workflows

| Script | Purpose |
|---|---|
| `scripts/dwg/count_units_from_floor_plans.py` | Counts unit names from floor-plan DWGs and exports summary data. |
| `scripts/dwg/count_mullions_by_floor.py` | Counts selected facade/mullion block types by floor. |
| `scripts/dwg/extract_blocks_summary.py` | Extracts block occurrences from DWGs and creates a summary table. |

## PDF workflows

| Script | Purpose |
|---|---|
| `scripts/pdf/split_pdf_by_page_groups.py` | Splits a PDF into files with a fixed number of pages per output file. |
| `scripts/pdf/merge_first_pages_from_floor_plans.py` | Merges the first page from each floor-plan PDF into one package. |
| `scripts/pdf/merge_pdf_from_quantity_table.py` | Builds a merged PDF based on a quantity/id table. |
| `scripts/pdf/split_pdf_to_single_pages.py` | Splits a PDF into one file per page. |
| `scripts/pdf/pdf_to_jpeg.py` | Converts PDF pages to high-quality JPEG images. |
| `scripts/pdf/images_to_pdf.py` | Converts JPEG/PNG/TIFF images into a multi-page PDF. |
| `scripts/pdf/remove_pdf_comments.py` | Removes PDF annotations/comments from a drawing package. |

## Athena / profile extraction

| Script | Purpose |
|---|---|
| `scripts/athena/extract_profiles_joining_elements.py` | Experimental Athena/CAD automation for extracting or placing profile/joining-element data. |

## STEP / annotation checking

| Script | Purpose |
|---|---|
| `scripts/check_step_annotations.py` | Checks STEP files for PMI/annotation entities and text-height consistency. |

## Safety rules

- Do not commit real project DWGs, PDFs, STEP files, client documents or internal production files.
- Keep examples generic and non-confidential.
- Replace company/project paths with `./examples`, `./input` or `./reports`.
- Use simplified sample data when demonstrating workflows.
