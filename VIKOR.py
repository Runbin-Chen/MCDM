import numpy as np
import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)
pd.set_option("display.float_format", "{:.4f}".format)

# =========================
# Alternatives and Criteria
# =========================

cars = [
    "Toyota Prius Hybrid",
    "Honda CR-V Hybrid",
    "Toyota RAV4 LE AWD Hybrid",
    "Toyota Prius Plug-in SE",
    "Volvo XC60 B5 Mild Hybrid",
    "Mazda CX-50 Hybrid"
]

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

# =========================
# Raw Decision Matrix X
# =========================

X = np.array([
    [41000.0, 4.8, 196.0, 566.0, 400.0, 8.0, 111.0, 9.0],
    [49000.0, 6.4, 204.0, 1028.0, 453.0, 8.0, 111.0, 9.0],
    [37500.0, 5.5, 236.0, 1070.0, 794.0, 9.0, 129.0, 9.0],
    [40150.0, 4.5, 220.0, 575.0, 400.0, 10.0, 31.0, 5.0],
    [57600.0, 9.0, 247.0, 613.0, 1580.0, 5.0, 212.0, 8.0],
    [42950.0, 6.2, 219.0, 1595.0, 680.0, 7.0, 145.0, 9.0]
])

X_df = pd.DataFrame(X, index=cars, columns=criteria)

print("Original Decision Matrix X:")
print(X_df)
print()


# =========================
# Step 1: AHP Weights
# =========================

weights = np.array([
    0.2224,  # Cost
    0.2399,  # Fuel Efficiency
    0.0683,  # Performance
    0.1443,  # Practicality
    0.0645,  # Utility
    0.1119,  # Warranty
    0.0542,  # Environmental Impact
    0.0945   # Drivability
])

weights_df = pd.DataFrame({
    "Criteria": criteria,
    "AHP Weight": weights
})

print("Step 1: AHP Weights")
print(weights_df)
print()


# =========================
# Step 2: Define Criteria Types
# =========================

criteria_type = [
    "Cost",      # Cost
    "Cost",      # Fuel Efficiency
    "Benefit",   # Performance
    "Benefit",   # Practicality
    "Benefit",   # Utility
    "Benefit",   # Warranty
    "Cost",      # Environmental Impact
    "Benefit"    # Drivability
]

criteria_type_df = pd.DataFrame({
    "Criteria": criteria,
    "Type": criteria_type
})

print("Step 2: Criteria Type")
print(criteria_type_df)
print()


# =========================
# Step 3: Determine Best and Worst Values
# For benefit criteria: best = max, worst = min
# For cost criteria: best = min, worst = max
# =========================

best_values = []
worst_values = []

for j, c_type in enumerate(criteria_type):
    if c_type == "Benefit":
        best_values.append(np.max(X[:, j]))
        worst_values.append(np.min(X[:, j]))
    else:
        best_values.append(np.min(X[:, j]))
        worst_values.append(np.max(X[:, j]))

best_values = np.array(best_values)
worst_values = np.array(worst_values)

best_worst_df = pd.DataFrame({
    "Criteria": criteria,
    "Type": criteria_type,
    "Best f*": best_values,
    "Worst f-": worst_values
})

print("Step 3: Best and Worst Values")
print(best_worst_df)
print()


# =========================
# Step 4: Calculate Normalized Regret Matrix D
# D = 0 means best performance
# D = 1 means worst performance
# =========================

D = np.zeros_like(X, dtype=float)

for j, c_type in enumerate(criteria_type):
    denominator = abs(best_values[j] - worst_values[j])
    
    if denominator == 0:
        D[:, j] = 0
    else:
        if c_type == "Benefit":
            D[:, j] = (best_values[j] - X[:, j]) / denominator
        else:
            D[:, j] = (X[:, j] - best_values[j]) / denominator

D_df = pd.DataFrame(D, index=cars, columns=criteria)

print("Step 4: Normalized Regret Matrix D")
print(D_df)
print()


# =========================
# Step 5: Weighted Regret Matrix
# =========================

WD = D * weights

WD_df = pd.DataFrame(WD, index=cars, columns=criteria)

print("Step 5: Weighted Regret Matrix")
print(WD_df)
print()


# =========================
# Step 6: Calculate S and R
# S = total weighted regret
# R = maximum weighted regret
# =========================

S = np.sum(WD, axis=1)
R = np.max(WD, axis=1)

SR_df = pd.DataFrame({
    "Car": cars,
    "S": S,
    "R": R
})

print("Step 6: S and R Values")
print(SR_df)
print()


# =========================
# Step 7: Calculate VIKOR Q Score
# v = 0.5 is commonly used
# Lower Q score means better alternative
# =========================

v = 0.5

S_best = np.min(S)
S_worst = np.max(S)

R_best = np.min(R)
R_worst = np.max(R)

Q = (
    v * (S - S_best) / (S_worst - S_best)
    + (1 - v) * (R - R_best) / (R_worst - R_best)
)

vikor_df = pd.DataFrame({
    "Car": cars,
    "S": S,
    "R": R,
    "Q VIKOR Score": Q
})

print("Step 7: VIKOR Q Score")
print(vikor_df)
print()


# =========================
# Step 8: Final VIKOR Ranking
# Lower Q score = better
# =========================

vikor_df["Rank"] = vikor_df["Q VIKOR Score"].rank(
    ascending=True,
    method="min"
).astype(int)

ranking_df = vikor_df.sort_values("Rank")

print("Step 8: Final VIKOR Ranking")
print(ranking_df)