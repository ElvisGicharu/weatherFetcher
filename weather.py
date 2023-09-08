import requests
API_KEY=''
API='https://api.openweathermap.org/data/2.5/weather'
city=input('Which City do you want?')
request_link=f'{API}?q={city}&appid={API_KEY}'

data=requests.get(request_link)

if data.status_code==200:
    data=data.json()
    weather=data['weather'][0]['description']
    # print(weather)
    
    # subtract 273.15 to turn it to degrees celsius
    temp=round(data['main']['temp']-273.15,2)
    
    print(f"The Weather is : {weather}")
    print(f"The temperature is {temp} \' Celsius")
    
else:
    print("Error occured")
    
