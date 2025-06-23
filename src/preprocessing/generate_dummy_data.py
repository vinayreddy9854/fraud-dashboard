import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

def generate_dummy_data(num_records=1000):
    np.random.seed(42)
    
    base_time = datetime.now()
    
    data = {
        'transaction_id': np.arange(1, num_records + 1),
        'timestamp': [base_time - timedelta(minutes=15*i) for i in range(num_records)],
        'amount': np.random.exponential(scale=2000, size=num_records).round(2),
        'is_fraud': np.random.choice([0, 1], size=num_records, p=[0.98, 0.02])
    }
    
    df = pd.DataFrame(data)
    os.makedirs('data', exist_ok=True)
    
    df.to_csv('data/transactions.csv', index=False)
    print(f"Generated dummy dataset with {num_records} records at data/transactions.csv")

if __name__ == "__main__":
    generate_dummy_data()

