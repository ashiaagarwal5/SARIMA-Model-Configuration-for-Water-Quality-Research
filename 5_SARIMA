from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_absolute_error

# Define training and testing data (use last 12 months as test data)
train_data = ganga_data['Water_Quality_Index'][:-12]
test_data = ganga_data['Water_Quality_Index'][-12:]

# Fit the SARIMA model
sarima_model = SARIMAX(train_data, order=(1,1,1), seasonal_order=(1,1,1,12))
sarima_result = sarima_model.fit()

# Forecast for the next 12 months
forecast = sarima_result.get_forecast(steps=12).predicted_mean

# Calculate MAE to evaluate the model
mae_value = mean_absolute_error(test_data, forecast)
print(f"Mean Absolute Error (MAE): {mae_value}")

# Plot the forecast
plt.figure(figsize=(10, 6))
plt.plot(ganga_data['Months'], ganga_data['Water_Quality_Index'], label='Observed WQI', color='blue')
plt.plot(pd.date_range(start=ganga_data['Months'].iloc[-1], periods=12, freq='M'), forecast, label='Forecasted WQI', color='red', linestyle='--')
plt.title('WQI Forecast')
plt.xlabel('Time')
plt.ylabel('WQI')
plt.xticks(rotation=45)
plt.legend()
plt.show()
