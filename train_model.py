import pandas as pd
import joblib
import os
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
from prepare_data import load_and_prepare

MODEL_DIR = "models"
MODEL_FILE = os.path.join(MODEL_DIR, "sales_model.pkl")

def train_and_save(path="data/sales_prepared.csv"):
    # ensure prepared file exists
    if not os.path.exists("data/sales_prepared.csv"):
        df = load_and_prepare("data/sales.csv")
        df.to_csv("data/sales_prepared.csv", index=False)
    df = pd.read_csv(path, parse_dates=["date"])
    df = df.sort_values(["store_id","product_id","date"])
    df["target_qty_next"] = df.groupby(["store_id","product_id"])["quantity"].shift(-1).fillna(0)
    features = ["price", "promotion", "dayofweek", "month", "is_weekend", "qty_lag_1", "qty_lag_7", "qty_roll_7"]
    X = df[features]
    y = df["target_qty_next"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=False)
    model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    mae = mean_absolute_error(y_test, preds)
    rmse = mean_squared_error(y_test, preds, squared=False)
    os.makedirs(MODEL_DIR, exist_ok=True)
    joblib.dump({"model": model, "features": features}, MODEL_FILE)
    print(f"Model saved to {MODEL_FILE}")
    print(f"MAE: {mae:.3f}, RMSE: {rmse:.3f}")

if __name__ == "__main__":
    train_and_save("data/sales_prepared.csv")
