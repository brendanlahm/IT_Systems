### Plotting using the Gauss–Newton Jacobian (not working, too many values to unpack!)
import numpy as np
from scipy.optimize import curve_fit

t = np.array([0, 1, 2, 3], dtype=float)
y = np.array([2.0, 0.7, 0.3, 0.1], dtype=float)

def f(t, x1, x2):
    return x1 * np.exp(x2 * t)

def jac(t, x1, x2):
    e = np.exp(x2 * t)
    return np.column_stack([
        e,
        x1 * t * e
    ])

popt, pcov = curve_fit(
    f,
    t,
    y,
    p0=[2.0, -1.0],
    jac=jac
)

print("Parameters:", popt)