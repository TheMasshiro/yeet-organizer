import os
import shutil
import sys


def process(path, key, extension, filename):
    full_path = os.path.join(path, key.title())
    extension_clean = extension.replace(".", "")

    if not filename.lower().endswith(extension):
        return

    if not os.path.exists(os.path.join(full_path, extension_clean)):
        os.makedirs(os.path.join(full_path, extension_clean))

    source = os.path.join(path, filename)
    destination = os.path.join(full_path, extension_clean, filename)
    shutil.move(source, destination)
    print(f"Moved {filename} -> {destination}")


def organize(path, yeet_type):
    path = os.path.abspath(path)

    filetypes = {
        "all": [],
        "archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "backups": [".iso", ".bak"],
        "code": [
            ".py",
            ".js",
            ".jsx",
            ".ts",
            ".tsx",
            ".html",
            ".css",
            ".c",
            ".cpp",
            ".java",
            ".cs",
            ".php",
            ".rb",
            ".go",
        ],
        "configs": [".ini", ".json", ".yaml", ".yml", ".xml", ".toml", ".config"],
        "databases": [".sqlite", ".sql", ".db", ".mdb"],
        "documents": [".pdf", ".docx", ".doc", ".odt"],
        "ebooks": [".epub", ".mobi", ".azw3"],
        "executables": [".exe", ".msi", ".sh", ".bat", ".bin", ".elf"],
        "fonts": [".ttf", ".otf", ".woff", ".woff2"],
        "images": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp", ".tiff", ".svg"],
        "installers": [".apk", ".pkg", ".deb", ".rpm"],
        "music": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"],
        "powerpoints": [".ppt", ".pptx", ".key", ".odp"],
        "publishers": [".pub"],
        "spreadsheets": [".xlsx", ".xls", ".ods", ".csv"],
        "subtitles": [".srt", ".vtt", ".ass"],
        "system files": [".dll", ".sys", ".drv"],
        "text files": [".txt", ".log", ".md"],
        "videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv"],
        "3d models": [".stl", ".obj", ".step", ".fbx", ".blend"],
    }

    for filename in os.listdir(path):
        for key, extensions in filetypes.items():
            if yeet_type != "all" and yeet_type != key:
                continue

            for value in extensions:
                if filename.lower().endswith(value):
                    process(path, key, value, filename)
                    break


if __name__ == "__main__":
    yeet_types = [
        "all",
        "archives",
        "backups",
        "code",
        "configs",
        "databases",
        "documents",
        "ebooks",
        "executables",
        "fonts",
        "images",
        "installers",
        "music",
        "powerpoints",
        "publishers",
        "spreadsheets",
        "subtitles",
        "system files",
        "text files",
        "videos",
        "3d models",
    ]

    cmd = sys.argv[1]
    if cmd.lower() != "yeet":
        print(
            """
Error:
    First argument must be 'yeet'

Tip:
    Use 'yeet -h' or 'yeet --help' for usage information
    """
        )
        sys.exit(1)

    if "-h" in sys.argv or "--help" in sys.argv:
        print(
            f"""
Yeet File Organizer
-------------------
Usage:
    yeet <path> <type>

Available types:
    {', '.join(yeet_types)}

Example:
    yeet C:/Users/John/Downloads images

Tip:
    You can use '-h' or '--help' anytime to see this message
    """
        )
        sys.exit(0)

    if len(sys.argv) < 4:
        print(
            f"""
Error:
    Missing path or type

Usage:
    yeet <path> <type>

Available types:
    {', '.join(yeet_types)}

Tip:
    Run 'yeet -h' or 'yeet --help' for more info
    """
        )
        sys.exit(1)

    path = sys.argv[2]
    if not os.path.exists(path) or not os.path.isdir(path):
        print(
            f"""
Error:
    '{path}' is not a valid directory

Tip:
    Run 'yeet -h' or 'yeet --help' for usage examples
    """
        )
        sys.exit(1)

    yeet_type = " ".join(sys.argv[3:]).lower()
    if yeet_type not in yeet_types:
        print(
            f"""
Error:
    Invalid type '{yeet_type}'

Available types:
    {', '.join(yeet_types)}

Tip:
    Run 'yeet -h' or 'yeet --help' for more info
    """
        )
        sys.exit(1)

    organize(path, yeet_type)
    sys.exit(0)
