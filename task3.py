import requests
import geocode_key as gk


url = f"http://geocode-maps.yandex.ru/1.x/?apikey={gk.key}&geocode=Москва, Красная площадь, 1&format=json"

response = requests.get(url)

if response:
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    coordinates = toponym["Point"]["pos"]
    full_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]

    print("Full address:", full_address)
    print("Coordinates:", coordinates)
else:
    print("Error:")
    print(url)
    print("HTTP Status:", response.status_code, "(", response.reason, ")")
