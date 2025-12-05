import shutil
import sys
from pathlib import Path


def copy_files_to_extension_dirs(input_directory: Path, output_directory: Path) -> None:
    """
    Recursively copies files to subdirectories grouped by file extension.

    Args:
        input_directory: Source directory path.
        output_directory: Destination directory path.
    """
    try:
        current_dir_list = list(input_directory.iterdir())
    except PermissionError:
        print(f"Permission Denied for directory: {input_directory}")
        return

    for item in current_dir_list:
        if item.is_dir():
            # Recurse into subdirectories
            copy_files_to_extension_dirs(item, output_directory)
            continue

        # Get file extension or use 'no_extension'
        file_extension = item.suffix.lstrip(".").lower()
        if not file_extension:
            # Handle files without extension
            file_extension = "no_extension"

        ext_dir = output_directory / file_extension
        if not ext_dir.exists():
            ext_dir.mkdir()

        try:
            shutil.copy2(item, ext_dir / item.name)
        except PermissionError:
            print(f"Permission Denied for file: {item}")


if __name__ == "__main__":
    # Parse command-line arguments
    try:
        in_dir, out_dir = sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "dist"
    except IndexError:
        print("Usage: python task1.py <in_dir> [out_dir]")
        sys.exit(1)

    in_path_obj = Path(in_dir)
    if not in_path_obj.exists() or not in_path_obj.is_dir():
        print(
            f"Error: Input directory '{in_dir}' does not exist or is not a directory."
        )
        sys.exit(1)

    out_path_obj = Path(out_dir)
    if not out_path_obj.exists():
        out_path_obj.mkdir(parents=True)

    if not out_path_obj.is_dir():
        print(f"Error: Output path '{out_dir}' is not a directory.")
        sys.exit(1)

    # Verify output directory is empty
    if list(out_path_obj.iterdir()):
        print(f"Error: Output directory '{out_dir}' is not empty.")
        sys.exit(1)

    copy_files_to_extension_dirs(in_path_obj, out_path_obj)
