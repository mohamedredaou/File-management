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
    "██████╗ ███████╗██████╗  █████╗ ██╗  ██╗     ██████╗██╗     ██╗",
    "██╔══██╗██╔════╝██╔══██╗██╔══██╗╚██╗██╔╝    ██╔════╝██║     ██║",
    "██████╔╝█████╗  ██║  ██║███████║ ╚███╔╝     ██║     ██║     ██║",
    "██╔══██╗██╔════╝██║  ██║██╔══██║ ██╔██╗     ██║     ██║     ██║",
    "██║  ██║███████╗██████╔╝██║  ██║██╔╝ ██╗    ╚██████╗███████╗██║",
    "╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝╚══════╝╚═╝"]

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

# run
if __name__ == "__main__":
    """Display the Title"""
    for line in Title_REDAX_CLI:
        console.print(f"[bold cyan]{line}[/bold cyan]")

    console.print(f"\n[bold white]Welcome to {APP_NAME} v{VERSION}![/bold white]")
    console.print("Type [bold yellow]--help [/bold yellow] to see avialable commands.\n")

    cli()