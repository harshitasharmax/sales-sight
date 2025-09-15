# SalesSight — Sales Analytics & Forecasting (synthetic)

## What is this
A small end-to-end demo project that:
- generates synthetic sales data
- prepares features
- trains a RandomForest model to predict next-day quantity
- serves predictions via a Flask API
- includes a Streamlit dashboard for exploration

## Quickstart
1. Create virtualenv:
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate

2. Install requirements:
   pip install -r requirements.txt

3. Generate data:
   python generate_data.py

4. Prepare & train:
   python prepare_data.py
   python train_model.py

5. Run API:
   python api.py

6. Run dashboard:
   streamlit run dashboard.py

## Files
- data/ : generated CSVs
- models/: trained model saved as models/sales_model.pkl
- generate_data.py, prepare_data.py, train_model.py, api.py, dashboard.py, client_predict.py

## Next steps
Replace synthetic data with your real dataset, try XGBoost/LGBM, add auth, containerize with Docker, or deploy to a cloud VM.






SalesSight — Business Analytics & Forecasting
Project Report
This report documents the development of SalesSight, a business analytics and forecasting
system. It demonstrates an end-to-end pipeline for generating, processing, analyzing, and
forecasting sales data. The project integrates data generation, machine learning model training, a
Flask API for predictions, and a Streamlit dashboard for interactive analytics and visualization.
Objectives
1 Generate synthetic sales data for demonstration.
2 Prepare and engineer features suitable for forecasting.
3 Train a machine learning model to predict next-day sales quantity.
4 Expose predictions through a REST API built with Flask.
5 Visualize data and predictions via a Streamlit dashboard.
Methodology
The methodology followed these steps: 1. Data Generation: Synthetic daily sales data was created
for multiple stores and products using Python. 2. Data Preparation: The dataset was processed to
include time-based features (day of week, month, weekend flags) and lag features (previous day,
previous week, rolling averages). 3. Model Training: A RandomForestRegressor model was trained
on the prepared dataset. The target variable was next-day sales quantity. 4. API Development: A
Flask-based API was implemented to serve predictions for given input features. 5. Dashboard
Development: A Streamlit dashboard was created to visualize sales trends, KPIs, and model
forecasts.

Results
The trained RandomForest model achieved good predictive performance (measured by MAE and
RMSE). The dashboard provides clear visualization of sales patterns and enables interactive
forecasting. The API endpoint allows integration with external systems or business applications.
Tools and Technologies Used
1 Python 3
2 pandas, numpy (data handling and processing)
3 scikit-learn (machine learning)
4 Flask (API framework)
5 Streamlit, Plotly (dashboard and visualization)
6 Joblib (model persistence)
Conclusion

SalesSight demonstrates how business analytics and machine learning can be combined to provide
actionable insights and forecasts. While this project uses synthetic data, the pipeline can be
adapted to real-world business datasets for sales forecasting, demand planning, and decision
support.
Future Work
1 Integrate real business datasets from ERP/CRM systems.
2 Experiment with advanced models (XGBoost, LSTM, Prophet).
3 Deploy the system in the cloud with containerization.
4 Enhance dashboard with more advanced KPIs and drill-down analytics.
