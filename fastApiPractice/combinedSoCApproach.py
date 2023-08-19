# # Battery parameters
# Q = 3.5  # Battery capacity in Ah
# Vmax = 4.2  # Maximum battery voltage in V
# Vmin = 3.0  # Minimum battery voltage in V
# I = 0.5  # Battery current in A (negative for discharge, positive for charge)
# dt = 1  # Time interval in seconds

# V = 3.65  # Battery voltage in V (measured)
# SoC_OCV = (V - Vmin) / (Vmax - Vmin)*100
# Initial_SoC = SoC_OCV 
# # Calculate SoC using Coulomb counting method
# dQ = I * dt  # Change in charge/discharge
# SoC_CCM = Initial_SoC + (dQ/Q) * 100  # Coulomb counting method

# # Calculate SoC using voltage-based method (OCV)
# V = 3.65  # Battery voltage in V (measured)
# SoC_OCV = (V - Vmin) / (Vmax - Vmin)*100  # OCV method

# # Weight for combining methods
# alpha = 0.5  # Weight for Coulomb counting method (adjust as needed)

# # Combine methods using weighted average
# Combined_SoC = alpha * SoC_CCM + (1 - alpha) * SoC_OCV

# # Print results
# print(f"Coulomb Counting SoC: {SoC_CCM:.4f}")
# print(f"Voltage-Based SoC (OCV): {SoC_OCV:.4f}")
# print(f"Combined SoC: {Combined_SoC:.4f}")

import pandas as pd

# Battery parameters
Q = 3.5  # Battery capacity in mAh
Vmax = 4.2  # Maximum battery voltage in V
Vmin = 3.0  # Minimum battery voltage in V
dt = 60  # Time interval in seconds (1 minute)

# Read battery readings from CSV file
battery_data = pd.read_csv("demo-batteryReadings.csv", parse_dates=["Timestamp"])

# Calculate initial SoC using voltage-based method (OCV)
initial_V = battery_data.iloc[0]["Voltage(V)"]
initial_SoC_OCV = (initial_V - Vmin) / (Vmax - Vmin) * 100  # Initial OCV method
# Initialize lists to store results
SoC_CCM_list = []
SoC_OCV_list = []
Combined_SoC_list = []

# Iterate through battery readings
SoC_CCM = initial_SoC_OCV  # Initialize Coulomb counting SoC with initial OCV estimate
for i, reading in battery_data.iterrows():
    # Battery current in A (negative for discharge, positive for charge)
    I = reading["Current(A)"]

    # Calculate SoC using voltage-based method (OCV)
    V = reading["Voltage(V)"]
    SoC_OCV = (V - Vmin) / (Vmax - Vmin) * 100  # OCV method
    
    # Calculate SoC using Coulomb counting method
    dQ = I * dt  # Change in charge/discharge
    SoC_CCM = SoC_CCM + (dQ / Q)  # Coulomb counting method
    
    # Combine methods using weighted average (adjust alpha as needed)
    alpha = 0.5
    Combined_SoC = alpha * SoC_CCM + (1 - alpha) * SoC_OCV
    
    # Append results to lists
    SoC_CCM_list.append(SoC_CCM)
    SoC_OCV_list.append(SoC_OCV)
    Combined_SoC_list.append(Combined_SoC)


# Print results for each timestamp
for i, reading in enumerate(battery_data["Timestamp"]):
    print(f"Timestamp: {reading}")
    print(f"Coulomb Counting SoC: {SoC_CCM_list[i]:.4f}")
    print(f"Voltage-Based SoC (OCV): {SoC_OCV_list[i]:.4f}")
    print(f"Combined SoC: {Combined_SoC_list[i]:.4f}")
    print("---------------------")
