days = np.array(['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
cities = np.array(['Techiman','Wa','Tamale','Ho','Kumasi'])                                        
temperature = np.random.randint(0,101, size = (7,5))
print(f'Temperatures: {temperature}')

#Converting celsius to fahrenheit
celsius_fahrenheit = (temperature*9/5) + 32
print(f'Temperatures converted from celsius to fahrenheit: {celsius_fahrenheit}')

#Finding daily extremes
hottest_city_index = np.argmax(celsius_fahrenheit, axis=1) #Finding the hottest city according to index
daily_hottest_temps = celsius_fahrenheit[np.arange(7), hottest_city_index]

for day_index in range(len(days)):
    print(f'The hottest city on {days[day_index]} is {cities[hottest_city_index[day_index]]} with a temperature of {daily_hottest_temps[day_index]}') 


coldest_city_index = np.argmin(celsius_fahrenheit, axis=1) #Finding the coldest city
daily_coldest_temps = celsius_fahrenheit[np.arange(7), coldest_city_index]

for day_index in range(len(days)):
    print(f'The coldest city on {days[day_index]} is {cities[coldest_city_index[day_index]]} with a temperature of {daily_coldest_temps[day_index]}') 

range = np.argmax(celsius_fahrenheit) - np.argmin(celsius_fahrenheit) #Range of the temperatures
print(f'The range is {range}') 

#Comparing each city to the daily hottest
hottest_temp_per_day = np.max(celsius_fahrenheit, axis=1)
hottest_temp_per_day_col = hottest_temp_per_day.reshape(7,1)
difference_from_hottest = hottest_temp_per_day_col - celsius_fahrenheit
print(f'The difference is {difference_from_hottest}')

#Weekly summaries
avg_temp_per_city = np.average(celsius_fahrenheit, axis=0)
print(f'The average temperature per city is {avg_temp_per_city}')

avg_temp_per_day = np.average(celsius_fahrenheit, axis=1)
print(f'The average temperature per day is {avg_temp_per_day}')
