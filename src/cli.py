"""Command-line interface for tool tracking"""

import click
from tabulate import tabulate
from src.database import ToolTrackerDB
from src.utils import validate_date, validate_time, format_record

db = ToolTrackerDB()

@click.group()
def cli():
    """Tool Body Time Tracker - Track tool installations on machines"""
    pass

@cli.command()
@click.option('--machine', required=True, help='Machine name')
@click.option('--tool', required=True, help='Tool name')
@click.option('--installed-date', required=True, help='Installation date (YYYY-MM-DD)')
@click.option('--installation-time', default=None, help='Installation time (HH:MM:SS)')
@click.option('--tool-type', default=None, help='Tool type/category')
@click.option('--notes', default=None, help='Notes or comments')
def add(machine, tool, installed_date, installation_time, tool_type, notes):
    """Add a new tool installation record"""
    
    # Validate date
    if not validate_date(installed_date):
        click.echo("Error: Invalid date format. Use YYYY-MM-DD", err=True)
        return
    
    # Validate time if provided
    if installation_time and not validate_time(installation_time):
        click.echo("Error: Invalid time format. Use HH:MM:SS", err=True)
        return
    
    try:
        record_id = db.add_installation(
            machine_name=machine,
            tool_name=tool,
            installed_date=installed_date,
            installation_time=installation_time,
            notes=notes
        )
        click.echo(f"✓ Installation record added successfully (ID: {record_id})")
        click.echo(f"  Machine: {machine}")
        click.echo(f"  Tool: {tool}")
        click.echo(f"  Date: {installed_date}")
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)

@cli.command()
@click.option('--machine', default=None, help='Filter by machine name')
@click.option('--tool', default=None, help='Filter by tool name')
@click.option('--limit', type=int, default=None, help='Limit number of records')
def list(machine, tool, limit):
    """List all installation records"""
    
    if machine:
        records = db.get_installations_by_machine(machine)
    elif tool:
        records = db.get_installations_by_tool(tool)
    else:
        records = db.get_all_installations()
    
    if limit:
        records = records[:limit]
    
    if not records:
        click.echo("No records found")
        return
    
    # Format records for display
    headers = ['Machine', 'Tool', 'Tool Type', 'Installed Date', 'Time', 'Removal Date', 'Notes']
    rows = []
    for record in records:
        rows.append([
            record.get('machine', ''),
            record.get('tool', ''),
            record.get('tool_type', '') or '-',
            record.get('installed_date', ''),
            record.get('installation_time', '') or '-',
            record.get('removal_date', '') or '-',
            record.get('notes', '') or '-'
        ])
    
    click.echo(tabulate(rows, headers=headers, tablefmt='grid'))
    click.echo(f"\nTotal records: {len(records)}")

@cli.command()
@click.option('--query', required=True, help='Search query (machine, tool name, or notes)')
def search(query):
    """Search installation records"""
    
    records = db.search_installations(query)
    
    if not records:
        click.echo(f"No records found matching '{query}'")
        return
    
    headers = ['Machine', 'Tool', 'Tool Type', 'Installed Date', 'Time', 'Removal Date', 'Notes']
    rows = []
    for record in records:
        rows.append([
            record.get('machine', ''),
            record.get('tool', ''),
            record.get('tool_type', '') or '-',
            record.get('installed_date', ''),
            record.get('installation_time', '') or '-',
            record.get('removal_date', '') or '-',
            record.get('notes', '') or '-'
        ])
    
    click.echo(tabulate(rows, headers=headers, tablefmt='grid'))
    click.echo(f"\nFound {len(records)} matching record(s)")

@cli.command()
def stats():
    """Display statistics"""
    
    stats = db.get_statistics()
    
    click.echo("=" * 50)
    click.echo("TOOL INSTALLATION STATISTICS")
    click.echo("=" * 50)
    click.echo(f"Total Installation Records: {stats['total_records']}")
    click.echo(f"Total Machines: {stats['total_machines']}")
    click.echo(f"Total Tools: {stats['total_tools']}")
    
    if stats['tools_per_machine']:
        click.echo("\nTools per Machine:")
        click.echo("-" * 50)
        for machine, count in stats['tools_per_machine'].items():
            click.echo(f"  {machine}: {count} tool(s)")

@cli.command()
@click.option('--machine', default=None, help='Filter by machine name')
def machines(machine):
    """List all machines or get details for a specific machine"""
    
    if machine:
        records = db.get_installations_by_machine(machine)
        if records:
            click.echo(f"Machine: {machine}")
            click.echo(f"Tools installed: {len(records)}")
            click.echo("\nTools:")
            for record in records:
                click.echo(f"  - {record['tool']} (installed: {record['installed_date']})")
        else:
            click.echo(f"No records found for machine '{machine}'")
    else:
        records = db.get_all_installations()
        machines_set = set(record['machine'] for record in records)
        
        if not machines_set:
            click.echo("No machines found")
            return
        
        click.echo("Machines in database:")
        for m in sorted(machines_set):
            tool_count = len([r for r in records if r['machine'] == m])
            click.echo(f"  - {m} ({tool_count} tool(s))")

@cli.command()
@click.option('--tool', default=None, help='Filter by tool name')
def tools(tool):
    """List all tools or get details for a specific tool"""
    
    if tool:
        records = db.get_installations_by_tool(tool)
        if records:
            click.echo(f"Tool: {tool}")
            click.echo(f"Installed on: {len(records)} machine(s)")
            click.echo("\nMachines:")
            for record in records:
                click.echo(f"  - {record['machine']} (installed: {record['installed_date']})")
        else:
            click.echo(f"No records found for tool '{tool}'")
    else:
        records = db.get_all_installations()
        tools_set = set((record['tool'], record['tool_type']) for record in records)
        
        if not tools_set:
            click.echo("No tools found")
            return
        
        click.echo("Tools in database:")
        for tool_name, tool_type in sorted(tools_set):
            machine_count = len([r for r in records if r['tool'] == tool_name])
            type_str = f" ({tool_type})" if tool_type else ""
            click.echo(f"  - {tool_name}{type_str}: installed on {machine_count} machine(s)")

def main():
    """Entry point for the CLI"""
    cli()

if __name__ == '__main__':
    main()
