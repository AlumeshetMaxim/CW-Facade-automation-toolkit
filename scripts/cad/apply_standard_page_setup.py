"""Template: apply a standard page setup to CAD layouts.

Use this as a public checklist for local AutoCAD/BricsCAD automation.
"""

PAGE_SETUP_NAME = "AUTO_EXTENTS_A3"
PLOTTER_NAME = "DWG To PDF.pc3"
STYLE_SHEET = "monochrome.ctb"


def main() -> None:
    print("Page setup:", PAGE_SETUP_NAME)
    print("Plotter:", PLOTTER_NAME)
    print("Style sheet:", STYLE_SHEET)
    print("Apply these values through your local CAD API.")


if __name__ == "__main__":
    main()
