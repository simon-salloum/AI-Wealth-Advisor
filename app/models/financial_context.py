from dataclasses import dataclass

from app.models.client import Client


@dataclass
class FinancialContext:
    client: Client

    score: int
    rating: str

    monthly_income: float
    monthly_surplus: float

    savings_ratio: float
    debt_ratio: float
    savings_rate: float
