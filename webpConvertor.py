from pathlib import Path
from PIL import Image

paths = []


def get_files(extensions):
    """Get all files with specified extensions.

    Args:
        extensions (tuple): Tuple of file extensions

    Returns:
        list: List of paths to files

    paths = []  # List of paths to files to return.

    # For each extension in the tuple,
    # get all files with that extension.
    # Append to list of paths.""

    """
    for ext in extensions:
        paths.extend(Path(".").glob(ext))
        print("path", paths)
    return paths


files = get_files(("**/*.png", "**/*.jpg", "**/*.jpeg"))


def convert_to_webp_with_compression(source):
    """Convert image to webp.

    Args:
        source (pathlib.Path): Path to source image

    Returns:
        pathlib.Path: path to new image
    """
    destination = source.with_suffix(".webp")
    image = Image.open(source)  # Open image
    image.save(
        destination, format="webp", optimize=True, quality=50
    )  # Convert image to webp with optimization

    return destination


def main():
    print(paths)
    for path in paths:
        webp_path = convert_to_webp_with_compression(path)
        print(webp_path)


main()
