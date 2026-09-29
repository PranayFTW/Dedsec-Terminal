from rich.console import Console
from rich.panel import Panel 

console = Console()

banner = r"""
 ____   _____  ____   ____   _____   ____
|  _ \ | ____||  _ \ / ___| | ____| / ___|
| | | ||  _|  | | | |\___ \ |  _|  | |
| |_| || |___ | |_| | ___) || |___ | |___
|____/ |_____||____/ |____/ |_____| \____|
"""

console.print(banner, style="bold green")
console.print(Panel("SYSTEM ONLINE", style="bold red", border_style="red"))