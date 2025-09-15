import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import os

st.set_page_config(page_title="SalesSight Dashboard", layout="wide")

@st.cache_data
def load_data(path="data/sales.csv"):
    df = pd.read_csv(path, parse_dates=["date"])
    df["sales_value"] = df["price"] * df["quantity"]
    return df

@st.cache_data
def load_model():
    model_bundle = joblib.load(os.path.join("models","sales_model.pkl"))
    return model_bundle

df = load_data()
model_bundle = load_model()
features = model_bundle["features"]
model = model_bundle["model"]

st.title("SalesSight — Sales Analytics & Forecasting")
left, right = st.columns([1, 2])

with left:
    store = st.selectbox("Select store", sorted(df["store_id"].unique()))
    product = st.selectbox("Select product", sorted(df["product_id"].unique()))
    st.write("Date range")
    date_min = df["date"].min()
    date_max = df["date"].max()
    date_range = st.date_input("Select date range", [date_min, date_max])

with right:
    filtered = df[(df["store_id"]==store) & (df["product_id"]==product)]
    ts = filtered.groupby("date").agg({"quantity":"sum", "sales_value":"sum"}).reset_index()
    fig = px.line(ts, x="date", y="sales_value", title=f"Sales value for {store} - {product}")
    st.plotly_chart(fig, use_container_width=True)

st.markdown("### KPIs")
k1, k2, k3 = st.columns(3)
total_sales = filtered["sales_value"].sum()
total_qty = filtered["quantity"].sum()
avg_price = filtered["price"].mean()
k1.metric("Total Sales Value", f"₹{total_sales:,.0f}")
k2.metric("Total Quantity Sold", f"{total_qty:,}")
k3.metric("Avg Price", f"₹{avg_price:.2f}")

st.markdown("### Model Prediction (next day quantity)")
latest = filtered.sort_values("date").tail(1).iloc[-1]
sample = {
    "price": float(latest["price"]),
    "promotion": int(latest["promotion"]),
    "dayofweek": int(latest["date"].dayofweek),
    "month": int(latest["date"].month),
    "is_weekend": int(latest["date"].dayofweek >=5),
    "qty_lag_1": int(latest["quantity"]),
    "qty_lag_7": int(filtered.tail(7)["quantity"].mean()) if len(filtered)>=7 else int(filtered["quantity"].mean()),
    "qty_roll_7": float(filtered.tail(7)["quantity"].mean()) if len(filtered)>=7 else float(filtered["quantity"].mean())
}
st.json(sample)
pred = model.predict(pd.DataFrame([sample])[features])[0]
st.success(f"Predicted next-day quantity: {pred:.1f}")

st.markdown("### Sales by Product (all stores)")
agg_prod = df.groupby("product_id").agg({"sales_value":"sum", "quantity":"sum"}).reset_index()
fig2 = px.bar(agg_prod, x="product_id", y="sales_value", title="Sales value by product")
st.plotly_chart(fig2, use_container_width=True)
