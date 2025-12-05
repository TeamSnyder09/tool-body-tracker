# Tool Body Tracker

Welcome to **Tool Body Tracker** - a comprehensive CLI program to track tool body installation time on machines.

## Overview

Tool Body Tracker is designed to help you manage and monitor tool installations across multiple machines. It provides:

- **Database Storage** - SQLite database for reliable data persistence
- **CLI Interface** - Easy-to-use command-line commands
- **Search & Filter** - Find records by machine, tool, or date
- **Statistics** - Get insights on tool deployments
- **Validation** - Automatic date and time format validation

## Quick Start

### Installation

```bash
pip install -r requirements.txt
```

### Add a Tool Installation

```bash
python -m src.cli add \
  --machine "Machine-01" \
  --tool "Tool-A" \
  --installed-date "2025-12-05"
```

### View All Records

```bash
python -m src.cli list
```

### Get Statistics

```bash
python -m src.cli stats
```

## Features

✅ **Machine Management** - Track multiple machines  
✅ **Tool Registry** - Manage different tool types  
✅ **Installation Records** - Detailed history of installations  
✅ **Search & Filter** - Find records easily  
✅ **Statistics** - Generate deployment reports  

## Documentation

- [Installation Guide](installation.md) - Detailed setup instructions
- [Usage Guide](usage.md) - Command reference and examples
- [API Reference](api.md) - Python API documentation
- [Contributing](contributing.md) - How to contribute

## Project Info

- **Author**: Tool Tracking Team
- **License**: MIT
- **Repository**: [GitHub](https://github.com/TeamSnyder09/tool-body-tracker)
