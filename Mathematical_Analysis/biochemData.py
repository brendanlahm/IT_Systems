### Plotting the biochem data
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Data Assignments
t = np.array([
    6, 12, 18, 24, 30, 36,
    42, 48, 54, 60, 66, 72,
    78, 84, 90, 96, 102, 108,
    114, 120, 126, 132, 138, 144,
    150, 156, 162, 168, 174, 180
], dtype=float)
y = np.array([24.19, 35.34, 43.43, 42.63, 49.92, 51.53, 57.39, 59.56, 55.60, 51.91, 58.27, 62.99, 52.99, 53.83, 59.37, 62.35, 61.84, 61.62, 49.64, 57.81, 54.79, 50.38, 43.85, 45.16, 46.72, 40.68, 35.14, 45.47, 42.40, 55.21], dtype=float)

# Model function
def g(t, x1, x2, x3):
    return (
        x1
        * np.exp(-(x2**2 + x3**2) * t)
        * np.sinh(x3**2 * t)
        / (x3**2)
    )

# Initial values suggested in the sheet
p0 = [10.0, 0.05, 0.10]

# Nonlinear least-squares fit
#popt, pcov = curve_fit(
#    g,
#    t,
#    y,
#    p0=p0,
#    bounds=([0, 0, 0], [1000, 1, 1]),
#    maxfev=10000
#)

popt, pcov = curve_fit(g, t, y, p0=[3.5, 0.05, 0.15])

x1_fit, x2_fit, x3_fit = popt

print(f"x1 = {x1_fit:.6f}")
print(f"x2 = {x2_fit:.6f}")
print(f"x3 = {x3_fit:.6f}")

# Residual sum of squares
rss = np.sum((y - g(t, *popt))**2)
print(f"RSS = {rss:.6f}")

# Plot
t_plot = np.linspace(0, 180, 1000)

plt.scatter(t, y, label="Data")
plt.plot(t_plot, g(t_plot, *popt), label="Least-squares fit")
plt.xlabel("t")
plt.ylabel("DNA concentration")
plt.legend()
plt.grid(True)
plt.show()





