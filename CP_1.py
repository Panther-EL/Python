import requests
def get_weather():
    api_key = '263270d0a0bb988c751401d4687f6eb4'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'

    #API request
    city = print(input('Enter city name: '))
    link= f'{base_url}?q={city}&appid={api_key}&units=metric'

    feedback = requests.get(link) #Make a request
    data = feedback.json()

    #Extracting details
    if str(data.get('cod')) == '200':
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        description = data['weather'][0]['description']

        print(f'Temperature:{temperature}')
        print(f'Humidity:{humidity}')
        print(f'Description:{description}')
        print(f'Pressure:{pressure}')
    else:
        print('The city you entered is an invalid city. Try again')

get_weather() #Calling the function to get input



