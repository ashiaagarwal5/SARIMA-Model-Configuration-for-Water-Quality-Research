# Forecast for pH
ph_train_data = ganga_data['pH'][:-12]  # Use all except last 12 months for training
ph_test_data = ganga_data['pH'][-12:]   # Use the last 12 months for testing

# Fit the SARIMA model for pH
ph_sarima_model = SARIMAX(ph_train_data, order=(1,1,1), seasonal_order=(1,1,1,12))
ph_sarima_result = ph_sarima_model.fit()

# Forecast pH for the next 12 months
ph_forecast = ph_sarima_result.get_forecast(steps=12).predicted_mean

# Evaluate pH forecast accuracy with MAE
from sklearn.metrics import mean_absolute_error
ph_mae = mean_absolute_error(ph_test_data, ph_forecast)
print(f"pH MAE: {ph_mae}")
