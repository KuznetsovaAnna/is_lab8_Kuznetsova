import requests
import geocode_key as gk

cities = ["Барнаул", "Мелеуз", "Йошкар-Ола"]

for city in cities:
    response = requests.get(f"http://geocode-maps.yandex.ru/1.x/?apikey={gk.key}&geocode={city}&format=json")
    data = response.json()
    address_components = data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["metaDataProperty"][
        "GeocoderMetaData"]["Address"]["Components"]

    for component in address_components:
        if "province" in component["kind"]:
            print(f"{city} belongs to {component['name']}")
            break
