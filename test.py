import questionary
from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns
from rich.text import Text
import pyfiglet
import random

console = Console()

def Welcome_screen():
    # 1. صنع اللوجو (ASCII Art)
    ascii_art = pyfiglet.figlet_format("ZEN", font="slant")
    # تحويل الـ ASCII لنص ملون عشان Rich يفهمه صح
    logo_text = Text(ascii_art, style="bold cyan")
    
    # 2. تجهيز معلومات الإصدار والتعريف
    version_info = Text()
    version_info.append("\n\n") # موازاة مع اللوجو
    version_info.append("v1.0.0\n", style="bold magenta")
    version_info.append("Your Minimalist Project Manager\n", style="italic white")
    
    # 3. تجميع اللوجو والإصدار في أعمدة (بره الـ Panel)
    header = Columns([logo_text, version_info])

    # 4. الحالة وعبارة الترحيب
    status = "[dim white]Status:[/dim white] [bold green]Ready to Focus[/bold green]"
    quotes = [
        "“Simplicity is the soul of efficiency.”",
        "“Breathe in, Code out.”",
        "“Clean code, clean mind.”"
    ]
    random_quote = random.choice(quotes)

    # 5. الطباعة
    console.print(header) # نطبع اللوجو والإصدار فوق
    console.print(Panel(
        Text.from_markup(f"{status}\n\n[cyan]{random_quote}[/cyan]"),
        border_style="blue",
        padding=(1, 2)
    ))

if __name__ == "__main__":
    Welcome_screen()