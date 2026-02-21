import pandas as pd
import joblib
import sys
sys.path.append('src')

from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from model import get_model

def train():
    data = load_diabetes()
    X = pd.DataFrame(data.data)
    y = pd.Series(data.target)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = get_model()
    model.fit(X_train, y_train)

    joblib.dump(model, "model.pkl")
    print("Model saved successfully as model.pkl")

if __name__ == "__main__":
    train()
