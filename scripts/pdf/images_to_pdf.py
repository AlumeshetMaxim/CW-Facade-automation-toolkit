"""Convert a folder of images into one multi-page PDF."""

from pathlib import Path

from PIL import Image

IMAGES_DIR = Path("./examples/images")
OUTPUT_PDF = Path("./reports/images_merged.pdf")
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".tif", ".tiff"}


def main() -> None:
    if not IMAGES_DIR.exists():
        raise FileNotFoundError(f"Images folder not found: {IMAGES_DIR}")

    files = sorted(path for path in IMAGES_DIR.iterdir() if path.suffix.lower() in IMAGE_EXTENSIONS)
    if not files:
        raise RuntimeError(f"No images found in {IMAGES_DIR}")

    OUTPUT_PDF.parent.mkdir(parents=True, exist_ok=True)
    images = []
    for path in files:
        image = Image.open(path)
        if image.mode != "RGB":
            image = image.convert("RGB")
        images.append(image)

    first, rest = images[0], images[1:]
    first.save(OUTPUT_PDF, save_all=True, append_images=rest)
    print(f"Created: {OUTPUT_PDF}")


if __name__ == "__main__":
    main()
