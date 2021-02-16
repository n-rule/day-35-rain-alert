import requests

API_KEY = '9fb60369241b9d962759b2e7c4db10bc'
ONE_CALL_API = 'https://api.openweathermap.org/data/2.5/onecall?'
LAT = 50.447731
LON = 30.542721
params = {
    'lat': LAT,
    'lon': LON,
    'appid': API_KEY,
    'exclude': 'current,minutely,daily'
}

pull = requests.get(ONE_CALL_API, params)
pull.raise_for_status()
data = pull.json()

for hour in range(12):
    if data['hourly'][hour]['weather'][0]['id'] > 700:
        will_rain = True

# SLICING METHOD

weather_slice = data['hourly'][:12]['weather'][0]['id']


if will_rain:
    print('Bring an umbrella')


# lat={lat}&lon={lon}&exclude={part}&appid={API key}