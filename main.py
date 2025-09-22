import os
import shutil
import sys


def process(path, key, filename):
    if not os.path.exists(os.path.join(path, key.title())):
        os.makedirs(os.path.join(path, key.title()))
    source = os.path.join(path, filename)
    destination = os.path.join(path, key.title(), filename)
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
                    process(path, key, filename)
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

    if len(sys.argv) < 4:
        print("Usage: yeet <path> <type>")
        print(f"Available types: {', '.join(yeet_types)}")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd.lower() != "yeet":
        print("Error: first argument must be 'yeet'")
        print("Usage: yeet <path> <type>")
        sys.exit(1)

    path = sys.argv[2]
    if not os.path.exists(path) and os.path.isdir(path):
        print(f"Error: '{path}' is not a valid directory")
        print("Usage: yeet <path> <type>")
        sys.exit(1)

    yeet_type = " ".join(sys.argv[3:]).lower()
    if yeet_type not in yeet_types:
        print(f"Error: invalid type '{yeet_type}'")
        print(f"Available types: {', '.join(yeet_types)}")
        sys.exit(1)
    organize(path, yeet_type)
    sys.exit(0)
