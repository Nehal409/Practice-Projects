from fastapi import FastAPI;
# import pandas as pd
# import skfuzzy as fuzz
# import numpy as np
# from skfuzzy import control as ctrl

app = FastAPI()

# # Define fuzzy sets for each parameter (voltage, current, etc.)
# voltage = ctrl.Antecedent(np.arange(3.20, 5.19, 0.01), 'voltage')
# current = ctrl.Antecedent(np.arange(0.0, 12.01, 0.01), 'current')
# soc = ctrl.Consequent(np.arange(0, 101, 1), 'soc')

# # Define membership functions for voltage
# voltage['low'] = fuzz.trapmf(voltage.universe, [3.20, 3.40, 3.60, 3.90])
# voltage['medium'] = fuzz.trapmf(voltage.universe, [3.80, 4.00, 4.40, 4.60])
# voltage['high'] = fuzz.trapmf(voltage.universe, [4.60, 4.80, 5.00, 5.18])

# # Define membership functions for current
# current['low'] = fuzz.trapmf(current.universe, [0.0, 1.2, 2.4, 3.50])  # Adjusted
# current['medium'] = fuzz.trapmf(current.universe, [3.4, 5.8, 7.0, 9.0])  # Adjusted
# current['high'] = fuzz.trapmf(current.universe, [7.0, 10.6, 11.5, 12.00])


# # Define membership functions for SoC
# soc['low'] = fuzz.trimf(soc.universe, [0, 0, 50])
# soc['medium'] = fuzz.trimf(soc.universe, [0, 50, 100])
# soc['high'] = fuzz.trimf(soc.universe, [50, 100, 100])

# # Define fuzzy rules to estimate the battery SoC
# rule1 = ctrl.Rule(voltage['low'] & current['low'], soc['low'])
# rule2 = ctrl.Rule(voltage['medium'] & current['low'], soc['medium'])
# rule3 = ctrl.Rule(voltage['high'] & current['low'], soc['high'])

# # Create the fuzzy control system
# soc_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
# soc_estimation = ctrl.ControlSystemSimulation(soc_ctrl)

# # Provide input values from variables
# voltage_value = 5.12  # Replace with your desired voltage value
# current_value = 4.4  # Replace with your desired current value

# # Calculate SoC using fuzzy logic
# soc_estimation.input['voltage'] = voltage_value
# soc_estimation.input['current'] = current_value

# # Compute the result
# soc_estimation.compute()

# # Print the results
# print(f"Voltage: {voltage_value} V, Current: {current_value} A")
# print(f"Estimated SoC: {soc_estimation.output['soc']:.2f}%")
# print("--------------")


import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Battery parameters
Q = 100  # Battery capacity in Ah
Vmax = 4.2  # Maximum battery voltage in V
Vmin = 3.0  # Minimum battery voltage in V
I = -10.0  # Battery current in A (negative for discharge, positive for charge)
dt = 1  # Time interval in seconds
tmax = 100  # Number of time steps

# Initialize SoC using Coulomb counting method
SoC_CCM = 1.0

# Initialize arrays to store results
actual_SoC_voltage = np.zeros(tmax)
estimated_SoC_CCM = np.zeros(tmax)
error = np.zeros(tmax)
change_in_error = np.zeros(tmax - 1)

# OCV Method
def calculate_SoC_voltage(V):
    return (V - Vmin) / (Vmax - Vmin) * 100

# Coulomb Counting Method
def estimate_SoC_CCM(I, dt, SoC_CCM):
    dQ = I * dt
    SoC_CCM -= dQ / Q * 100
    return SoC_CCM

# Fuzzy Logic
# Define membership functions for error and change in error
error_range = np.arange(0, 101, 1)
change_in_error_range = np.arange(-100, 101, 1)

error_mf = ctrl.Antecedent(error_range, 'error')
change_in_error_mf = ctrl.Antecedent(change_in_error_range, 'change_in_error')
SoC_correction = ctrl.Consequent(error_range, 'SoC_correction')

# Define membership functions for error and change in error inputs
error_mf['low'] = fuzz.trimf(error_range, [0, 0, 20])
error_mf['medium'] = fuzz.trimf(error_range, [0, 50, 100])
error_mf['high'] = fuzz.trimf(error_range, [50, 100, 100])

