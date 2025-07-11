# Financial Fraud Detection Dashboard

This project is a real-time interactive dashboard for detecting and visualizing financial fraud using machine learning predictions and geospatial data.

## Features

- **Fraud Prediction Charts** (Pie & Bar)
- **Geospatial Fraud Map** using Mapbox
- **Risk Score Trends** over time
- **User Activity Timeline**
- **High-Risk User Alerts**
- FastAPI backend with Jinja2 templates

##  Project Structure

financial-fraud-detection/
├── data/
│ └── predicted_frauds_with_location.csv
├── src/
│ └── api/
│ ├── main.py
│ └── templates/
│ └── dashboard.html
├── venv/ (or .venv)
├── .gitignore
└── README.md


## Run Locally

```bash
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn pandas jinja2
uvicorn src.api.main:app --reload
