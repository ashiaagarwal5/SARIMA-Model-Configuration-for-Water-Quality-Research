# Forecast for Dissolved Oxygen (DO)
do_train_data = ganga_data['DO'][:-12]  # Use all except last 12 months for training
do_test_data = ganga_data['DO'][-12:]   # Use the last 12 months for testing

# Fit the SARIMA model for DO
do_sarima_model = SARIMAX(do_train_data, order=(1,1,1), seasonal_order=(1,1,1,12))
do_sarima_result = do_sarima_model.fit()

# Forecast DO for the next 12 months
do_forecast = do_sarima_result.get_forecast(steps=12).predicted_mean

# Evaluate DO forecast accuracy with MAE
do_mae = mean_absolute_error(do_test_data, do_forecast)
print(f"Dissolved Oxygen MAE: {do_mae}")

# Plot DO Forecast
plt.figure(figsize=(10, 6))
plt.plot(ganga_data['Months'], ganga_data['DO'], label='Observed DO', color='blue')
plt.plot(pd.date_range(start=ganga_data['Months'].iloc[-1], periods=12, freq='M'), do_forecast, label='Forecasted DO', color='red', linestyle='--')
plt.title('Dissolved Oxygen (DO) Forecast')
plt.xlabel('Time')
plt.ylabel('Dissolved Oxygen (mg/L)')
plt.xticks(rotation=45)
plt.legend()
plt.show()
