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
Title_REDAX_CLI = ["██████╗ ███████╗██████╗  █████╗ ██╗  ██╗     ██████╗██╗     ██╗",
                   "██╔══██╗██╔════╝██╔══██╗██╔══██╗╚██╗██╔╝    ██╔════╝██║     ██║",
                   "██████╔╝█████╗  ██║  ██║███████║ ╚███╔╝     ██║     ██║     ██║",
                   "██╔══██╗██╔════╝██║  ██║██╔══██║ ██╔██╗     ██║     ██║     ██║",
                   "██║  ██║███████╗██████╔╝██║  ██║██╔╝ ██╗    ╚██████╗███████╗██║",
                   "╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝╚══════╝╚═╝"]


# run
if __name__ == "__main__":
    for i in range(len(Title_REDAX_CLI)):
        console.print(Title_REDAX_CLI[i])
    console.print("\nWelcome to REDAX CLI! Please enter your command:")