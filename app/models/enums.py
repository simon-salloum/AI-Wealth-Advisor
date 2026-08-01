from enum import Enum


class RiskTolerance(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


class InvestmentExperience(Enum):
    BEGINNER = "Beginner"
    INTERMEDIATE = "Intermediate"
    ADVANCED = "Advanced"


class InvestmentGoal(Enum):
    RETIREMENT = "Retirement"
    WEALTH_GROWTH = "Wealth Growth"
    CAPITAL_PRESERVATION = "Capital Preservation"
    EDUCATION = "Education"
