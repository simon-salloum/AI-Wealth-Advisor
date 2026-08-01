# AI Wealth Advisor

> An AI-powered Private Banking Decision Support application built with Python, OpenAI, and Rich.

AI Wealth Advisor is a terminal-based application designed to simulate an internal advisory tool used by private bankers and financial advisors. It helps advisors manage clients, assess financial health, generate AI-driven insights, and prepare for client meetings.

---

## Features

### Client Management
- Add new clients
- View client portfolio
- Delete clients
- JSON-based data storage

### Financial Analysis
- Financial Health Score (0–100)
- Financial Rating
- Savings Ratio
- Debt Ratio
- Monthly Surplus
- Savings Rate

### AI Features
- AI-generated financial analysis
- AI meeting preparation
- Personalized recommendations
- Investment observations
- Risk assessment

### Dashboard
- Professional Rich terminal interface
- Financial Health dashboard
- Client Information panel
- Investment Profile
- AI Advisor status
- Keyboard shortcuts for navigation

---

## Technologies

- Python 3.14
- OpenAI API
- Rich
- Dataclasses
- Enum
- Ruff
- Git
- GitHub

---

## Project Structure

```text
AI Wealth Advisor
│
├── app
│   ├── models
│   ├── services
│   ├── ui
│   │   ├── components
│   │   ├── analysis_view.py
│   │   ├── client_manager.py
│   │   ├── client_profile.py
│   │   ├── meeting_view.py
│   │   └── advisor.py
│   │
│   └── utils
│
├── data
├── reports
├── main.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/ai-wealth-advisor.git
```

Navigate to the project:

```bash
cd ai-wealth-advisor
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
```

Run the application:

```bash
python main.py
```

---

## Future Improvements

- SQLite database
- Portfolio dashboard
- Advisor Copilot
- Client search
- Client editing
- PDF report generation
- Portfolio analytics
- Charts and visualizations
- Authentication
- Web application (Streamlit or FastAPI)

---

## What I Learned

This project was built to strengthen my Python skills by applying software engineering principles to a realistic business case.

During development I practiced:

- Object-Oriented Programming
- Clean Architecture
- API integrations
- Data modeling with dataclasses
- Modular application design
- Building reusable UI components
- Working with Git and GitHub
- Structuring larger Python projects

The project will continue to evolve as I expand my knowledge of Python, databases, AI integrations, and software architecture.

---

## Author

**Simon Salloum**

Business Analyst | Python Developer | Data & AI Enthusiast

GitHub: https://github.com/simon-salloum