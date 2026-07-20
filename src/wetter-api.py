# Aufgabe 1.1

import requests

latitude = 52.5244
longitude = 13.4105

location_name = "Berlin"

print(
    "Der Wohnort ist "
    + location_name
    + " mit den Koordinaten: "
    + ", "
    + str(longitude)
    + ", "
    + str(latitude)
)

forecast_params = {
    "latitude": latitude,
    "longitude": longitude,
    "hourly": "temperature_2m",
}

forecast_url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m"

response = requests.get(forecast_url, forecast_params)
# Reihenfolge wichtig, wenn unklar muss benannt werden : "param=", "url="

# print(response)
# print("response code", response.status_code)
# print("response json", response.json())
## Warum gibt er die ganzen time stamps aus?

# Aufgabe 1.2

forecast_5t_url = "https://api.open-meteo.com/v1/forecast"

start_date = "2026-07-15"
end_date = "2026-07-21"

forecast_5t_params = {
    "latitude": latitude,
    "longitude": longitude,
    "hourly": "temperature_2m",
    "start_date": start_date,
    "end_date": end_date,
}

response_5t = requests.get(forecast_5t_url, forecast_5t_params)

data = response.json()

print("response code", response_5t.status_code)
print("response json", response_5t.json())

print("Das Wetter in " + location_name + " ist: vom " + start_date + " bis " + end_date)

# Warum gibt es bis 22.7. aus? -> Fehler liegt bei Seite

# Aufgabe 1.3

historical_url = "https://archive-api.open-meteo.com/v1/archive"

historical_params = {
    "latitude": latitude,
    "longitude": longitude,
    "start_date": "2019-03-08",
    "end_date": "2019-03-08",
    "hourly": "temperature_2m",
}

response_190308 = requests.get(historical_url, historical_params)

data_190308 = response_190308.json()

print("reponse code", response_190308.status_code)

print(
    "Das Wetter in "
    + location_name
    + " am 08. März 2019: "
    + str(data_190308["hourly"]["temperature_2m"])
)
