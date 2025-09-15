import pandas as pd
import numpy as np
import os

def load_and_prepare(path="data/sales.csv"):
    df = pd.read_csv(path, parse_dates=["date"])
    df["sales_value"] = df["price"] * df["quantity"]
    df = df.sort_values(["store_id", "product_id", "date"])
    df["dayofweek"] = df["date"].dt.dayofweek
    df["month"] = df["date"].dt.month
    df["is_weekend"] = (df["dayofweek"] >= 5).astype(int)
    df["qty_lag_1"] = df.groupby(["store_id","product_id"])["quantity"].shift(1).fillna(0)
    df["qty_lag_7"] = df.groupby(["store_id","product_id"])["quantity"].shift(7).fillna(0)
    df["qty_roll_7"] = df.groupby(["store_id","product_id"])["quantity"].transform(lambda x: x.rolling(7,min_periods=1).mean()).fillna(0)
    df = df.fillna(0)
    return df

if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    df = load_and_prepare("data/sales.csv")
    df.to_csv("data/sales_prepared.csv", index=False)
    print("Saved data/sales_prepared.csv with", len(df), "rows")
