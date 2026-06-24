import numpy as np
import pandas as pd

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
    [41000, 4.8, 196, 566, 400, 8, 111, 9],
    [49000, 6.4, 204, 1028, 453, 8, 111, 9],
    [37500, 5.5, 236, 1070, 794, 9, 129, 9],
    [40150, 4.5, 220, 575, 0, 10, 31, 5],
    [57600, 9.0, 247, 613, 1580, 5, 212, 8],
    [42950, 6.2, 219, 1595, 680, 7, 145, 9]
], dtype=float)



# =========================
# 2. Raw decision matrix
# =========================
# Cost: CAD
# Fuel Efficiency: L/100 km
# Performance: horsepower
# Practicality: cargo volume, L
# Utility: towing capacity, kg
# Warranty: manually converted score
# Environmental Impact: g CO2/km
# Drivability: manually converted score

# Warranty:
# 10 = very strong warranty
# 8 = strong hybrid/battery warranty
# 5 = standard warranty

# Drivability:
# 9 = AWD or e-AWD
# 8 = AWD
# 5 = FWD only

# =========================
# AHP Weights
# Replace this with your final AHP weights
# Order must match criteria
# =========================

weights = np.array([
    0.2224,   # Cost
    0.2399,   # Fuel Efficiency
    0.0683,   # Performance
    0.1443,   # Practicality
    0.0645,   # Utility
    0.1119,   # Warranty
    0.0542,   # Environmental Impact
    0.0945    # Drivability
])

weights = weights / weights.sum()

# =========================
# Criteria Direction
# 1 = benefit, larger is better
# -1 = cost, smaller is better
# =========================

directions = np.array([
    -1,   # Cost
    -1,   # Fuel Efficiency
     1,   # Performance
     1,   # Practicality
     1,   # Utility
     1,   # Warranty
    -1,   # Environmental Impact
     1    # Drivability
])

# =========================
# Display Raw Matrix
# =========================

df_X = pd.DataFrame(X, index=cars, columns=criteria)

print("\nOriginal Decision Matrix X:")
print(df_X.round(4))


# ============================================================
# Step 1: Normalize
# r_ij = x_ij / sqrt(sum(x_ij^2))
# ============================================================

denominator = np.sqrt((X ** 2).sum(axis=0))
R = X / denominator

df_R = pd.DataFrame(R, index=cars, columns=criteria)

print("\nStep 1: Normalized Matrix R")
print(df_R.round(4))


# ============================================================
# Step 2: Weighted Normalized Matrix
# v_ij = w_j * r_ij
# ============================================================

V = R * weights

df_weights = pd.DataFrame({
    "Criteria": criteria,
    "AHP Weight": weights
})

df_V = pd.DataFrame(V, index=cars, columns=criteria)

print("\nStep 2.1: AHP Weights")
print(df_weights.round(4))

print("\nStep 2.2: Weighted Normalized Matrix V")
print(df_V.round(4))


# ============================================================
# Step 3: Ideal Solutions
# For benefit criteria: A+ = max, A- = min
# For cost criteria:    A+ = min, A- = max
# ============================================================

A_plus = np.where(directions == 1, V.max(axis=0), V.min(axis=0))
A_minus = np.where(directions == 1, V.min(axis=0), V.max(axis=0))

df_ideal = pd.DataFrame({
    "Criteria": criteria,
    "Type": ["Benefit" if d == 1 else "Cost" for d in directions],
    "A+ Positive Ideal": A_plus,
    "A- Negative Ideal": A_minus
})

print("\nStep 3: Ideal Solutions A+ and A-")
print(df_ideal.round(4))


# ============================================================
# Step 4: Separation Distance
# S+ = distance to A+
# S- = distance to A-
# ============================================================

S_plus = np.sqrt(((V - A_plus) ** 2).sum(axis=1))
S_minus = np.sqrt(((V - A_minus) ** 2).sum(axis=1))

df_distance = pd.DataFrame({
    "Car": cars,
    "S+ Distance to A+": S_plus,
    "S- Distance to A-": S_minus
})

print("\nStep 4: Separation Distances")
print(df_distance.round(4))


# ============================================================
# Step 5: Similarity Score
# C* = S- / (S+ + S-)
# Higher C* = better
# ============================================================

C_star = S_minus / (S_plus + S_minus)

df_score = pd.DataFrame({
    "Car": cars,
    "S+": S_plus,
    "S-": S_minus,
    "C* TOPSIS Score": C_star
})

print("\nStep 5: Similarity Score C*")
print(df_score.round(4))


# ============================================================
# Step 6: Rank
# Rank alternatives by C* in descending order
# ============================================================

df_score["Rank"] = df_score["C* TOPSIS Score"].rank(
    ascending=False,
    method="min"
).astype(int)

final_result = df_score.sort_values("C* TOPSIS Score", ascending=False)

print("\nStep 6: Final TOPSIS Ranking")
print(final_result.round(4))