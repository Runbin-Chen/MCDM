import numpy as np
import pandas as pd

criteria = [
    "Cost",
    "Fuel Efficiency",
    "Performance",
    "Practicality",
    "Utility",
    "Warranty",
    "Environmental Impact",
    "Drivability"
]

A = np.array([
    [1,     1.5,   2,     3,     2,     5,     5,     2],
    [1/1.5, 1,     2,     1,     2,     3,     3,     1],
    [1/2,   1/2,   1,     0.5,   1,     0.5,   2,     1],
    [1/3,   1,     1/0.5, 1,     3,     1.5,   3,     3],
    [1/2,   1/2,   1,     1/3,   1,     2,     2,     0.8],
    [1/5,   1/3,   1/0.5, 1/1.5, 1/2,   1,     3,     0.8],
    [1/5,   1/3,   1/2,   1/3,   1/2,   1/3,   1,     0.4],
    [1/2,   1,     1,     1/3,   1/0.8, 1/0.8, 1/0.4, 1]
])

# Eigenvector method
eigenvalues, eigenvectors = np.linalg.eig(A)

max_index = np.argmax(eigenvalues.real)
lambda_max = eigenvalues[max_index].real

weights = eigenvectors[:, max_index].real
weights = np.abs(weights)
weights = weights / weights.sum()

# Consistency test
n = A.shape[0]
CI = (lambda_max - n) / (n - 1)

RI_dict = {
    1: 0.00,
    2: 0.00,
    3: 0.58,
    4: 0.90,
    5: 1.12,
    6: 1.24,
    7: 1.32,
    8: 1.41,
    9: 1.45,
    10: 1.49
}

RI = RI_dict[n]
CR = CI / RI

result = pd.DataFrame({
    "Criteria": criteria,
    "Weight": weights,
    "Percentage": weights * 100
})

result = result.sort_values("Weight", ascending=False)

print(result.round(4))

print("\nConsistency Test:")
print(f"lambda_max = {lambda_max:.4f}")
print(f"CI = {CI:.4f}")
print(f"CR = {CR:.4f}")

if CR < 0.1:
    print("Consistency is acceptable.")
else:
    print("Consistency is not acceptable.")