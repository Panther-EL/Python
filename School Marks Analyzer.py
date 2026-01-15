import numpy as np
                                                #School Marks Analyzer
a = np.array([
        [70,65,80],
        [60,75,70],
        [90,85,95]
    ])

b = np.array([74,69,92])
weights = np.linalg.solve(a,b)
print('Weights:',weights)
