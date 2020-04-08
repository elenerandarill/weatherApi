#!usr/bin/python
import requests


api_key = '371d82fc6de5c042c8dc8103b0b68caf'
# ex1 = 'api.openweathermap.org/data/2.5/weather?q=London'
# ex_api_q = 'api.openweathermap.org/data/2.5/weather?q={city name}&appid={your api key}'

api_base_url = 'http://api.openweathermap.org/data/2.5/weather'
city_name = input('give a name of the city you want to fee weather for: ')
# city_name = 'Warsaw'
city = f"?q={city_name}"
end_url = f"{api_base_url}{city}&appid={api_key}"
print(end_url)

r = requests.get(end_url)
resp = r.json()
# resp = {"coord":{"lon":21.01,"lat":52.23},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"base":"stations","main":{"temp":292.47,"feels_like":289.39,"temp_min":290.93,"temp_max":293.71,"pressure":1026,"humidity":22},"visibility":10000,"wind":{"speed":1},"clouds":{"all":0},"dt":1586360671,"sys":{"type":1,"id":1713,"country":"PL","sunrise":1586318016,"sunset":1586366485},"timezone":7200,"id":756135,"name":"Warsaw","cod":200}
# print(f"status code: {resp.status_code}")
# print(type(resp))
# print(resp.text)

print(f"Forecast for {city_name}. ")
weath_sky = resp["weather"][0]["description"]
print(f"The sky is: {weath_sky}.")
weath_temp = resp["main"]["temp"]
weath_temp_c = (weath_temp - 273.15)
print(f"Temperature is: {weath_temp} F, {weath_temp_c:.2f} C.")
pressure = resp["main"]["pressure"]
print(f"The pressure is: {pressure}.")

print("Have a nice day!")