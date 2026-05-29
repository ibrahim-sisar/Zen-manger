import questionary # pyright: ignore[reportMissingImports]
from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns
from rich.text import Text
import pyfiglet
import random
import subprocess
# globel ver
console = Console()
BASE_DIR = "/mnt/C4DE4D4BDE4D36C8/ibrahim_project"

# tools
def Welcome_screen():

    ascii_art = pyfiglet.figlet_format("ZEN", font="slant")
    logo_text = Text(ascii_art, style="bold cyan")
    

    version_info = Text()
    version_info.append("\n\n") 
    version_info.append(" v1.0.0", style="bold magenta")
    version_info.append(" | ", style="dim white")
    version_info.append("Minimalist Manager\n", style="italic white")
    version_info.append(" " * 2 + "Ready to build something great?", style="dim white")
    
    header = Columns([logo_text, version_info])

    quotes = [
        "“Simplicity is the soul of efficiency.”",
        "“Breathe in, Code out.”",
        "“Code as if the next maintainer is a psychopath who knows where you live.”",
        "“Clean code always looks like it was written by someone who cares.”"
    ]
    random_quote = f"[italic cyan]{random.choice(quotes)}[/italic cyan]"
    console.print(header)

def create_new_project():
    project_name = questionary.text("what is your project name?: ").ask()
    project_type = questionary.select(
        "project type: ",
        choices = [
            "django",
            "python",
            "frontend",
            "other"
        ],
        style=questionary.Style([
            ('pointer', 'fg:cyan bold'),
            ('highlighted', 'fg:cyan bold'),
            ('selected', 'fg:green'),
        ])
    ).ask()
    output = subprocess.run(["mkdir", f"{BASE_DIR}/{project_type}/{project_name}"],capture_output=True,text=True)
    print(output.stdout)

def menu():
    choice = questionary.select(
        "Main Menu:",
        choices=[
            "1. Create new project",
            "2. Open project",
            "3. Delete project",
            "4. Tag project",
            "5. Add project idea",
            "6. List projects",
            "7. Push to GitHub",
            "8. Clone from GitHub",
            "9. Pull (Safe)",
            "Exit"
        ],
        style=questionary.Style([
            ('pointer', 'fg:cyan bold'),
            ('highlighted', 'fg:cyan bold'),
            ('selected', 'fg:green'),
        ])
    ).ask()
    
    if choice[0] == "1":
        create_new_project()
        

# project run
if __name__ == "__main__":
    Welcome_screen()
    menu()
    

