from rich.columns import Columns
from rich.console import Group
from rich.panel import Panel
from rich.table import Table

from app.models.financial_context import FinancialContext
from app.ui.components.badges import Badges
from app.ui.components.cards import DashboardCards


class ClientDashboard:
    @staticmethod
    def render(context: FinancialContext) -> Group:
        return Group(
            ClientDashboard.header(context),
            ClientDashboard.top_row(context),
            ClientDashboard.bottom_row(context),
        )

    @staticmethod
    def header(context: FinancialContext) -> Panel:
        client = context.client

        return Panel.fit(
            f"[title]{client.name}[/title]\n"
            f"[subtitle]Private Banking Client • Age {client.age}[/subtitle]",
            border_style="panel",
        )

    @staticmethod
    def top_row(
        context: FinancialContext,
    ) -> Columns:

        return Columns(
            [
                DashboardCards.financial_health(context),
                DashboardCards.personal_information(context),
            ],
            equal=True,
            expand=True,
        )

    @staticmethod
    def bottom_row(
        context: FinancialContext,
    ) -> Columns:

        return Columns(
            [
                DashboardCards.investment_profile(context),
                ClientDashboard.ai_status(context),
            ],
            equal=True,
            expand=True,
        )

    @staticmethod
    def ai_status(
        context: FinancialContext,
    ) -> Panel:

        table = Table(
            show_header=False,
            box=None,
            pad_edge=False,
        )

        table.add_column(width=22)
        table.add_column()

        table.add_row(
            "Financial Rating",
            Badges.rating(context.rating),
        )

        table.add_row(
            "AI Analysis",
            "[success]Ready[/success]",
        )

        table.add_row(
            "Meeting Preparation",
            "[success]Ready[/success]",
        )

        table.add_row(
            "Advisor Copilot",
            "[warning]Coming Soon[/warning]",
        )

        table.add_row(
            "PDF Reports",
            "[warning]Coming Soon[/warning]",
        )

        return Panel(
            table,
            title="🤖 AI Advisor",
            border_style="panel",
        )
