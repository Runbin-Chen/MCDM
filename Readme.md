## Raw Data
| Car | Cost | Fuel Efficiency | Performance | Practicality | Utility | Warranty | Environmental Impact | Drivability |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Toyota Prius Hybrid | 41000 | 4.8 | 196 | 566 | 400 | 8 | 111 | 9 |
| Honda CR-V Hybrid | 49000 | 6.4 | 204 | 1028 | 453 | 8 | 111 | 9 |
| Toyota RAV4 LE AWD Hybrid | 37500 | 5.5 | 236 | 1070 | 794 | 9 | 129 | 9 |
| Toyota Prius Plug-in SE | 40150 | 4.5 | 220 | 575 | 0 | 10 | 31 | 5 |
| Volvo XC60 B5 Mild Hybrid | 57600 | 9.0 | 247 | 613 | 1580 | 5 | 212 | 8 |
| Mazda CX-50 Hybrid | 42950 | 6.2 | 219 | 1595 | 680 | 7 | 145 | 9 |

---

## AHP Criteria Weights

| Criteria | Weight | Percentage |
|---|---:|---:|
| Cost | 0.2224 | 22.24% |
| Fuel Efficiency | 0.2399 | 23.99% |
| Performance | 0.0683 | 6.83% |
| Practicality | 0.1443 | 14.43% |
| Utility | 0.0645 | 6.45% |
| Warranty | 0.1119 | 11.19% |
| Environmental Impact | 0.0542 | 5.42% |
| Drivability | 0.0945 | 9.45% |

---


# Updated TOPSIS Analysis Results

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

| Criteria             | AHP Weight | Percentage |
| -------------------- | ---------: | ---------: |
| Cost                 |     0.2224 |     22.24% |
| Fuel Efficiency      |     0.2399 |     23.99% |
| Performance          |     0.0683 |      6.83% |
| Practicality         |     0.1443 |     14.43% |
| Utility              |     0.0645 |      6.45% |
| Warranty             |     0.1119 |     11.19% |
| Environmental Impact |     0.0542 |      5.42% |
| Drivability          |     0.0945 |      9.45% |

---

## Step 2.2: Weighted Normalized Matrix $V$

| Car                       |   Cost | Fuel Efficiency | Performance | Practicality | Utility | Warranty | Environmental Impact | Drivability |
| ------------------------- | -----: | --------------: | ----------: | -----------: | ------: | -------: | -------------------: | ----------: |
| Toyota Prius Hybrid       | 0.0823 |          0.0753 |      0.0247 |       0.0340 |  0.0130 |   0.0457 |               0.0183 |      0.0419 |
| Honda CR-V Hybrid         | 0.0984 |          0.1004 |      0.0257 |       0.0617 |  0.0147 |   0.0457 |               0.0183 |      0.0419 |
| Toyota RAV4 LE AWD Hybrid | 0.0753 |          0.0863 |      0.0298 |       0.0643 |  0.0258 |   0.0515 |               0.0213 |      0.0419 |
| Toyota Prius Plug-in SE   | 0.0806 |          0.0706 |      0.0278 |       0.0345 |  0.0000 |   0.0572 |               0.0051 |      0.0233 |
| Volvo XC60 B5 Mild Hybrid | 0.1157 |          0.1412 |      0.0312 |       0.0368 |  0.0512 |   0.0286 |               0.0349 |      0.0372 |
| Mazda CX-50 Hybrid        | 0.0863 |          0.0972 |      0.0276 |       0.0958 |  0.0221 |   0.0400 |               0.0239 |      0.0419 |

---

## Step 3: Ideal Solutions $A^+$ and $A^-$

