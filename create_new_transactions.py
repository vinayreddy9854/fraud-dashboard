import pandas as pd
df = pd.read_csv('data/processed_transactions.csv')
df_new = df.drop(columns=['is_fraud'])
df_new_sample = df_new.sample(n=10, random_state=42)
df_new_sample.to_csv('data/new_transactions.csv', index=False)

print(" Sample new_transactions.csv created for prediction.")
