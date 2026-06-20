

Original Decision Matrix X:
                              Cost  Fuel Efficiency  Performance  Practicality  Utility  Warranty  Environmental Impact  Drivability
Toyota Prius Hybrid        41000.0              4.8        196.0         566.0    400.0       8.0                 111.0          9.0
Honda CR-V Hybrid          49000.0              6.4        204.0        1028.0    453.0       8.0                 111.0          9.0
Toyota RAV4 LE AWD Hybrid  37500.0              5.5        236.0        1070.0    794.0       9.0                 129.0          9.0
Toyota Prius Plug-in SE    40150.0              4.5        220.0         575.0      0.0      10.0                  31.0          5.0
Volvo XC60 B5 Mild Hybrid  57600.0              9.0        247.0         613.0   1580.0       5.0                 212.0          8.0
Mazda CX-50 Hybrid         42950.0              6.2        219.0        1595.0    680.0       7.0                 145.0          9.0

Step 1: Normalized Matrix R
                             Cost  Fuel Efficiency  Performance  Practicality  Utility  Warranty  Environmental Impact  Drivability
Toyota Prius Hybrid        0.3702           0.3138       0.3620        0.2356   0.2011    0.4088                0.3374       0.4429
Honda CR-V Hybrid          0.4425           0.4184       0.3768        0.4279   0.2278    0.4088                0.3374       0.4429
Toyota RAV4 LE AWD Hybrid  0.3386           0.3596       0.4359        0.4454   0.3993    0.4599                0.3921       0.4429
Toyota Prius Plug-in SE    0.3626           0.2942       0.4064        0.2393   0.0000    0.5110                0.0942       0.2460
Volvo XC60 B5 Mild Hybrid  0.5202           0.5884       0.4562        0.2551   0.7945    0.2555                0.6445       0.3937
Mazda CX-50 Hybrid         0.3879           0.4054       0.4045        0.6639   0.3420    0.3577                0.4408       0.4429

Step 2.1: AHP Weights
               Criteria  AHP Weight
0                  Cost      0.2626
1       Fuel Efficiency      0.1597
2           Performance      0.0834
3          Practicality      0.1693
4               Utility      0.0930
5              Warranty      0.0864
6  Environmental Impact      0.0430
7           Drivability      0.1025

Step 2.2: Weighted Normalized Matrix V
                             Cost  Fuel Efficiency  Performance  Practicality  Utility  Warranty  Environmental Impact  Drivability
Toyota Prius Hybrid        0.0972           0.0501       0.0302        0.0399   0.0187    0.0353                0.0145       0.0454
Honda CR-V Hybrid          0.1162           0.0668       0.0314        0.0725   0.0212    0.0353                0.0145       0.0454
Toyota RAV4 LE AWD Hybrid  0.0889           0.0574       0.0364        0.0754   0.0371    0.0397                0.0169       0.0454
Toyota Prius Plug-in SE    0.0952           0.0470       0.0339        0.0405   0.0000    0.0442                0.0041       0.0252
Volvo XC60 B5 Mild Hybrid  0.1366           0.0940       0.0381        0.0432   0.0739    0.0221                0.0277       0.0404
Mazda CX-50 Hybrid         0.1018           0.0647       0.0337        0.1124   0.0318    0.0309                0.0190       0.0454

Step 3: Ideal Solutions A+ and A-
               Criteria     Type  A+ Positive Ideal  A- Negative Ideal
0                  Cost     Cost             0.0889             0.1366
1       Fuel Efficiency     Cost             0.0470             0.0940
2           Performance  Benefit             0.0381             0.0302
3          Practicality  Benefit             0.1124             0.0399
4               Utility  Benefit             0.0739             0.0000
5              Warranty  Benefit             0.0442             0.0221
6  Environmental Impact     Cost             0.0041             0.0277
7           Drivability  Benefit             0.0454             0.0252

Step 4: Separation Distances
                         Car  S+ Distance to A+  S- Distance to A-
0        Toyota Prius Hybrid             0.0929             0.0677
1          Honda CR-V Hybrid             0.0758             0.0585
2  Toyota RAV4 LE AWD Hybrid             0.0549             0.0844
3    Toyota Prius Plug-in SE             0.1053             0.0706
4  Volvo XC60 B5 Mild Hybrid             0.1017             0.0759
5         Mazda CX-50 Hybrid             0.0517             0.0944

Step 5: Similarity Score C*
                         Car      S+      S-  C* TOPSIS Score
0        Toyota Prius Hybrid  0.0929  0.0677           0.4214
1          Honda CR-V Hybrid  0.0758  0.0585           0.4356
2  Toyota RAV4 LE AWD Hybrid  0.0549  0.0844           0.6058
3    Toyota Prius Plug-in SE  0.1053  0.0706           0.4012
4  Volvo XC60 B5 Mild Hybrid  0.1017  0.0759           0.4274
5         Mazda CX-50 Hybrid  0.0517  0.0944           0.6462

Step 6: Final TOPSIS Ranking
                         Car      S+      S-  C* TOPSIS Score  Rank
5         Mazda CX-50 Hybrid  0.0517  0.0944           0.6462     1
2  Toyota RAV4 LE AWD Hybrid  0.0549  0.0844           0.6058     2
1          Honda CR-V Hybrid  0.0758  0.0585           0.4356     3
4  Volvo XC60 B5 Mild Hybrid  0.1017  0.0759           0.4274     4
0        Toyota Prius Hybrid  0.0929  0.0677           0.4214     5
3    Toyota Prius Plug-in SE  0.1053  0.0706           0.4012     6
(base) chenrunbin@chenrunbindeMacBook-Air MCDM % 