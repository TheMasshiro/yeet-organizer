import os
import shutil
from datetime import datetime


def create_logs(path, key, extension, filename):
    project_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_path = os.path.join(project_directory, "yeet.log")

    if not os.path.exists(log_path):
        with open(log_path, "w") as f:
            f.write("=== Yeet File Organizer Log ===\n\n")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = (
        f"[{timestamp}] "
        f"directory: {path}, type: {key}, extension: {extension}, filename: {filename}\n"
    )

    with open(log_path, "a") as f:
        f.write(log_entry)


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
                    create_logs(path, key, value, filename)
                    break
