## AHP Criteria Weights

| Rank | Criteria             | Weight | Percentage |
| ---: | -------------------- | -----: | ---------: |
|    1 | Fuel Efficiency      | 0.2407 |   24.0706% |
|    2 | Cost                 | 0.2236 |   22.3631% |
|    3 | Practicality         | 0.1441 |   14.4143% |
|    4 | Warranty             | 0.1114 |   11.1379% |
|    5 | Drivability          | 0.0940 |    9.3963% |
|    6 | Performance          | 0.0680 |    6.7976% |
|    7 | Utility              | 0.0642 |    6.4206% |
|    8 | Environmental Impact | 0.0540 |    5.3996% |

---

## Consistency Test

| Indicator        |  Value |
| ---------------- | -----: |
| $\lambda_{\max}$ | 8.0839 |
| CI               | 0.0120 |
| CR               | 0.0085 |

Since the consistency ratio is:

$$
CR = 0.0085 < 0.10
$$

the consistency of the AHP pairwise comparison matrix is **acceptable**.



# TOPSIS Analysis Results

## Original Decision Matrix $X$

| Car                       |    Cost | Fuel Efficiency | Performance | Practicality | Utility | Warranty | Environmental Impact | Drivability |
| ------------------------- | ------: | --------------: | ----------: | -----------: | ------: | -------: | -------------------: | ----------: |
| Toyota Prius Hybrid       | 41000.0 |             4.8 |       196.0 |        566.0 |   400.0 |      8.0 |                111.0 |         9.0 |
| Honda CR-V Hybrid         | 49000.0 |             6.4 |       204.0 |       1028.0 |   453.0 |      8.0 |                111.0 |         9.0 |
| Toyota RAV4 LE AWD Hybrid | 37500.0 |             5.5 |       236.0 |       1070.0 |   794.0 |      9.0 |                129.0 |         9.0 |
| Toyota Prius Plug-in SE   | 40150.0 |             4.5 |       220.0 |        575.0 |     0.0 |     10.0 |                 31.0 |         5.0 |
| Volvo XC60 B5 Mild Hybrid | 57600.0 |             9.0 |       247.0 |        613.0 |  1580.0 |      5.0 |                212.0 |         8.0 |
| Mazda CX-50 Hybrid        | 42950.0 |             6.2 |       219.0 |       1595.0 |   680.0 |      7.0 |                145.0 |         9.0 |

---

## Step 1: Normalized Matrix $R$

| Car                       |   Cost | Fuel Efficiency | Performance | Practicality | Utility | Warranty | Environmental Impact | Drivability |
| ------------------------- | -----: | --------------: | ----------: | -----------: | ------: | -------: | -------------------: | ----------: |
| Toyota Prius Hybrid       | 0.3702 |          0.3138 |      0.3620 |       0.2356 |  0.2011 |   0.4088 |               0.3374 |      0.4429 |
| Honda CR-V Hybrid         | 0.4425 |          0.4184 |      0.3768 |       0.4279 |  0.2278 |   0.4088 |               0.3374 |      0.4429 |
| Toyota RAV4 LE AWD Hybrid | 0.3386 |          0.3596 |      0.4359 |       0.4454 |  0.3993 |   0.4599 |               0.3921 |      0.4429 |
| Toyota Prius Plug-in SE   | 0.3626 |          0.2942 |      0.4064 |       0.2393 |  0.0000 |   0.5110 |               0.0942 |      0.2460 |
| Volvo XC60 B5 Mild Hybrid | 0.5202 |          0.5884 |      0.4562 |       0.2551 |  0.7945 |   0.2555 |               0.6445 |      0.3937 |
| Mazda CX-50 Hybrid        | 0.3879 |          0.4054 |      0.4045 |       0.6639 |  0.3420 |   0.3577 |               0.4408 |      0.4429 |

---

## Step 2.1: AHP Weights

| Criteria             | AHP Weight |
| -------------------- | ---------: |
| Cost                 |     0.2626 |
| Fuel Efficiency      |     0.1597 |
| Performance          |     0.0834 |
| Practicality         |     0.1693 |
| Utility              |     0.0930 |
| Warranty             |     0.0864 |
| Environmental Impact |     0.0430 |
| Drivability          |     0.1025 |

---

## Step 2.2: Weighted Normalized Matrix $V$

