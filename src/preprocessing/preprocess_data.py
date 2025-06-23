import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def load_data(file_path):
    """Load transaction data from CSV."""
    data = pd.read_csv(file_path)
    print(f"Loaded data with shape: {data.shape}")
    return data

def clean_data(data):
    """Handle missing values and normalize amount."""
    data = data.fillna(method='ffill')
    
    scaler = MinMaxScaler()
    if 'amount' in data.columns:
        data['amount'] = scaler.fit_transform(data[['amount']])
    else:
        print("Warning: 'amount' column not found in data!")
    
    return data

def feature_engineering(data):
    """Add features like transaction hour."""
    data['transaction_hour'] = pd.to_datetime(data['timestamp']).dt.hour
    return data

def main():
    file_path = 'data/transactions.csv'  
    data = load_data(file_path)
    data = clean_data(data)
    data = feature_engineering(data)
    print(data.head())
    data.to_csv('data/processed_transactions.csv', index=False)

    print("Preprocessing complete and saved.")

if __name__ == '__main__':
    main()
