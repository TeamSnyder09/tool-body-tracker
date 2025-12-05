# Installation Guide

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/TeamSnyder09/tool-body-tracker.git
cd tool-body-tracker
```

### 2. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Required Packages

- **Click** (8.1.7) - Command-line interface framework
- **Tabulate** (0.9.0) - Table formatting for output

### 3. Verify Installation

Run the help command to verify the installation:

```bash
python -m src.cli --help
```

You should see output listing all available commands.

## Optional: Installation with Setup.py

If you want to install as a package:

```bash
pip install -e .
```

This will install the tool globally as `tool-tracker` command.

## Troubleshooting

### Python not found
Ensure Python 3.8+ is installed and in your PATH.

### Import errors
Make sure you're in the correct directory and all dependencies are installed:
```bash
pip install -r requirements.txt --upgrade
```

### Database errors
The database will be created automatically on first run. Ensure the directory is writable.

## Uninstall

To uninstall:

```bash
pip uninstall tool-body-tracker
```

And remove the project directory.
