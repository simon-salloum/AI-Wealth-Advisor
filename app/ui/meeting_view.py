from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

console = Console()


class MeetingView:
    @staticmethod
    def display(report: str) -> None:
        console.clear()

        console.print(
            Panel.fit(
                "[bold green]Meeting Preparation[/bold green]",
                border_style="green",
            )
        )

        console.print()

        console.print(Markdown(report))

        input("\nPress ENTER to continue...")
