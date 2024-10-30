import matplotlib.pyplot as plt

# Filter observed data for March 2018 to March 2024
observed_data = ganga_data[(ganga_data['Months'] >= '2018-03') & (ganga_data['Months'] <= '2024-03')]

# Dates for forecasted values from April 2024 to April 2025
forecast_dates = pd.date_range(start=observed_data['Months'].iloc[-1] + pd.DateOffset(months=1), periods=12, freq='M')

# Observed Values 2x2 Grid
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Observed WQI
axs[0, 0].plot(observed_data['Months'], observed_data['Water_Quality_Index'], color='blue')
axs[0, 0].set_title('Observed WQI')
axs[0, 0].set_xlabel('Time')
axs[0, 0].set_ylabel('WQI')

# Observed Nitrate
axs[0, 1].plot(observed_data['Months'], observed_data['Nitrate'], color='green')
axs[0, 1].set_title('Observed Nitrate')
axs[0, 1].set_xlabel('Time')
axs[0, 1].set_ylabel('Nitrate (mg/L)')

# Observed DO
axs[1, 0].plot(observed_data['Months'], observed_data['DO'], color='purple')
axs[1, 0].set_title('Observed Dissolved Oxygen (DO)')
axs[1, 0].set_xlabel('Time')
axs[1, 0].set_ylabel('DO (mg/L)')

# Observed pH
axs[1, 1].plot(observed_data['Months'], observed_data['pH'], color='orange')
axs[1, 1].set_title('Observed pH')
axs[1, 1].set_xlabel('Time')
axs[1, 1].set_ylabel('pH')

plt.tight_layout()
plt.show()

# Forecasted Values 2x2 Grid
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Forecasted WQI (with observed values included)
axs[0, 0].plot(observed_data['Months'], observed_data['Water_Quality_Index'], color='blue', label='Observed')
axs[0, 0].plot(forecast_dates, forecast, color='red', linestyle='--', label='Forecasted')
axs[0, 0].set_title('Forecasted WQI')
axs[0, 0].set_xlabel('Time')
axs[0, 0].set_ylabel('WQI')
axs[0, 0].legend()

# Forecasted Nitrate (with observed values included)
axs[0, 1].plot(observed_data['Months'], observed_data['Nitrate'], color='green', label='Observed')
axs[0, 1].plot(forecast_dates, nitrate_forecast, color='red', linestyle='--', label='Forecasted')
axs[0, 1].set_title('Forecasted Nitrate')
axs[0, 1].set_xlabel('Time')
axs[0, 1].set_ylabel('Nitrate (mg/L)')
axs[0, 1].legend()

# Forecasted DO (with observed values included)
axs[1, 0].plot(observed_data['Months'], observed_data['DO'], color='purple', label='Observed')
axs[1, 0].plot(forecast_dates, do_forecast, color='red', linestyle='--', label='Forecasted')
axs[1, 0].set_title('Forecasted Dissolved Oxygen (DO)')
axs[1, 0].set_xlabel('Time')
axs[1, 0].set_ylabel('DO (mg/L)')
axs[1, 0].legend()

# Forecasted pH (with observed values included)
axs[1, 1].plot(observed_data['Months'], observed_data['pH'], color='orange', label='Observed')
axs[1, 1].plot(forecast_dates, ph_forecast, color='red', linestyle='--', label='Forecasted')
axs[1, 1].set_title('Forecasted pH')
axs[1, 1].set_xlabel('Time')
axs[1, 1].set_ylabel('pH')
axs[1, 1].legend()

plt.tight_layout()
plt.show()
