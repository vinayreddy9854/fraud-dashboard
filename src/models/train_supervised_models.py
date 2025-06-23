import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from imblearn.over_sampling import SMOTE

def load_data(file_path):
    return pd.read_csv(file_path)

def prepare_features(data):
    X = data.drop(columns=['is_fraud', 'transaction_id', 'timestamp'])
    y = data['is_fraud']
    return X, y

def train_and_evaluate():
    data = load_data('data/processed_transactions.csv')
    X, y = prepare_features(data)
    smote = SMOTE(random_state=42)
    X_resampled, y_resampled = smote.fit_resample(X, y)
    X_train, X_test, y_train, y_test = train_test_split(
        X_resampled, y_resampled, test_size=0.2, random_state=42
    )

    models = {
        'Logistic Regression': LogisticRegression(max_iter=1000),
        'Decision Tree': DecisionTreeClassifier(),
        'Random Forest': RandomForestClassifier(n_estimators=100)
    }

    for name, model in models.items():
        print(f'Training {name}...')
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        print(f'--- {name} Evaluation ---')
        print(classification_report(y_test, y_pred))
        print('Confusion Matrix:\n', confusion_matrix(y_test, y_pred))
        print('Accuracy:', accuracy_score(y_test, y_pred))
        print('\n')

    import joblib
    import os
    os.makedirs('models', exist_ok=True)
    best_model = models['Random Forest']
    joblib.dump(best_model, 'models/random_forest_model.pkl')
    print("Random Forest model saved to models/random_forest_model.pkl")
if __name__ == '__main__':
    train_and_evaluate()
