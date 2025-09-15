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
