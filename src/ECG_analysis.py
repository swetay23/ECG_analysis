import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Load raw ECG data
data = pd.read_csv('../data/Data.csv')

# Simple R-peak detection using a threshold (in reality, you'd use more advanced methods)
peaks, _ = find_peaks(data['ECG_Signal'], height=0.9)  # Detect R-peaks above a threshold of 0.9

# Store the detected R-peaks
r_peaks = data.iloc[peaks]
r_peaks.to_csv('../results/r_peaks.csv', index=False)

# Plot the ECG signal with R-peaks
plt.plot(data['Time'], data['ECG_Signal'], label='ECG Signal')
plt.plot(data['Time'].iloc[peaks], data['ECG_Signal'].iloc[peaks], 'rx', label='R-peaks')
plt.legend()
plt.savefig('../results/plots/r_peaks_plot.png')
plt.show()

