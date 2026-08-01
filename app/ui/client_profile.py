from rich.console import Console
from rich.prompt import Prompt

from app.models.client import Client
from app.services.ai_analysis import AIAnalysisService
from app.services.financial_analysis import FinancialAnalysisService
from app.services.meeting_preparation import (
    MeetingPreparationService,
)
from app.services.storage import delete_client
from app.ui.analysis_view import AnalysisView
from app.ui.components.client_dashboard import ClientDashboard
from app.ui.components.theme import BANK_THEME
from app.ui.meeting_view import MeetingView

console = Console(theme=BANK_THEME)


class ClientProfile:
    @staticmethod
    def show(
        client: Client,
        index: int,
    ) -> bool:
        """
        Display the selected client.

        Returns
        -------
        True
            Client was deleted.

        False
            Return to previous menu.
        """

        while True:
            context = FinancialAnalysisService.analyze(client)

            console.clear()

            console.print(ClientDashboard.render(context))

            console.print()

            console.print("[section]Actions[/section]")

            console.print("[number][A][/number] 🤖 AI Analysis")

            console.print("[number][M][/number] 📅 Meeting Preparation")

            console.print("[number][C][/number] 💬 Advisor Copilot")

            console.print("[number][E][/number] ✏ Edit Client")

            console.print("[number][D][/number] 🗑 Delete Client")

            console.print("[number][B][/number] ⬅ Back")

            choice = Prompt.ask(
                "\nSelect option",
                choices=[
                    "A",
                    "M",
                    "C",
                    "E",
                    "D",
                    "B",
                    "a",
                    "m",
                    "c",
                    "e",
                    "d",
                    "b",
                ],
            ).upper()

            if choice == "A":
                with console.status("[info]Generating AI Analysis..."):
                    report = AIAnalysisService.analyze(client)

                AnalysisView.display(report)

            elif choice == "M":
                with console.status("[info]Preparing Meeting..."):
                    report = MeetingPreparationService.prepare(client)

                MeetingView.display(report)

            elif choice == "C":
                console.print()

                console.print("[warning]Advisor Copilot coming soon.[/warning]")

                input("\nPress ENTER to continue...")

            elif choice == "E":
                console.print()

                console.print("[warning]Edit Client coming soon.[/warning]")

                input("\nPress ENTER to continue...")

            elif choice == "D":
                confirm = Prompt.ask(
                    "\nDelete this client?",
                    choices=["y", "n"],
                    default="n",
                )

                if confirm == "y":
                    delete_client(index)

                    console.print()

                    console.print("[danger]Client deleted.[/danger]")

                    input("\nPress ENTER...")

                    return True

            elif choice == "B":
                return False
