from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


class Dashboard:
    @staticmethod
    def display(metrics: dict) -> None:

        if metrics["score"] >= 90:
            colour = "green"

        elif metrics["score"] >= 75:
            colour = "yellow"

        elif metrics["score"] >= 60:
            colour = "dark_orange"

        else:
            colour = "red"

        table = Table(
            show_header=False,
            box=None,
            pad_edge=False,
        )

        table.add_column(width=28)
        table.add_column(justify="right")

        table.add_row(
            "Financial Health Score",
            f"{metrics['score']} / 100",
        )

        table.add_row(
            "Rating",
            metrics["rating"],
        )

        table.add_row(
            "Monthly Income",
            f"{metrics['monthly_income']:,.0f} SEK",
        )

        table.add_row(
            "Monthly Surplus",
            f"{metrics['monthly_surplus']:,.0f} SEK",
        )

        table.add_row(
            "Savings Ratio",
            str(metrics["savings_ratio"]),
        )

        table.add_row(
            "Debt Ratio",
            str(metrics["debt_ratio"]),
        )

        table.add_row(
            "Savings Rate",
            f"{metrics['savings_rate']} %",
        )

        console.print()

        console.print(
            Panel(
                table,
                title="Financial Dashboard",
                border_style=colour,
            )
        )