| Car                       |   Cost | Fuel Efficiency | Performance | Practicality | Utility | Warranty | Environmental Impact | Drivability |
| ------------------------- | -----: | --------------: | ----------: | -----------: | ------: | -------: | -------------------: | ----------: |
| Toyota Prius Hybrid       | 0.0972 |          0.0501 |      0.0302 |       0.0399 |  0.0187 |   0.0353 |               0.0145 |      0.0454 |
| Honda CR-V Hybrid         | 0.1162 |          0.0668 |      0.0314 |       0.0725 |  0.0212 |   0.0353 |               0.0145 |      0.0454 |
| Toyota RAV4 LE AWD Hybrid | 0.0889 |          0.0574 |      0.0364 |       0.0754 |  0.0371 |   0.0397 |               0.0169 |      0.0454 |
| Toyota Prius Plug-in SE   | 0.0952 |          0.0470 |      0.0339 |       0.0405 |  0.0000 |   0.0442 |               0.0041 |      0.0252 |
| Volvo XC60 B5 Mild Hybrid | 0.1366 |          0.0940 |      0.0381 |       0.0432 |  0.0739 |   0.0221 |               0.0277 |      0.0404 |
| Mazda CX-50 Hybrid        | 0.1018 |          0.0647 |      0.0337 |       0.1124 |  0.0318 |   0.0309 |               0.0190 |      0.0454 |

---

## Step 3: Ideal Solutions $A^+$ and $A^-$

| Criteria             | Type    | $A^+$ Positive Ideal | $A^-$ Negative Ideal |
| -------------------- | ------- | -------------------: | -------------------: |
| Cost                 | Cost    |               0.0889 |               0.1366 |
| Fuel Efficiency      | Cost    |               0.0470 |               0.0940 |
| Performance          | Benefit |               0.0381 |               0.0302 |
| Practicality         | Benefit |               0.1124 |               0.0399 |
| Utility              | Benefit |               0.0739 |               0.0000 |
| Warranty             | Benefit |               0.0442 |               0.0221 |
| Environmental Impact | Cost    |               0.0041 |               0.0277 |
| Drivability          | Benefit |               0.0454 |               0.0252 |

---

## Step 4: Separation Distances

| Car                       | $S^+$ Distance to $A^+$ | $S^-$ Distance to $A^-$ |
| ------------------------- | ----------------------: | ----------------------: |
| Toyota Prius Hybrid       |                  0.0929 |                  0.0677 |
| Honda CR-V Hybrid         |                  0.0758 |                  0.0585 |
| Toyota RAV4 LE AWD Hybrid |                  0.0549 |                  0.0844 |
| Toyota Prius Plug-in SE   |                  0.1053 |                  0.0706 |
| Volvo XC60 B5 Mild Hybrid |                  0.1017 |                  0.0759 |
| Mazda CX-50 Hybrid        |                  0.0517 |                  0.0944 |

---

## Step 5: Similarity Score $C^*$

| Car                       |  $S^+$ |  $S^-$ | $C^*$ TOPSIS Score |
| ------------------------- | -----: | -----: | -----------------: |
| Toyota Prius Hybrid       | 0.0929 | 0.0677 |             0.4214 |
| Honda CR-V Hybrid         | 0.0758 | 0.0585 |             0.4356 |
| Toyota RAV4 LE AWD Hybrid | 0.0549 | 0.0844 |             0.6058 |
| Toyota Prius Plug-in SE   | 0.1053 | 0.0706 |             0.4012 |
| Volvo XC60 B5 Mild Hybrid | 0.1017 | 0.0759 |             0.4274 |
| Mazda CX-50 Hybrid        | 0.0517 | 0.0944 |             0.6462 |

The TOPSIS similarity score is calculated as:

$$
C_i^* = \frac{S_i^-}{S_i^+ + S_i^-}
$$

A higher $C^*$ value means the alternative is closer to the positive ideal solution and farther from the negative ideal solution.

---

## Step 6: Final TOPSIS Ranking

| Rank | Car                       |  $S^+$ |  $S^-$ | $C^*$ TOPSIS Score |
| ---: | ------------------------- | -----: | -----: | -----------------: |
|    1 | Mazda CX-50 Hybrid        | 0.0517 | 0.0944 |             0.6462 |
|    2 | Toyota RAV4 LE AWD Hybrid | 0.0549 | 0.0844 |             0.6058 |
|    3 | Honda CR-V Hybrid         | 0.0758 | 0.0585 |             0.4356 |
|    4 | Volvo XC60 B5 Mild Hybrid | 0.1017 | 0.0759 |             0.4274 |
|    5 | Toyota Prius Hybrid       | 0.0929 | 0.0677 |             0.4214 |
|    6 | Toyota Prius Plug-in SE   | 0.1053 | 0.0706 |             0.4012 |

---

## Conclusion

Based on the TOPSIS results, the **Mazda CX-50 Hybrid** ranks first with the highest similarity score of **0.6462**, followed by the **Toyota RAV4 LE AWD Hybrid** with a score of **0.6058**.

This means that, under the selected AHP weights and TOPSIS evaluation criteria, the Mazda CX-50 Hybrid is the closest alternative to the positive ideal solution. Its strong performance mainly comes from its high practicality score, competitive overall balance, and relatively strong utility compared with other alternatives.

The Toyota RAV4 LE AWD Hybrid also performs well, especially because of its lower cost, strong performance, high utility, and good warranty score. The Toyota Prius Plug-in SE ranks last mainly because of its low utility value and lower drivability score, even though it has strong fuel efficiency and environmental performance.
