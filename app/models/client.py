from dataclasses import dataclass

from app.models.enums import (
    InvestmentExperience,
    InvestmentGoal,
    RiskTolerance,
)


@dataclass
class Client:
    name: str
    age: int
    annual_income: float
    savings: float
    monthly_expenses: float
    mortgage: float
    investment_experience: InvestmentExperience
    risk_tolerance: RiskTolerance
    investment_goal: InvestmentGoal
    time_horizon: int
