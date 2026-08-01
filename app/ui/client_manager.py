from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

from app.services.storage import load_clients
from app.ui.client_profile import ClientProfile

console = Console()


class ClientManager:
    def view_clients(self) -> None:
        while True:
            clients = load_clients()

            console.clear()

            if not clients:
                console.print(
                    Panel(
                        "No clients found.",
                        title="Clients",
                        border_style="red",
                    )
                )

                input("\nPress ENTER...")
                return

            table = Table(title="Clients")

            table.add_column("#", justify="center")
            table.add_column("Name")
            table.add_column("Risk")

            for index, client in enumerate(
                clients,
                start=1,
            ):
                table.add_row(
                    str(index),
                    client.name,
                    client.risk_tolerance.value,
                )

            console.print(table)

            choices = [
                str(i)
                for i in range(
                    1,
                    len(clients) + 1,
                )
            ]

            choices.append("B")

            choice = Prompt.ask(
                "\nSelect client (B = Back)",
                choices=choices,
            )

            if choice.upper() == "B":
                return

            deleted = ClientProfile.show(
                clients[int(choice) - 1],
                int(choice) - 1,
            )

            if deleted:
                continue
