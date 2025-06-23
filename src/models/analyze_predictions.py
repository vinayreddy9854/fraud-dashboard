import pandas as pd
import matplotlib.pyplot as plt

def analyze_predictions(file_path='data/predicted_frauds.csv'):
    df = pd.read_csv(file_path)
    counts = df['is_fraud_predicted'].value_counts()
    print("Prediction counts:")
    print(counts)
    
    counts.plot(kind='bar', color=['green', 'red'])
    plt.title('Predicted Fraud vs Non-Fraud Transactions')
    plt.xlabel('Is Fraud')
    plt.ylabel('Number of Transactions')
    plt.xticks(rotation=0)
    plt.show()

if __name__ == "__main__":
    analyze_predictions()
