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
# Step 1: Normalize Matrix R
# MOORA uses vector normalization
# rij = xij / sqrt(sum(xij^2))
# =========================

denominator = np.sqrt(np.sum(X ** 2, axis=0))
R = X / denominator

R_df = pd.DataFrame(R, index=cars, columns=criteria)

print("Step 1: Normalized Matrix R")
print(R_df)
print()


# =========================
# Step 2: AHP Weights
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

print("Step 2.1: AHP Weights")
print(weights_df)
print()


# =========================
# Step 2.2: Weighted Normalized Matrix V
# vij = rij * wj
# =========================

V = R * weights

V_df = pd.DataFrame(V, index=cars, columns=criteria)

print("Step 2.2: Weighted Normalized Matrix V")
print(V_df)
print()


# =========================
# Step 3: Define Benefit and Cost Criteria
# =========================

cost_criteria = [
    "Cost",
    "Fuel Efficiency",
    "Environmental Impact"
]

benefit_criteria = [
    "Performance",
    "Practicality",
    "Utility",
    "Warranty",
    "Drivability"
]

print("Step 3: Criteria Type")
criteria_type_df = pd.DataFrame({
    "Criteria": criteria,
    "Type": ["Cost" if c in cost_criteria else "Benefit" for c in criteria]
})
print(criteria_type_df)
print()


# =========================
# Step 4: MOORA Score
# MOORA Score = Sum(Benefit criteria) - Sum(Cost criteria)
# Higher score is better
# =========================

benefit_index = [criteria.index(c) for c in benefit_criteria]
cost_index = [criteria.index(c) for c in cost_criteria]

benefit_sum = np.sum(V[:, benefit_index], axis=1)
cost_sum = np.sum(V[:, cost_index], axis=1)

moora_score = benefit_sum - cost_sum

moora_df = pd.DataFrame({
    "Car": cars,
    "Benefit Sum": benefit_sum,
    "Cost Sum": cost_sum,
    "MOORA Score": moora_score
})

print("Step 4: MOORA Benefit Sum, Cost Sum, and Score")
print(moora_df)
print()


# =========================
# Step 5: Final MOORA Ranking
# Higher MOORA Score = Better
# =========================

moora_df["Rank"] = moora_df["MOORA Score"].rank(
    ascending=False,
    method="min"
).astype(int)

ranking_df = moora_df.sort_values("Rank")

print("Step 5: Final MOORA Ranking")
print(ranking_df)