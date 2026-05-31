### Plotting a fitted line using least squares method
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Data
t = np.array([0, 1, 2, 3], dtype=float)
y = np.array([2.0, 0.7, 0.3, 0.1], dtype=float)

# Model function
def f(t, x1, x2):
    return x1 * np.exp(x2 * t)

# Nonlinear least-squares fit
popt, pcov = curve_fit(f, t, y, p0=[2.0, -1.0])

x1_fit, x2_fit = popt

print(f"x1 = {x1_fit:.6f}")
print(f"x2 = {x2_fit:.6f}")

# Plot
t_plot = np.linspace(0, 3, 200)

plt.scatter(t, y, label="Data")
plt.plot(t_plot, f(t_plot, *popt), label="Least-squares fit")
plt.xlabel("t")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()







