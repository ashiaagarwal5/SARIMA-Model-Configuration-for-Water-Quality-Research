# Forecast for Nitrate
nitrate_train_data = ganga_data['Nitrate'][:-12]  # Use all except last 12 months for training
nitrate_test_data = ganga_data['Nitrate'][-12:]   # Use the last 12 months for testing

# Fit the SARIMA model for Nitrate
nitrate_sarima_model = SARIMAX(nitrate_train_data, order=(1,1,1), seasonal_order=(1,1,1,12))
nitrate_sarima_result = nitrate_sarima_model.fit()

# Forecast Nitrate for the next 12 months
nitrate_forecast = nitrate_sarima_result.get_forecast(steps=12).predicted_mean

# Evaluate Nitrate forecast accuracy with MAE
nitrate_mae = mean_absolute_error(nitrate_test_data, nitrate_forecast)
print(f"Nitrate MAE: {nitrate_mae}")

# Plot Nitrate Forecast
plt.figure(figsize=(10, 6))
plt.plot(ganga_data['Months'], ganga_data['Nitrate'], label='Observed Nitrate', color='blue')
plt.plot(pd.date_range(start=ganga_data['Months'].iloc[-1], periods=12, freq='M'), nitrate_forecast, label='Forecasted Nitrate', color='red', linestyle='--')
plt.title('Nitrate Forecast')
plt.xlabel('Time')
plt.ylabel('Nitrate (mg/L)')
plt.xticks(rotation=45)
plt.legend()
plt.show()
