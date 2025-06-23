import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler


MODEL_PATH = 'models/random_forest_model.pkl'
DATA_PATH = 'data/new_transactions.csv'  
OUTPUT_PATH = 'data/predicted_frauds.csv'

def load_model(path):
    return joblib.load(path)

def load_data(path):
    return pd.read_csv(path)

def prepare_features(df):
    features = df.drop(columns=['transaction_id', 'timestamp'], errors='ignore')
    return features

def main():
    print("🔍 Loading model...")
    model = load_model(MODEL_PATH)

    print("📄 Loading new transaction data...")
    df = load_data(DATA_PATH)

    X = prepare_features(df)

    print("🤖 Predicting frauds...")
    predictions = model.predict(X)
    probabilities = model.predict_proba(X)[:, 1]  

    df['is_fraud_predicted'] = predictions
    df['fraud_confidence'] = probabilities

    print(f" Saving predictions to {OUTPUT_PATH}...")
    df.to_csv(OUTPUT_PATH, index=False)
    print(" Predictions saved!")

if __name__ == '__main__':
    main()
