import requests
import geocode_key as gk

address = "Московский Уголовный Розыск, Петровка 38, Москва"
url = "https://geocode-maps.yandex.ru/1.x"
params = {
    "apikey": gk.key,
    "geocode": address,
    "format": "json"
}

response = requests.get(url, params=params)
data = response.json()
postal_code = data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["metaDataProperty"][
    "GeocoderMetaData"]["Address"]["postal_code"]

print(f"Postal index for the address '{address}': {postal_code}")
