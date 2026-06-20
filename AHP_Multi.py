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

# 每个人只需要填上三角数据
# 顺序是：
# C1-C2, C1-C3, C1-C4, C1-C5, C1-C6, C1-C7, C1-C8,
# C2-C3, C2-C4, C2-C5, C2-C6, C2-C7, C2-C8,
# C3-C4, C3-C5, C3-C6, C3-C7, C3-C8,
# C4-C5, C4-C6, C4-C7, C4-C8,
# C5-C6, C5-C7, C5-C8,
# C6-C7, C6-C8,
# C7-C8

person1 = [
    1.5, 2, 3, 2, 5, 5, 2,
    2, 1, 2, 3, 3, 1,
    0.5, 1, 0.5, 2, 1,
    3, 1.5, 3, 3,
    2, 2, 0.8,
    3, 0.8,
    0.4
]

# 把下面四组替换成其他4个人的评价
person2 = [
    1.5, 2, 3, 2, 5, 5, 2,
    2, 1, 2, 3, 3, 1,
    0.5, 1, 0.5, 2, 1,
    3, 1.5, 3, 3,
    2, 2, 0.8,
    3, 0.8,
    0.4
]

person3 = [
    1.5, 2, 3, 2, 5, 5, 2,
    2, 1, 2, 3, 3, 1,
    0.5, 1, 0.5, 2, 1,
    3, 1.5, 3, 3,
    2, 2, 0.8,
    3, 0.8,
    0.4
]

person4 = [
    1.5, 2, 3, 2, 5, 5, 2,
    2, 1, 2, 3, 3, 1,
    0.5, 1, 0.5, 2, 1,
    3, 1.5, 3, 3,
    2, 2, 0.8,
    3, 0.8,
    0.4
]

person5 = [
    1.5, 2, 3, 2, 5, 5, 2,
    2, 1, 2, 3, 3, 1,
    0.5, 1, 0.5, 2, 1,
    3, 1.5, 3, 3,
    2, 2, 0.8,
    3, 0.8,
    0.4
]

all_people = [person1, person2, person3, person4, person5]


def build_matrix(upper_values, n=8):
    A = np.ones((n, n))
    k = 0

    for i in range(n):
        for j in range(i + 1, n):
            A[i, j] = upper_values[k]
            A[j, i] = 1 / upper_values[k]
            k += 1

    return A


def ahp_weight(A):
    eigenvalues, eigenvectors = np.linalg.eig(A)

    max_index = np.argmax(eigenvalues.real)
    lambda_max = eigenvalues[max_index].real

    weights = eigenvectors[:, max_index].real
    weights = np.abs(weights)
    weights = weights / weights.sum()

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

    CR = CI / RI_dict[n]

    return weights, lambda_max, CI, CR


# 生成5个人的判断矩阵
matrices = np.array([build_matrix(person) for person in all_people])

# 用几何平均法合并5个人的判断矩阵
group_matrix = np.prod(matrices, axis=0) ** (1 / len(matrices))

# 计算最终小组权重
weights, lambda_max, CI, CR = ahp_weight(group_matrix)

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