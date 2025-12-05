# Usage Guide

## Command Reference

### Add Installation Record

Add a new tool installation record to the database.

```bash
python -m src.cli add [OPTIONS]
```

**Options:**

| Option | Required | Description |
|--------|----------|-------------|
| `--machine TEXT` | Yes | Machine name |
| `--tool TEXT` | Yes | Tool name |
| `--installed-date TEXT` | Yes | Installation date (YYYY-MM-DD) |
| `--installation-time TEXT` | No | Installation time (HH:MM:SS) |
| `--tool-type TEXT` | No | Tool type/category |
| `--notes TEXT` | No | Additional notes or comments |

**Example:**

```bash
python -m src.cli add \
  --machine "CNC-Machine-01" \
  --tool "Cutting-Tool-A" \
  --installed-date "2025-12-05" \
  --installation-time "09:30:00" \
  --tool-type "End-Mill" \
  --notes "High-speed steel tool for aluminum"
```

### List Records

Display installation records with optional filtering.

```bash
python -m src.cli list [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--machine TEXT` | Filter by machine name |
| `--tool TEXT` | Filter by tool name |
| `--limit INTEGER` | Limit number of records displayed |

**Examples:**

```bash
# Show all records
python -m src.cli list

# Show records for specific machine
python -m src.cli list --machine "CNC-Machine-01"

# Show records for specific tool
python -m src.cli list --tool "Cutting-Tool-A"

# Show first 10 records
python -m src.cli list --limit 10
```

### Search Records

Search for installation records by keyword.

```bash
python -m src.cli search --query TEXT
```

**Example:**

```bash
python -m src.cli search --query "Cutting-Tool"
```

### View Statistics

Display statistics about tool installations.

```bash
python -m src.cli stats
```

**Output includes:**

- Total installation records
- Total number of machines
- Total number of tools
- Number of tools per machine

**Example:**

```bash
$ python -m src.cli stats

==================================================
TOOL INSTALLATION STATISTICS
==================================================
Total Installation Records: 15
Total Machines: 3
Total Tools: 5

Tools per Machine:
--------------------------------------------------
  CNC-Machine-01: 5 tool(s)
  CNC-Machine-02: 6 tool(s)
  Lathe-01: 4 tool(s)
```

### List Machines

Display all machines or details for a specific machine.

```bash
python -m src.cli machines [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--machine TEXT` | Filter by specific machine name |

**Examples:**

```bash
# Show all machines
python -m src.cli machines

# Show details for specific machine
python -m src.cli machines --machine "CNC-Machine-01"
```

### List Tools

Display all tools or details for a specific tool.

```bash
python -m src.cli tools [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--tool TEXT` | Filter by specific tool name |

**Examples:**

```bash
# Show all tools
python -m src.cli tools

# Show details for specific tool
python -m src.cli tools --tool "Cutting-Tool-A"
```

## Common Workflows

### Workflow 1: Track New Tool Installation

```bash
# Add new tool installation
python -m src.cli add \
  --machine "Machine-01" \
  --tool "New-Tool" \
  --installed-date "2025-12-05"

# Verify the record
python -m src.cli list --machine "Machine-01"
```

### Workflow 2: Generate Monthly Report

```bash
# View all records for a specific machine
python -m src.cli list --machine "Machine-01"

# Get installation statistics
python -m src.cli stats
```

### Workflow 3: Find Tool Deployments

```bash
# Search for all installations of a specific tool
python -m src.cli search --query "Tool-Name"

# Or list by tool
python -m src.cli list --tool "Tool-Name"
```

## Date and Time Formats

### Date Format (YYYY-MM-DD)

- `2025-12-05` - December 5, 2025
- `2025-01-15` - January 15, 2025

### Time Format (HH:MM:SS) - Optional

- `09:30:00` - 9:30 AM
- `14:45:30` - 2:45:30 PM
- `23:59:59` - 11:59:59 PM
