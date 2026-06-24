import numpy as np
import pandas as pd

# ============================================================
# Criteria
# ============================================================

criteria = [
    "C1 Cost",
    "C2 Fuel Efficiency",
    "C3 Performance",
    "C4 Practicality",
    "C5 Utility",
    "C6 Warranty",
    "C7 Environmental Impact",
    "C8 Drivability"
]

# ============================================================
# AHP calculation function
# ============================================================

def ahp_weights_and_cr(M):
    M = np.array(M, dtype=float)
    n = M.shape[0]

    # Normalize each column
    column_sums = M.sum(axis=0)
    normalized_matrix = M / column_sums

    # Row average = weight
    weights = normalized_matrix.mean(axis=1)

    # Weighted sum vector
    weighted_sum = M @ weights

    # Consistency vector
    consistency_vector = weighted_sum / weights

    # Lambda max
    lambda_max = consistency_vector.mean()

    # Consistency index
    CI = (lambda_max - n) / (n - 1)

    # Random Index table
    RI_table = {
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

    RI = RI_table[n]

    if RI == 0:
        CR = 0
    else:
        CR = CI / RI

    return weights, lambda_max, CI, CR, normalized_matrix


def geometric_mean_group_matrix(matrices):
    matrices = np.array(matrices, dtype=float)
    group_matrix = np.prod(matrices, axis=0) ** (1 / matrices.shape[0])
    return group_matrix


# ============================================================
# Matrix 1
# ============================================================

M1 = np.array([
    [1,     2,     2,     3,     5,     4,     4,     5],
    [1/2,   1,     2,     2,     3,     3,     2,     4],
    [1/2,   1/2,   1,     1,     2,     1,     4,     4],
    [1/3,   1/2,   1,     1,     3,     3,     4,     5],
    [1/5,   1/3,   1/2,   1/3,   1,     1,     2,     2],
    [1/4,   1/3,   1,     1/3,   1,     1,     4,     4],
    [1/4,   1/2,   1/4,   1/4,   1/2,   1/4,   1,     1],
    [1/5,   1/4,   1/4,   1/5,   1/2,   1/4,   1,     1]
], dtype=float)


# ============================================================
# Matrix 2
# ============================================================

M2 = np.array([
    [1,       1.5,     2,       3,       2,       5,       5,       2],
    [1/1.5,   1,       2,       1,       2,       3,       3,       1],
    [1/2,     1/2,     1,       1/2,     1,       1/2,     2,       1],
    [1/3,     1,       2,       1,       3,       1.5,     3,       3],
    [1/2,     1/2,     1,       1/3,     1,       2,       2,       0.8],
    [1/5,     1/3,     2,       1/1.5,   1/2,     1,       3,       0.8],
    [1/5,     1/3,     1/2,     1/3,     1/2,     1/3,     1,       0.4],
    [1/2,     1,       1,       1/3,     1/0.8,   1/0.8,   1/0.4,   1]
], dtype=float)


# ============================================================
# Matrix 3
# ============================================================

M3 = np.array([
    [1,     1/2,   4,     2,     5,     3,     2,     1],
    [2,     1,     5,     3,     6,     4,     2,     2],
    [1/4,   1/5,   1,     1/3,   2,     1/2,   1/3,   1/3],
    [1/2,   1/3,   3,     1,     4,     2,     1,     1/2],
    [1/5,   1/6,   1/2,   1/4,   1,     1/3,   1/4,   1/5],
    [1/3,   1/4,   2,     1/2,   3,     1,     1/2,   1/3],
    [1/2,   1/2,   3,     1,     4,     2,     1,     1/2],
    [1,     1/2,   3,     2,     5,     3,     2,     1]
], dtype=float)


# ============================================================
# Matrix 4
# ============================================================

M4 = np.array([
    [1,     1/2,   9,     3,     5,     1,     9,     5],
    [2,     1,     9,     3,     5,     1,     9,     5],
    [1/9,   1/9,   1,     1/5,   1/3,   1/9,   1,     1/3],
    [1/3,   1/3,   5,     1,     2,     1/3,   5,     3],
    [1/5,   1/5,   3,     1/2,   1,     1/5,   3,     2],
    [1,     1,     9,     3,     5,     1,     9,     5],
    [1/9,   1/9,   1,     1/5,   1/3,   1/9,   1,     1/3],
    [1/5,   1/5,   3,     1/3,   1/2,   1/5,   3,     1]
], dtype=float)


# ============================================================
# Matrix 5
# ============================================================

M5 = np.array([
    [1,     1/2,   2,     1,     2,     1,     2,     1/2],
    [2,     1,     3,     2,     4,     2,     3,     2],
    [1/2,   1/3,   1,     1/2,   2,     1,     2,     1/2],
    [1,     1/2,   2,     1,     2,     2,     2,     1],
    [1/2,   1/4,   1/2,   1/2,   1,     1,     1,     1/2],
    [1,     1/2,   1,     1/2,   1,     1,     2,     1/2],
    [1/2,   1/3,   1/2,   1/2,   1,     1/2,   1,     1/2],
    [2,     1/2,   2,     1,     2,     2,     2,     1]
], dtype=float)


# ============================================================
# Put all matrices together
# ============================================================

matrices = [M1, M2, M3, M4, M5]


# ============================================================
# Individual AHP results
# ============================================================

individual_results = []
individual_weights_list = []

for i, M in enumerate(matrices, start=1):
    weights, lambda_max, CI, CR, normalized = ahp_weights_and_cr(M)
    individual_weights_list.append(weights)

    individual_results.append({
        "Person": f"Person {i}",
        "Lambda Max": lambda_max,
        "CI": CI,
        "CR": CR,
        "Acceptable": "Yes" if CR < 0.10 else "No"
    })

    print(f"\nPerson {i} Results")
    print("-" * 40)
    for c, w in zip(criteria, weights):
        print(f"{c}: {w:.4f}")
    print(f"Lambda Max = {lambda_max:.4f}")
    print(f"CI = {CI:.4f}")
    print(f"CR = {CR:.4f}")
    print("Consistency:", "Acceptable" if CR < 0.10 else "Not acceptable")


# ============================================================
# Group AHP matrix using geometric mean
# ============================================================

group_matrix = geometric_mean_group_matrix(matrices)

group_weights, group_lambda_max, group_CI, group_CR, group_normalized = ahp_weights_and_cr(group_matrix)


# ============================================================
# Print group result
# ============================================================

print("\n\nGroup AHP Results")
print("=" * 40)

print("\nGroup Weights:")
for c, w in zip(criteria, group_weights):
    print(f"{c}: {w:.4f}")

print(f"\nGroup Lambda Max = {group_lambda_max:.4f}")
print(f"Group CI = {group_CI:.4f}")
print(f"Group CR = {group_CR:.4f}")
print("Group Consistency:", "Acceptable" if group_CR < 0.10 else "Not acceptable")


# ============================================================
# Create dataframes
# ============================================================

individual_cr_df = pd.DataFrame(individual_results)

individual_weights_df = pd.DataFrame(
    individual_weights_list,
    columns=criteria,
    index=[f"Person {i}" for i in range(1, 6)]
)

group_matrix_df = pd.DataFrame(
    group_matrix,
    index=criteria,
    columns=criteria
)

group_normalized_df = pd.DataFrame(
    group_normalized,
    index=criteria,
    columns=criteria
)

group_weights_df = pd.DataFrame({
    "Criteria": criteria,
    "Group Weight": group_weights
})

group_cr_df = pd.DataFrame({
    "Metric": ["Lambda Max", "CI", "CR", "Acceptable"],
    "Value": [
        group_lambda_max,
        group_CI,
        group_CR,
        "Yes" if group_CR < 0.10 else "No"
    ]
})


# ============================================================
# Export to Excel
# ============================================================

output_file = "AHP_Group_Result.xlsx"

with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
    individual_cr_df.to_excel(writer, sheet_name="Individual CR", index=False)
    individual_weights_df.to_excel(writer, sheet_name="Individual Weights")
    group_matrix_df.to_excel(writer, sheet_name="Group Matrix")
    group_normalized_df.to_excel(writer, sheet_name="Group Normalized")
    group_weights_df.to_excel(writer, sheet_name="Group Weights", index=False)
    group_cr_df.to_excel(writer, sheet_name="Group CR", index=False)

print(f"\nExcel file saved as: {output_file}")