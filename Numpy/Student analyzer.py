import numpy as np
#Array creation for students
scores = np.random.randint(0,101,size=(10,3))
print(scores)

#Print array properties 
print(f'Shape:{scores.shape}')
print(f'Size:{scores.size}')
print(f'Data type:{scores.dtype}')

#Reshape array
scores_1d = scores.reshape(-1) #Reshapes to 1D array
scores_2d = scores.reshape(10,3) #Reshapes to 2D array

print('Score in 1D:',scores_1d)
print('Scores in 2D:',scores_2d)

#Change dtype
scores_float = scores.astype(float)

#Analysis
stud_avg = np.mean(scores, axis=1)
sub_avg = np.mean(scores, axis=0)

print("Student's average is:" ,stud_avg)
print("Subject average is:", sub_avg)
