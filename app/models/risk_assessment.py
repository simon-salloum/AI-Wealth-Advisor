from dataclasses import dataclass


@dataclass
class RiskAssessment:
    liquidity: str

    debt: str

    savings: str

    retirement: str

    cash_flow: str

    overall: str
