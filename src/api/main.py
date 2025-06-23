from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pandas as pd
import os

app = FastAPI()
templates = Jinja2Templates(directory="src/api/templates")

@app.get("/", response_class=HTMLResponse)
async def get_dashboard(request: Request):
    file_path = "data/predicted_frauds_with_location.csv"

    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        return templates.TemplateResponse("dashboard.html", {
            "request": request,
            "data_available": False,
            "fraud_counts": {"0": 0, "1": 0},
            "confidence_scores": [],
            "user_activities": [],
            "risk_scores": [],
            "high_risk_users": [],
            "data": []
        })

    try:
        df = pd.read_csv(file_path)

      
        required_columns = ["is_fraud_predicted", "fraud_confidence", "latitude", "longitude"]
        if not all(col in df.columns for col in required_columns):
            raise ValueError("Missing required columns in CSV")

        df = df.dropna(subset=["latitude", "longitude"])

        fraud_counts = df["is_fraud_predicted"].value_counts().to_dict()
        fraud_counts_str = {
            '0': fraud_counts.get(0, 0),
            '1': fraud_counts.get(1, 0)
        }

        confidence_scores = df["fraud_confidence"].fillna(0).tolist()
        data = df.to_dict(orient="records")

    except Exception as e:
        print(f"Error reading CSV: {e}")
        return templates.TemplateResponse("dashboard.html", {
            "request": request,
            "data_available": False,
            "fraud_counts": {"0": 0, "1": 0},
            "confidence_scores": [],
            "user_activities": [],
            "risk_scores": [],
            "high_risk_users": [],
            "data": []
        })
    user_activities = [
        {"timestamp": "2025-05-20T08:00:00", "event": "login"},
        {"timestamp": "2025-05-20T10:15:00", "event": "transaction"},
        {"timestamp": "2025-05-21T09:30:00", "event": "logout"},
    ]


    risk_scores = [
        {"date": "2025-05-20", "score": 0.3},
        {"date": "2025-05-21", "score": 0.45},
        {"date": "2025-05-22", "score": 0.5},
    ]

   
    high_risk_users = [
        {"user_id": "U123", "risk_score": 0.9},
        {"user_id": "U456", "risk_score": 0.85},
    ]

    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "data_available": True,
        "fraud_counts": fraud_counts_str,
        "confidence_scores": confidence_scores,
        "user_activities": user_activities,
        "risk_scores": risk_scores,
        "high_risk_users": high_risk_users,
        "data": data
    })
