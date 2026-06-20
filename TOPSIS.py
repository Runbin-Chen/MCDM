import numpy as np
import pandas as pd

# =========================
# 1. Alternatives
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

X = np.array([
    [41000, 4.8, 196, 566, 400, 8, 111, 9],      # Toyota Prius Hybrid
    [49000, 6.4, 204, 1028, 453, 8, 111, 9],     # Honda CR-V Hybrid, 36.3 ft3 ≈ 1028 L
    [37500, 5.5, 236, 1070, 794, 9, 129, 9],     # Toyota RAV4 Hybrid
    [40150, 4.5, 220, 575, 0, 10, 31, 5],        # Prius Plug-in SE, Utility N/A = 0
    [57600, 9.0, 247, 613, 1580, 5, 212, 8],     # Volvo XC60 B5 Mild Hybrid
    [42950, 6.2, 219, 1595, 680, 7, 145, 9]      # Mazda CX-50 Hybrid
])

# =========================
# 3. AHP weights
# =========================
# 这里先放你前面那组 AHP 权重
# 顺序必须和 criteria 一致

weights = np.array([
    0.2625,   # Cost
    0.1597,   # Fuel Efficiency
    0.0834,   # Performance
    0.1693,   # Practicality
    0.0930,   # Utility
    0.0864,   # Warranty
    0.0430,   # Environmental Impact
    0.1025    # Drivability
])

# 保证权重加起来等于 1
weights = weights / weights.sum()

# =========================
# 4. Criteria direction
# =========================
# 1 = benefit criterion, larger is better
# -1 = cost criterion, smaller is better

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
# 5. Vector normalization
# =========================

X_norm = X / np.sqrt((X ** 2).sum(axis=0))

# =========================
# 6. Weighted normalized matrix
# =========================

V = X_norm * weights

# =========================
# 7. Ideal best and ideal worst
# =========================

ideal_best = np.where(directions == 1, V.max(axis=0), V.min(axis=0))
ideal_worst = np.where(directions == 1, V.min(axis=0), V.max(axis=0))

# =========================
# 8. Distance to ideal best and worst
# =========================

distance_best = np.sqrt(((V - ideal_best) ** 2).sum(axis=1))
distance_worst = np.sqrt(((V - ideal_worst) ** 2).sum(axis=1))

# =========================
# 9. TOPSIS score
# =========================

score = distance_worst / (distance_best + distance_worst)

# =========================
# 10. Output ranking
# =========================

result = pd.DataFrame({
    "Car": cars,
    "TOPSIS Score": score
})

result["Rank"] = result["TOPSIS Score"].rank(
    ascending=False,
    method="min"
).astype(int)

result = result.sort_values("TOPSIS Score", ascending=False)

print(result.round(4))