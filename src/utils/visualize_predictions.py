import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load predictions
df = pd.read_csv('data/predicted_frauds.csv')

# Count plot for fraud vs non-fraud
plt.figure(figsize=(6,4))
sns.countplot(x='is_fraud_predicted', data=df)
plt.title('Fraud vs Non-Fraud Prediction Counts')
plt.xlabel('Prediction (0=Non-Fraud, 1=Fraud)')
plt.ylabel('Count')
plt.savefig('reports/fraud_vs_nonfraud_counts.png')
plt.show()


plt.figure(figsize=(8,5))
sns.histplot(data=df, x='fraud_confidence', hue='is_fraud_predicted', kde=True, bins=20)
plt.title('Confidence Score Distribution by Prediction')
plt.xlabel('Fraud Confidence Score')
plt.ylabel('Frequency')
plt.savefig('reports/confidence_score_distribution.png')
plt.show()
