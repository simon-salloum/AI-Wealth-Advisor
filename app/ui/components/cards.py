from rich.panel import Panel
from rich.table import Table

from app.models.financial_context import FinancialContext
from app.ui.components.badges import Badges


class DashboardCards:
    @staticmethod
    def financial_health(context: FinancialContext) -> Panel:
        table = Table(
            show_header=False,
            box=None,
            pad_edge=False,
        )

        table.add_column(style="label", width=20)
        table.add_column(style="value")

        table.add_row(
            "Health Score",
            Badges.score(context.score),
        )

        table.add_row(
            "Rating",
            Badges.rating(context.rating),
        )

        table.add_row(
            "Monthly Income",
            f"{context.monthly_income:,.0f} SEK",
        )

        table.add_row(
            "Monthly Surplus",
            f"{context.monthly_surplus:,.0f} SEK",
        )

        table.add_row(
            "Savings Ratio",
            str(context.savings_ratio),
        )

        table.add_row(
            "Debt Ratio",
            str(context.debt_ratio),
        )

        table.add_row(
            "Savings Rate",
            f"{context.savings_rate:.1f} %",
        )

        return Panel(
            table,
            title="💰 Financial Health",
            border_style="panel",
        )

    @staticmethod
    def investment_profile(
        context: FinancialContext,
    ) -> Panel:

        client = context.client

        table = Table(
            show_header=False,
            box=None,
            pad_edge=False,
        )

        table.add_column(style="label", width=18)
        table.add_column(style="value")

        table.add_row(
            "Risk",
            Badges.risk(client.risk_tolerance.value),
        )

        table.add_row(
            "Goal",
            client.investment_goal.value,
        )

        table.add_row(
            "Experience",
            client.investment_experience.value,
        )

        table.add_row(
            "Time Horizon",
            f"{client.time_horizon} years",
        )

        return Panel(
            table,
            title="📈 Investment Profile",
            border_style="panel",
        )

    @staticmethod
    def personal_information(
        context: FinancialContext,
    ) -> Panel:

        client = context.client

        table = Table(
            show_header=False,
            box=None,
            pad_edge=False,
        )

        table.add_column(style="label", width=20)
        table.add_column(style="value")

        table.add_row("Name", client.name)
        table.add_row("Age", str(client.age))
        table.add_row(
            "Income",
            f"{client.annual_income:,.0f} SEK",
        )
        table.add_row(
            "Savings",
            f"{client.savings:,.0f} SEK",
        )
        table.add_row(
            "Mortgage",
            f"{client.mortgage:,.0f} SEK",
        )
        table.add_row(
            "Monthly Expenses",
            f"{client.monthly_expenses:,.0f} SEK",
        )

        return Panel(
            table,
            title="👤 Client Information",
            border_style="panel",
        )
