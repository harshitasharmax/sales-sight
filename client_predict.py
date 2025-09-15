import requests
sample = {
  "price": 62.5,
  "promotion": 0,
  "dayofweek": 1,
  "month": 9,
  "is_weekend": 0,
  "qty_lag_1": 18,
  "qty_lag_7": 14,
  "qty_roll_7": 15.4
}
resp = requests.post("http://127.0.0.1:5000/predict", json=sample)
print(resp.status_code, resp.json())
