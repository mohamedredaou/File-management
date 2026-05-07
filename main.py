# setup and imports
import click
from rich.console import Console
from commands.search import search_files
from commands.organize import organize_folder
from commands.move import move_file
from commands.remove import remove_file
from commands.read import read_content
from commands.read_line import read_specific_line
from commands.create import create_file
from config.settings import APP_NAME, VERSION

console = Console()

# Title: REDAX CLI
Title_REDAX_CLI = [
    "  ██████╗ ███████╗██████╗  █████╗ ██╗  ██╗     ██████╗██╗     ██╗",
    "  ██╔══██╗██╔════╝██╔══██╗██╔══██╗╚██╗██╔╝    ██╔════╝██║     ██║",
    "  ██████╔╝█████╗  ██║  ██║███████║ ╚███╔╝     ██║     ██║     ██║",
    "  ██╔══██╗██╔════╝██║  ██║██╔══██║ ██╔██╗     ██║     ██║     ██║",
    "  ██║  ██║███████╗██████╔╝██║  ██║██╔╝ ██╗    ╚██████╗███████╗██║",
    "  ╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝╚══════╝╚═╝"]

@click.group()
def cli():
    """"Simple and pwerful command-line tool to manage your files."""
    pass

@cli.command()
@click.option('--name', help='File name to search for')
@click.option('--ext', help='File extension (e.g. .txt)')
@click.option('--path', default='.', help='Directory to search in')
def search(name, ext, path):
    """Search for files by name or extension."""
    search_files(name, ext, path)

@cli.command()
@click.option('--path', required=True, help='Directory to organize')
def organize(path):
    """Automatically organize files by type or date."""
    organize_folder(path)

@cli.command()
@click.option('--src', required=True, help='Source file path')
@click.option('--dest', required=True, help='Destination directory')
def move(src, dest):
    """Move a file to a new location."""
    move_file(src, dest)

@cli.command()
@click.option('--path', required=True, help='Path to the file to delete')
def remove(path):
    """Delete a file permanently."""
    if click.confirm(f"Are you sure you want to delete {path}?"):
        remove_file(path)

@cli.command()
@click.option('--path', required=True, help='Path to the file to read')
def read(path):
    """Read and display full file content."""
    read_content(path)

@cli.command(name="read-line")
@click.option('--path', required=True, help='Path to the file')
@click.option('--line', type=int, required=True, help='Line number to read')
def read_line(path, line):
    """Read a specific line number from a file."""
    read_specific_line(path, line)

@cli.command()
@click.option('--name', required=True, help='Name of the new file')
@click.option('--path', default='.', help='Directory for the new file')
def create(name, path):
    """Create a new .txt file."""
    create_file(name, path)

# run
if __name__ == "__main__":
    """Display the Title"""
    for line in Title_REDAX_CLI:
        console.print(f"[bold cyan]{line}[/bold cyan]")

    console.print(f"\n[bold white]Welcome to {APP_NAME} v{VERSION}![/bold white]")
    console.print("Type [bold yellow]--help [/bold yellow] to see avialable commands.\n")

    cli()