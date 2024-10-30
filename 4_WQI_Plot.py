import matplotlib.pyplot as plt

# Plot the WQI trend over time
plt.figure(figsize=(10, 6))
plt.plot(ganga_data['Months'], ganga_data['Water_Quality_Index'], label='WQI', color='blue')
plt.title('Water Quality Index (WQI) Trend')
plt.xlabel('Time')
plt.ylabel('WQI')
plt.xticks(rotation=45)
plt.legend()
plt.show()
