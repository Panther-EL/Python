import numpy as np
                                #Weather Data Analysis
#Array creation
temperature = np.random.randint(21,40, size=(5,7))
print(f'Temperature:{temperature}')

#Finding average temperature for each city and day
avg_city = np.mean(temperature, axis=1) #Average temperature for each city
print(f'The average temperature for each city is: {avg_city}')

avg_day = np.mean(temperature, axis=0)
print(f'The average temperature for each day is {avg_day}') #Average temperature for each day

#Finding the hottest day of the week
hottest_day = np.argmax(avg_day)
print(f'The hottest day of the week was(according to index): {hottest_day}')

#Finding the coldest city
coldest_city = np.argmin(avg_city)
print(f'The coldest city was(according to index): {coldest_city}')

#Finding the global maximun and minimum temperatures
maximum_temperature = np.max(temperature)
print(f'The hottest temperature recorded was:{maximum_temperature}')

minimum_temperature = np.min(temperature)
print(f'The coldest temperature recorded was :{minimum_temperature}')
