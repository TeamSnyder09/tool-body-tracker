# API Reference

## Database Module

### ToolTrackerDB Class

Main database interface for tool tracking operations.

#### Constructor

```python
from src.database import ToolTrackerDB

db = ToolTrackerDB(db_path="tool_tracker.db")
```

**Parameters:**

- `db_path` (str, optional): Path to the SQLite database file. Default: "tool_tracker.db"

#### Methods

### Machine Operations

#### `add_machine(name: str) -> int`

Add a new machine to the database.

```python
machine_id = db.add_machine("CNC-Machine-01")
```

**Parameters:**
- `name` (str): Unique machine name

**Returns:** Machine ID

**Raises:** `ValueError` if machine already exists

#### `get_machine_id(name: str) -> Optional[int]`

Get machine ID by name.

```python
machine_id = db.get_machine_id("CNC-Machine-01")
```

**Parameters:**
- `name` (str): Machine name

**Returns:** Machine ID or None if not found

### Tool Operations

#### `add_tool(name: str, tool_type: str = None) -> int`

Add a new tool to the database.

```python
tool_id = db.add_tool("Cutting-Tool-A", "End-Mill")
```

**Parameters:**
- `name` (str): Unique tool name
- `tool_type` (str, optional): Tool type/category

**Returns:** Tool ID

**Raises:** `ValueError` if tool already exists

#### `get_tool_id(name: str) -> Optional[int]`

Get tool ID by name.

```python
tool_id = db.get_tool_id("Cutting-Tool-A")
```

**Parameters:**
- `name` (str): Tool name

**Returns:** Tool ID or None if not found

### Installation Operations

#### `add_installation(machine_name: str, tool_name: str, installed_date: str, installation_time: str = None, notes: str = None) -> int`

Add a tool installation record.

```python
record_id = db.add_installation(
    machine_name="CNC-Machine-01",
    tool_name="Cutting-Tool-A",
    installed_date="2025-12-05",
    installation_time="09:30:00",
    notes="High-speed steel tool"
)
```

**Parameters:**
- `machine_name` (str): Name of the machine
- `tool_name` (str): Name of the tool
- `installed_date` (str): Installation date (YYYY-MM-DD)
- `installation_time` (str, optional): Installation time (HH:MM:SS)
- `notes` (str, optional): Additional notes

**Returns:** Record ID

**Raises:** `ValueError` if record already exists

#### `get_all_installations() -> List[Dict]`

Get all installation records.

```python
records = db.get_all_installations()
```

**Returns:** List of installation record dictionaries

#### `get_installations_by_machine(machine_name: str) -> List[Dict]`

Get all installations for a specific machine.

```python
records = db.get_installations_by_machine("CNC-Machine-01")
```

**Parameters:**
- `machine_name` (str): Machine name

**Returns:** List of installation record dictionaries

#### `get_installations_by_tool(tool_name: str) -> List[Dict]`

Get all installations of a specific tool.

```python
records = db.get_installations_by_tool("Cutting-Tool-A")
```

**Parameters:**
- `tool_name` (str): Tool name

**Returns:** List of installation record dictionaries

#### `search_installations(query: str) -> List[Dict]`

Search installation records by keyword.

```python
results = db.search_installations("Cutting")
```

**Parameters:**
- `query` (str): Search query

**Returns:** List of matching installation record dictionaries

### Statistics

#### `get_statistics() -> Dict`

Get statistics about tool installations.

```python
stats = db.get_statistics()
print(f"Total records: {stats['total_records']}")
print(f"Total machines: {stats['total_machines']}")
print(f"Total tools: {stats['total_tools']}")
```

**Returns:** Dictionary with statistics:
- `total_records` (int): Total installation records
- `total_machines` (int): Total number of machines
- `total_tools` (int): Total number of tools
- `tools_per_machine` (dict): Tools count per machine

## Utility Module

### validate_date(date_string: str) -> bool

Validate date format (YYYY-MM-DD).

```python
from src.utils import validate_date

is_valid = validate_date("2025-12-05")  # True
is_valid = validate_date("12/05/2025")  # False
```

### validate_time(time_string: str) -> bool

Validate time format (HH:MM:SS).

```python
from src.utils import validate_time

is_valid = validate_time("09:30:00")  # True
is_valid = validate_time("9:30 AM")   # False
```

### calculate_days_installed(installed_date: str, removal_date: str = None) -> int

Calculate days a tool was installed.

```python
from src.utils import calculate_days_installed

days = calculate_days_installed("2025-01-01", "2025-12-31")  # 364
days = calculate_days_installed("2025-12-05")  # Days until today
```

## Example Usage

```python
from src.database import ToolTrackerDB

# Initialize database
db = ToolTrackerDB()

# Add machines and tools
db.add_machine("CNC-01")
db.add_tool("Tool-A", "End-Mill")

# Record installation
record_id = db.add_installation(
    machine_name="CNC-01",
    tool_name="Tool-A",
    installed_date="2025-12-05",
    installation_time="09:00:00"
)

# Retrieve records
all_records = db.get_all_installations()
machine_records = db.get_installations_by_machine("CNC-01")

# Search
results = db.search_installations("Tool-A")

# Get statistics
stats = db.get_statistics()
print(f"Total machines: {stats['total_machines']}")
```
