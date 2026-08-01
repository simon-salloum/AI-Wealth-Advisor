import json
from dataclasses import asdict
from pathlib import Path

from app.models.client import Client
from app.models.enums import (
    InvestmentExperience,
    InvestmentGoal,
    RiskTolerance,
)

DATA_FILE = Path("data/clients.json")


def load_clients() -> list[Client]:
    if not DATA_FILE.exists():
        return []

    with DATA_FILE.open(
        "r",
        encoding="utf-8",
    ) as file:
        data = json.load(file)

    clients = []

    for client_data in data:
        client = Client(
            name=client_data["name"],
            age=client_data["age"],
            annual_income=client_data["annual_income"],
            savings=client_data["savings"],
            monthly_expenses=client_data["monthly_expenses"],
            mortgage=client_data["mortgage"],
            investment_experience=InvestmentExperience(
                client_data["investment_experience"]
            ),
            risk_tolerance=RiskTolerance(client_data["risk_tolerance"]),
            investment_goal=InvestmentGoal(client_data["investment_goal"]),
            time_horizon=client_data["time_horizon"],
        )

        clients.append(client)

    return clients


def save_client(client: Client) -> None:
    clients = load_clients()

    clients.append(client)

    data = []

    for stored_client in clients:
        client_dict = asdict(stored_client)

        client_dict["investment_experience"] = stored_client.investment_experience.value

        client_dict["risk_tolerance"] = stored_client.risk_tolerance.value

        client_dict["investment_goal"] = stored_client.investment_goal.value

        data.append(client_dict)

    DATA_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with DATA_FILE.open(
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            data,
            file,
            indent=4,
        )


def save_all_clients(clients: list[Client]) -> None:
    data = []

    for client in clients:
        client_dict = asdict(client)

        client_dict["investment_experience"] = client.investment_experience.value

        client_dict["risk_tolerance"] = client.risk_tolerance.value

        client_dict["investment_goal"] = client.investment_goal.value

        data.append(client_dict)

    with DATA_FILE.open(
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(data, file, indent=4)


def delete_client(index: int) -> None:
    clients = load_clients()

    clients.pop(index)

    save_all_clients(clients)
