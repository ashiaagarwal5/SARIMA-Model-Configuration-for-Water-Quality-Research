# Define weights for each parameter
weights = {
    'Q_DO': 0.12, 'Q_Fecal_Coliform': 0.07, 'Q_pH': 0.09, 'Q_BOD': 0.09,
    'Q_Nitrate': 0.1, 'Q_Total_Phosphate': 0.09, 'Q_Total_Solids': 0.07,
    'Q_Sulphate': 0.06, 'Q_EC': 0.04, 'Q_Alkalinity': 0.05, 'Q_Chloride': 0.05, 'Q_Hardness': 0.04
}

# Initialize WQI column
ganga_data['Water_Quality_Index'] = 0

# Calculate WQI by multiplying q-values by weights
for param, weight in weights.items():
    ganga_data['Water_Quality_Index'] += ganga_data[param] * weight

# Normalize by the sum of the weights
ganga_data['Water_Quality_Index'] /= sum(weights.values())
