from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

console = Console()


class AnalysisView:
    @staticmethod
    def display(report: str) -> None:

        console.clear()

        console.print(
            Panel.fit(
                "[bold cyan]AI Wealth Analysis[/bold cyan]",
                border_style="cyan",
            )
        )

        console.print()

        console.print(Markdown(report))

        input("\nPress ENTER...")
