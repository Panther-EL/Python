                    #Student performance normalization using broadcasting                                
scores = np.random.randint(50,101, size = (10,6))
print(f'The scores are:{scores}')

subject_avg = np.average(scores, axis=0) #Finding the average of the subjects
print(f'The subject averages are:{subject_avg}')

subject_avg_col = subject_avg.reshape(1,6) #Broadcasting to shape(1,6) for readability
normalized_student_scores = scores - subject_avg_col
print(f'The normalized student scores are{normalized_student_scores}')

deviations = np.abs(normalized_student_scores)
print(f'The deviations are{deviations}')

avg_deviation_per_student = np.mean(deviations, axis=1)
print(f'The average deviation per student is{avg_deviation_per_student}')
