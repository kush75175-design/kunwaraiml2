import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, r2_score

# DATASET SETUP
# Rainfall (mm), Temp (Celsius), Area (Hectares), Soil pH
data = {
    'Rainfall_mm': [500, 1200, 800, 1500, 600, 1100, 900, 1400, 700, 1000],
    'Temp_C': [25, 28, 26, 32, 24, 29, 27, 31, 25, 28],
    'Area_Hectares': [10, 25, 15, 30, 12, 20, 18, 28, 14, 22],
    'Soil_pH': [6.2, 7.0, 6.5, 5.8, 6.1, 7.2, 6.8, 5.5, 6.4, 7.1],
    'Yield_Tons': [15, 45, 25, 35, 18, 42, 30, 32, 20, 38]
}
df = pd.DataFrame(data)

X = df[['Rainfall_mm', 'Temp_C', 'Area_Hectares', 'Soil_pH']]
y = df['Yield_Tons']

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
                                                  
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)

model = Ridge(alpha=1.0)
model.fit(X_train_scaled, y_train)

# EVALUATION
predictions = model.predict(X_val_scaled)
r2 = r2_score(y_val, predictions)
rmse = np.sqrt(mean_squared_error(y_val, predictions))

print("\n" + "="*40)
print("   AGRI-YIELD PREDICTION SYSTEM")
print("="*40)
print(f"Model Accuracy: {r2:.2%}")
print(f"Prediction Margin of Error: ±{rmse:.2f} Tons")
print("-" * 40)

new_data = pd.DataFrame([[1000, 27, 20, 6.5]], 
                        columns=['Rainfall_mm', 'Temp_C', 'Area_Hectares', 'Soil_pH'])

new_scaled = scaler.transform(new_data)
final_yield = model.predict(new_scaled)

print("   PREDICTION FOR NEW FARM CASE")
print(f"Rain: 1000mm | Temp: 27°C | Area: 20Hec | pH: 6.5")
print(f"ESTIMATED YIELD: {final_yield[0]:.2f} Tons")
print("="*40 + "\n")

# VISUALIZATION (Actual vs Predicted)
plt.figure(figsize=(8, 5))
plt.scatter(y_val, predictions, color='green', label='Predictions')
plt.plot([y_val.min(), y_val.max()], [y_val.min(), y_val.max()], 'r--', label='Perfect Match')
plt.xlabel("Actual Yield (Tons)")
plt.ylabel("Predicted Yield (Tons)")
plt.title("Actual vs Predicted Crop Yield")
plt.legend()
plt.show()
