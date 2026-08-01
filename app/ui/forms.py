from rich.prompt import IntPrompt, Prompt

from app.models.client import Client
from app.models.enums import (
    InvestmentExperience,
    InvestmentGoal,
    RiskTolerance,
)


class ClientForm:
    @staticmethod
    def create() -> Client:
        name = Prompt.ask("Name")

        age = IntPrompt.ask("Age")

        annual_income = float(Prompt.ask("Annual Income"))

        savings = float(Prompt.ask("Savings"))

        monthly_expenses = float(Prompt.ask("Monthly Expenses"))

        mortgage = float(Prompt.ask("Mortgage"))

        investment_experience = InvestmentExperience(
            Prompt.ask(
                "Investment Experience",
                choices=[
                    "Beginner",
                    "Intermediate",
                    "Advanced",
                ],
            )
        )

        risk_tolerance = RiskTolerance(
            Prompt.ask(
                "Risk Tolerance",
                choices=[
                    "Low",
                    "Medium",
                    "High",
                ],
            )
        )

        investment_goal = InvestmentGoal(
            Prompt.ask(
                "Investment Goal",
                choices=[
                    "Retirement",
                    "Wealth Growth",
                    "Capital Preservation",
                    "Education",
                ],
            )
        )

        time_horizon = IntPrompt.ask("Time Horizon (Years)")

        return Client(
            name=name,
            age=age,
            annual_income=annual_income,
            savings=savings,
            monthly_expenses=monthly_expenses,
            mortgage=mortgage,
            investment_experience=investment_experience,
            risk_tolerance=risk_tolerance,
            investment_goal=investment_goal,
            time_horizon=time_horizon,
        )