| Criteria             | Type    | $A^+$ Positive Ideal | $A^-$ Negative Ideal |
| -------------------- | ------- | -------------------: | -------------------: |
| Cost                 | Cost    |               0.0753 |               0.1157 |
| Fuel Efficiency      | Cost    |               0.0706 |               0.1412 |
| Performance          | Benefit |               0.0312 |               0.0247 |
| Practicality         | Benefit |               0.0958 |               0.0340 |
| Utility              | Benefit |               0.0512 |               0.0000 |
| Warranty             | Benefit |               0.0572 |               0.0286 |
| Environmental Impact | Cost    |               0.0051 |               0.0349 |
| Drivability          | Benefit |               0.0419 |               0.0233 |

---

## Step 4: Separation Distances

| Car                       | $S^+$ Distance to $A^+$ | $S^-$ Distance to $A^-$ |
| ------------------------- | ----------------------: | ----------------------: |
| Toyota Prius Hybrid       |                  0.0755 |                  0.0808 |
| Honda CR-V Hybrid         |                  0.0652 |                  0.0622 |
| Toyota RAV4 LE AWD Hybrid |                  0.0467 |                  0.0855 |
| Toyota Prius Plug-in SE   |                  0.0823 |                  0.0890 |
| Volvo XC60 B5 Mild Hybrid |                  0.1087 |                  0.0536 |
| Mazda CX-50 Hybrid        |                  0.0484 |                  0.0878 |

---

## Step 5: Similarity Score $C^*$

The TOPSIS similarity score is calculated as:

$$
C_i^* = \frac{S_i^-}{S_i^+ + S_i^-}
$$

| Car                       |  $S^+$ |  $S^-$ | $C^*$ TOPSIS Score |
| ------------------------- | -----: | -----: | -----------------: |
| Toyota Prius Hybrid       | 0.0755 | 0.0808 |             0.5171 |
| Honda CR-V Hybrid         | 0.0652 | 0.0622 |             0.4881 |
| Toyota RAV4 LE AWD Hybrid | 0.0467 | 0.0855 |             0.6464 |
| Toyota Prius Plug-in SE   | 0.0823 | 0.0890 |             0.5198 |
| Volvo XC60 B5 Mild Hybrid | 0.1087 | 0.0536 |             0.3301 |
| Mazda CX-50 Hybrid        | 0.0484 | 0.0878 |             0.6446 |

---

## Step 6: Final TOPSIS Ranking

| Rank | Car                       |  $S^+$ |  $S^-$ | $C^*$ TOPSIS Score |
| ---: | ------------------------- | -----: | -----: | -----------------: |
|    1 | Toyota RAV4 LE AWD Hybrid | 0.0467 | 0.0855 |             0.6464 |
|    2 | Mazda CX-50 Hybrid        | 0.0484 | 0.0878 |             0.6446 |
|    3 | Toyota Prius Plug-in SE   | 0.0823 | 0.0890 |             0.5198 |
|    4 | Toyota Prius Hybrid       | 0.0755 | 0.0808 |             0.5171 |
|    5 | Honda CR-V Hybrid         | 0.0652 | 0.0622 |             0.4881 |
|    6 | Volvo XC60 B5 Mild Hybrid | 0.1087 | 0.0536 |             0.3301 |

---

## Conclusion

Based on the updated AHP weights and TOPSIS calculation, the **Toyota RAV4 LE AWD Hybrid** ranks first with the highest TOPSIS score of **0.6464**. The **Mazda CX-50 Hybrid** ranks second with a very close score of **0.6446**, indicating that both vehicles perform strongly under the current evaluation framework.

The ranking is mainly influenced by the high weights assigned to **Fuel Efficiency** and **Cost**, which are both cost-type criteria. Therefore, vehicles with lower fuel consumption and lower purchase cost receive stronger advantages. The **Toyota RAV4 LE AWD Hybrid** performs well because it has the lowest cost among the alternatives, strong performance, good practicality, high utility, and a strong warranty score.

The **Volvo XC60 B5 Mild Hybrid** ranks last because it has the highest cost, highest fuel consumption, and highest environmental impact among the alternatives, even though it performs well in utility and performance.
