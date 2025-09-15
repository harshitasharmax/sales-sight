import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import os

def generate_sales(start_date="2023-01-01", days=730, n_stores=5, n_products=8, seed=42):
    np.random.seed(seed)
    rows = []
    start = datetime.fromisoformat(start_date)
    for d in range(days):
        date = start + timedelta(days=d)
        weekday = date.weekday()
        season_factor = 1.0 + 0.1 * np.sin(2 * np.pi * (d % 365) / 365)
        for store in range(1, n_stores+1):
            store_factor = 1.0 + (store - (n_stores/2)) * 0.02
            for product in range(1, n_products+1):
                base = 20 + product * 5
                weekly = 1.0 + (0.15 if weekday >=5 else 0.0)
                promo = 1.0
                if np.random.rand() < 0.02:
                    promo = 1.5
                noise = np.random.normal(scale=3.0)
                quantity = max(0, int((base * store_factor * weekly * season_factor * promo) + noise))
                price = round(50 + product*2 + np.random.normal(scale=2.0), 2)
                rows.append({
                    "date": date.strftime("%Y-%m-%d"),
                    "store_id": f"store_{store}",
                    "product_id": f"prod_{product}",
                    "price": price,
                    "quantity": quantity,
                    "promotion": 1 if promo>1 else 0
                })
    df = pd.DataFrame(rows)
    return df

if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    df = generate_sales()
    df.to_csv("data/sales.csv", index=False)
    print("Generated data/sales.csv with", len(df), "rows")
