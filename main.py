import os
import shutil


def add_subfolder():
    # TODO: add subfolders based on file extensions
    pass


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
