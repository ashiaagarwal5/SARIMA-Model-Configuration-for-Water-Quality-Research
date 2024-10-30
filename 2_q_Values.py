import io # Import the io module
import pandas as pd
import numpy as np

ganga_data = pd.read_excel(io.BytesIO(uploaded['ganga_data.xlsx']))
print(ganga_data.columns)

# Apply corrected q-value formulas for all parameters
ganga_data['Q_DO'] = -0.0093 * ganga_data['DO'] ** 2 + 1.83 * ganga_data['DO'] - 11.04
ganga_data['Q_Fecal_Coliform'] = np.log1p(ganga_data['Fecal Coliform'])
ganga_data['Q_Total_Coliform'] = np.log1p(ganga_data['Total Coliform'])
ganga_data['Q_pH'] = 89.0 * np.exp(-((ganga_data['pH'] - 7.0) ** 2) / (2 * (0.95 ** 2)))
ganga_data['Q_BOD'] = 138.94 * np.exp(-0.0853 * ganga_data['BOD'])
ganga_data['Q_Total_Phosphate'] = 100.74 * np.exp(-0.270 * ganga_data['Phosphate'])
ganga_data['Q_Nitrate'] = 102.66 * np.exp(-0.233 * ganga_data['Nitrate'])
ganga_data['Q_Total_Solids'] = -0.00018 * ganga_data['TDS'] ** 2 - 0.0536 * ganga_data['TDS'] + 88.04
ganga_data['Q_Sulphate'] = 100 - (1.5 * ganga_data['Sulphate'])
ganga_data['Q_EC'] = 100 - (0.1 * ganga_data['EC'])
ganga_data['Q_Alkalinity'] = 100 - (0.1 * ganga_data['Total Alkalinity'])
ganga_data['Q_Chloride'] = 100 - (0.5 * ganga_data['Chloride'])
ganga_data['Q_Hardness'] = 100 - (0.2 * ganga_data['Total Hardness'])
ganga_data['Q_COD'] = 100 - (0.1 * ganga_data['COD'])

# Define weights for each parameter, now including Total Coliform and COD
weights = {
    'Q_DO': 0.12, 'Q_Fecal_Coliform': 0.07, 'Q_Total_Coliform': 0.08, 'Q_pH': 0.09,
    'Q_BOD': 0.09, 'Q_Nitrate': 0.1, 'Q_Total_Phosphate': 0.09, 'Q_Total_Solids': 0.07,
    'Q_Sulphate': 0.06, 'Q_EC': 0.04, 'Q_Alkalinity': 0.05, 'Q_Chloride': 0.05,
    'Q_Hardness': 0.04, 'Q_COD': 0.05
}

# Calculate WQI
ganga_data['Water_Quality_Index'] = 0
for param, weight in weights.items():
    if param in ganga_data.columns:
        ganga_data['Water_Quality_Index'] += ganga_data[param] * weight

# Normalize by the sum of weights
ganga_data['Water_Quality_Index'] /= sum(weights.values())
