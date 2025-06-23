from fastapi import FastAPI
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_PATH = "data/predicted_frauds.csv"

def load_data():
    return pd.read_csv(DATA_PATH)

@app.get("/api/fraud_counts")
def fraud_counts():
    df = load_data()
    counts = df['is_fraud_predicted'].value_counts().to_dict()
    return counts

@app.get("/api/anomaly_scores")
def anomaly_scores():
    df = load_data()
    summary = df['fraud_confidence'].describe().to_dict()
    return summary

@app.get("/api/heatmap_data")
def heatmap_data():
    df = load_data()
    if 'latitude' not in df.columns or 'longitude' not in df.columns:
        return {"error": "Location data missing"}
    data = df[['latitude', 'longitude', 'is_fraud_predicted']].to_dict(orient='records')
    return data
@app.get("/")
def root():
    return {"message": "Welcome to Financial Fraud Detection API"}
