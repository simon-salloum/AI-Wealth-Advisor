from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

from app.services.storage import save_client
from app.ui.client_manager import ClientManager
from app.ui.forms import ClientForm

console = Console()


class WealthAdvisor:
    def __init__(self) -> None:
        self.client_manager = ClientManager()

    def run(self) -> None:
        while True:
            self.show_menu()

            choice = Prompt.ask(
                "Select an option",
                choices=["1", "2", "3"],
                default="3",
            )

            if choice == "1":
                self.add_client()

            elif choice == "2":
                self.client_manager.view_clients()

            elif choice == "3":
                console.print(
                    "\nGoodbye!\n",
                    style="bold green",
                )
                break

    def show_menu(self) -> None:
        console.clear()

        console.print(
            Panel.fit(
                "[bold cyan]AI Wealth Advisor[/bold cyan]",
                subtitle="Private Banking Assistant",
                border_style="blue",
            )
        )

        table = Table(
            show_header=True,
            header_style="bold blue",
        )

        table.add_column(
            "Option",
            justify="center",
            width=10,
        )

        table.add_column(
            "Description",
            width=35,
        )

        table.add_row("1", "Add Client")
        table.add_row("2", "View Clients")
        table.add_row("3", "Exit")

        console.print(table)

    def add_client(self) -> None:
        console.clear()

        console.print(Panel.fit("[bold green]Create New Client[/bold green]"))

        client = ClientForm.create()

        save_client(client)

        console.print(
            "\nClient saved successfully.",
            style="bold green",
        )

        input("\nPress ENTER to continue...")
