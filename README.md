# sports-ml-system

An end-to-end machine learning system for predicting sporting outcomes — from raw data ingestion through to a live prediction API.

Built as part of preparation for a Data Science Engineering internship at DraftKings (July 2026).

---

## What This Is

This project mirrors how a real data science system is structured in production:

- Raw sports data gets ingested, cleaned, and transformed into model-ready features
- Machine learning models are trained, evaluated, and versioned on those features
- A FastAPI service exposes predictions via a clean REST API
- Automated tests cover every layer of the system

It's not a notebook. It's an engineering project.

---

## System Architecture

```
sports-ml-system/
│
├── pipeline/               # Data ingestion, cleaning, transformation
│   ├── ingest.py           # Fetch raw data from sources
│   ├── clean.py            # Handle missing values, outliers, types
│   ├── transform.py        # Feature engineering and aggregations
│   └── README.md
│
├── models/                 # ML training, evaluation, versioning
│   ├── train.py            # Model training pipeline
│   ├── evaluate.py         # Performance metrics and validation
│   ├── features.py         # Feature definitions and selection
│   └── README.md
│
├── api/                    # FastAPI prediction service
│   ├── main.py             # App entry point
│   ├── routes/             # Endpoint definitions
│   ├── schemas.py          # Request/response models
│   └── README.md
│
├── tests/                  # pytest test suite
│   ├── test_pipeline.py
│   ├── test_models.py
│   └── test_api.py
│
├── notebooks/              # Exploration and analysis (not production code)
│
├── data/
│   ├── raw/                # Original source data (gitignored if large)
│   └── processed/          # Transformed, model-ready data
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Tech Stack

| Layer | Tools |
|---|---|
| Language | Python 3.11+ |
| Data processing | pandas, NumPy |
| Machine learning | scikit-learn |
| API | FastAPI, Uvicorn |
| Testing | pytest |
| Data storage | SQL (PostgreSQL / SQLite) |
| Version control | Git |

---

## Project Status

🔨 **In Progress** — actively built March–July 2026

| Module | Status |
|---|---|
| Pipeline | 🔨 In progress |
| Models | 🔲 Upcoming |
| API | 🔲 Upcoming |
| Tests | 🔲 Upcoming |

---

## Setup

```bash
# Clone the repo
git clone https://github.com/yosh-max-code/sports-ml-system.git
cd sports-ml-system

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## Running the API

```bash
uvicorn api.main:app --reload
```

API docs available at `http://localhost:8000/docs`

---

## Running Tests

```bash
pytest tests/ -v
```

---

## Author

**Yash Singh** — CS & AI student at Aberystwyth University
Incoming Data Science Engineering Intern @ DraftKings
[LinkedIn](https://www.linkedin.com/in/yash-singh-230243257/) · [GitHub](https://github.com/yosh-max-code)
