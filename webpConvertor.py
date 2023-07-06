from pathlib import Path
from PIL import Image
import json

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


class pathListClass:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


# creating list of path
pathList = []


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
    pathList.append(pathListClass(str(source), str(destination)))

    return destination


def main():
    for path in paths:
        webp_path = convert_to_webp_with_compression(path)
        print(webp_path)

    # Accessing object value using a for loop
    for obj in pathList:
        print({"src": obj.source, "dest": obj.destination})

    with open("path.json", "w", encoding="utf-8") as f:
        json.dump([ob.__dict__ for ob in pathList], f, ensure_ascii=False, indent=4)


main()
