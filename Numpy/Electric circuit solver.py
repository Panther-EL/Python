import numpy as np 
                        #Electric circuit solver


def solve_current(R1,R2,R3,R4,v1,v2,v3):
    a = np.array([
    [-R1+R2, -R2, 0],
    [-R2, R2+R3, 0],
    [0, R3, R3+R4]
]) #values for resistance

    b = np.array([v1,v2,v3]) #values for voltages
    return np.linalg.solve(a,b)

#Test case
currents = solve_current(4,6,5,10,12,9,15)
print('Currents in amperes(A):',currents)
