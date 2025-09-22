# Yeet File Organizer

A simple Python CLI tool to sort files into categorized folders based on file type.

## Motivation

My friend and I had really messy Download folders, so I built this tool to automatically organize them.  
It's flexible enough to work with **any folder** you specify by passing its path as an argument.

## Features

- Automatically sorts files into folders like **Images**, **Music**, **Videos**, etc.
- Supports both a specific type (e.g., `images`) or **all** types at once.
- Cross-platform support (Windows & Linux).
- GUI interface for easy folder selection and filetype filtering.

## Running GUI via script

1. Clone this repository:

```bash
git clone -b yeet-gui https://github.com/TheMasshiro/yeet-organizer.git
cd yeet-organizer
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the GUI

```bash
python app.py
```

## Build with Pyinstaller

Package the GUI app into a standalone executable:

```bash
pyinstaller --noconsole --icon assets/icon.ico --add-data "assets/*;assets" app.py
```

The executable will appear in the **dist** folder.

## Contributing

Feel free to open an issue or submit a pull request if you have suggestions for improvements.

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

## Todos

- [ ] Add subfolders inside each folder with specific file extensions
- [ ] Improve overall GUI
