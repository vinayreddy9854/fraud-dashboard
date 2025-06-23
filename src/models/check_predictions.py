import pandas as pd
df = pd.read_csv('data/predicted_frauds.csv')
print(df.head())
print("\nPrediction counts:")
print(df['is_fraud_predicted'].value_counts())
