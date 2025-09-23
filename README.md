# Yeet File Organizer

A simple Python CLI tool to sort files into categorized folders based on file type.

## Motivation

My friend and I had really messy Download folders, so I built this tool to automatically organize them.  
It's flexible enough to work with **any folder** you specify by passing its path as an argument.

## Features

- Automatically sorts files into folders like **Images**, **Music**, **Videos**, etc.
- Supports both a specific type (e.g., `images`) or **all** types at once.
- Cross-platform support (Windows & Linux).

## Installation

1. Clone this repository:

```bash
git clone https://github.com/TheMasshiro/yeet-organizer.git
cd yeet-organizer
```

2. Run the script:

```bash
python main.py <path_to_folder> <type>
```

Example:

```bash
python main.py C:/Users/John/Downloads images
python main.py /home/john/Downloads all
```

## Contributing

Feel free to open an issue or submit a pull request if you have suggestions for improvements.

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

## Todos

- [x] ~~Add subfolder inside each folder with specific file extensions~~
- [x] ~~Create a GUI app~~