change_in_error_mf['negative_large'] = fuzz.trimf(change_in_error_range, [-100, -100, -50])
change_in_error_mf['negative_small'] = fuzz.trimf(change_in_error_range, [-100, -50, 0])
change_in_error_mf['zero'] = fuzz.trimf(change_in_error_range, [-50, 0, 50])
change_in_error_mf['positive_small'] = fuzz.trimf(change_in_error_range, [0, 50, 100])
change_in_error_mf['positive_large'] = fuzz.trimf(change_in_error_range, [50, 100, 100])

# Define membership functions for SoC correction output
SoC_correction['reduce'] = fuzz.trimf(error_range, [0, 0, 50])
SoC_correction['maintain'] = fuzz.trimf(error_range, [0, 50, 100])
SoC_correction['increase'] = fuzz.trimf(error_range, [50, 100, 100])

# Define fuzzy rules
rule1 = ctrl.Rule(error_mf['low'] & change_in_error_mf['zero'], SoC_correction['maintain'])
rule2 = ctrl.Rule(error_mf['low'] & change_in_error_mf['positive_small'], SoC_correction['increase'])
rule3 = ctrl.Rule(error_mf['low'] & change_in_error_mf['positive_large'], SoC_correction['increase'])
rule4 = ctrl.Rule(error_mf['medium'] & change_in_error_mf['negative_large'], SoC_correction['reduce'])
rule5 = ctrl.Rule(error_mf['medium'] & change_in_error_mf['zero'], SoC_correction['maintain'])
rule6 = ctrl.Rule(error_mf['medium'] & change_in_error_mf['positive_small'], SoC_correction['increase'])
rule7 = ctrl.Rule(error_mf['high'] & change_in_error_mf['negative_small'], SoC_correction['reduce'])
rule8 = ctrl.Rule(error_mf['high'] & change_in_error_mf['zero'], SoC_correction['reduce'])
rule9 = ctrl.Rule(error_mf['high'] & change_in_error_mf['positive_small'], SoC_correction['maintain'])
rule10 = ctrl.Rule(error_mf['high'] & change_in_error_mf['positive_large'], SoC_correction['maintain'])

# Create fuzzy control system
SoC_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10])
SoC_correction_sim = ctrl.ControlSystemSimulation(SoC_ctrl)

# Battery SoC estimation process
for t in range(tmax):
    # OCV Method
    # Simulated battery voltage measurement (Replace with real sensor readings)
    V = np.random.uniform(Vmin, Vmax)  
    actual_SoC_voltage[t] = calculate_SoC_voltage(V)

    # Coulomb Counting Method
    SoC_CCM = estimate_SoC_CCM(I, dt, SoC_CCM)
    estimated_SoC_CCM[t] = SoC_CCM

    #### To check difference between both SoC's ####
    #print(["actual SoC: ",actual_SoC_voltage[t] ], ["estm_SoC: ", SoC_CCM/100])

    # Calculate error
    error[t] = abs(actual_SoC_voltage[t] - SoC_CCM)

    # Calculate change in error
    if t > 0:
        change_in_error[t - 1] = error[t] - error[t - 1]

    # Fuzzy Logic to correct SoC_CCM
    SoC_correction_sim.input['error'] = error[t]
    SoC_correction_sim.input['change_in_error'] = change_in_error[t - 1] if t > 0 else 0
    SoC_correction_sim.compute()
    SoC_correction_value = SoC_correction_sim.output['SoC_correction']

    # Apply SoC correction
    SoC_CCM += SoC_correction_value
    

# Display results
# plt.plot(actual_SoC_voltage, label="Actual SoC (OCV Method)")
# plt.plot(estimated_SoC_CCM, label="Estimated SoC (Coulomb Counting Method)")
# plt.xlabel("Time Steps")
# plt.ylabel("State of Charge (SoC)")
# plt.legend()
# plt.show()

# plt.plot(error, label="Error")
# plt.xlabel("Time Steps")
# plt.ylabel("Error")
# plt.legend()
# plt.show()

# plt.plot(change_in_error, label="Change in Error")
# plt.xlabel("Time Steps")
# plt.ylabel("Change in Error")
# plt.legend()
# plt.show()


#### Calculate change in error ####
# error_values = [5, 8, 10, 6, 3, 2, 1, 0, 2, 4]

# # Calculate the differences between consecutive error values
# error_diff = np.diff(error_values)

# # Shift the differences by one position
# change_in_error_values = np.insert(error_diff, 0, 0)

# print("Original Error Values:", error_values)
# print("Change in Error Values:", change_in_error_values)
