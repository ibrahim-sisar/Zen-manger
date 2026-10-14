"""
ZEN - Command Line Interface (cli)
===================================

Description:
------------
This module serves as the Command Line Interface for the Zen Manager.
It provides the primary user-facing interface through the terminal,
handling user input, command routing, menus, and interaction flow.

The CLI is responsible for communicating with the user and delegating
actual project operations to the Zen Manager's core engine.

This keeps the user interaction layer separated from the core application
logic and system-level operations.

Responsibilities:
-----------------
* User Interaction: Handling user input and displaying information.
* Command Routing: Interpreting commands and directing them to the engine.
* Menu Management: Providing interactive menus and navigation flows.
* Input Validation: Validating and processing user-provided data.
* Output Formatting: Presenting results, errors, and status information.
* Engine Communication: Delegating operations to the core Zen engine.

Technical Details:
------------------
* Module: core/cli.py
* Dependencies: Rich, Questionary, Pyfiglet
* Interface: Command Line / Terminal

Author:
-------
Ibrahim Said Abu Al-Roos (ibrahim.sisar@gmail.com)
Date: 07/06/2026

Last modified:
--------------
Date: 26/08/2026
"""

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
import questionary


console = Console()


def welcome() -> None:
    """Display the Zen welcome screen."""
    
    title = Text("ZEN", style="bold cyan")
    subtitle = Text("Minimalist Project Manager", style="dim")

    content = Text()
    content.append("\n")
    content.append(title)
    content.append("\n")
    content.append(subtitle)
    content.append("\n")

    console.print(
        Panel(
            Align.center(content),
            border_style="cyan",
            padding=(1, 4),
        )
    )


def main_menu() -> str:
    """Display the main menu and return the selected option."""

    return questionary.select(
        "What do you want to do?",
        choices=[
            "Create Project",
            "Open Project",
            "Manage Projects",
            "Settings",
            "Exit",
        ],
    ).ask()


def main() -> None:
    """Run the Zen CLI."""

    welcome()

    while True:
        choice = main_menu()

        if choice == "Exit" or choice is None:
            console.print("\n[cyan]Goodbye 👋[/cyan]")
            break

        console.print(f"\n[green]Selected:[/green] {choice}")


if __name__ == "__main__":
    main()