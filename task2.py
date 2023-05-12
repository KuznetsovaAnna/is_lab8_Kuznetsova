import requests
import geocode_key as gk


def get_json_data(url):
    response = requests.get(url)
    if response:
        json_response = response.json()
        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        toponym_region = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"][1]['name']
        toponym_country = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"][-1]['name']
        toponym_address = f'{toponym_country}, {toponym_region}'
        toponym_coordinates = toponym["Point"]["pos"]

    else:
        print("Error:")
        print(url)
        print("HTTP Status:", response.status_code, "(", response.reason, ")")
        return [0]

    return [toponym, toponym_address, toponym_coordinates]


a1 = get_json_data(f"http://geocode-maps.yandex.ru/1.x/?apikey={gk.key}&geocode=Якутск&format=json")
print(f"{a1[1]} имеет координаты: {a1[2]}")

a2 = get_json_data(f"http://geocode-maps.yandex.ru/1.x/?apikey={gk.key}&geocode=Магадан&format=json")
print(f"{a2[1]} имеет координаты: {a2[2]}\n")

b1 = get_json_data(f"http://geocode-maps.yandex.ru/1.x/?apikey={gk.key}&geocode=Торонто&format=json")
print(f"{b1[1]} имеет координаты: {b1[2]}")

b2 = get_json_data(f"http://geocode-maps.yandex.ru/1.x/?apikey={gk.key}&geocode=Кемерово&format=json")
print(f"{b2[1]} имеет координаты: {b2[2]}\n")

c1 = get_json_data(f"http://geocode-maps.yandex.ru/1.x/?apikey={gk.key}&geocode=Хабаровск&format=json")
print(f"{c1[1]} имеет координаты: {c1[2]}")

c2 = get_json_data(f"http://geocode-maps.yandex.ru/1.x/?apikey={gk.key}&geocode=Уфа&format=json")
print(f"{c2[1]} имеет координаты: {c2[2]}")

c3 = get_json_data(f"http://geocode-maps.yandex.ru/1.x/?apikey={gk.key}&geocode=Нижний Новгород&format=json")
print(f"{c3[1]} имеет координаты: {c3[2]}")

c4 = get_json_data(f"http://geocode-maps.yandex.ru/1.x/?apikey={gk.key}&geocode=Калининград&format=json")
print(f"{c4[1]} имеет координаты: {c4[2]}")

c5 = get_json_data(f"http://geocode-maps.yandex.ru/1.x/?apikey={gk.key}&geocode=Кемерово&format=json")
print(f"{c5[1]} имеет координаты: {c5[2]}\n")

d1 = get_json_data(f"http://geocode-maps.yandex.ru/1.x/?apikey={gk.key}&"
                   f"geocode=Кемерово+Кемерово, Красная, 6&format=json&district")
print(f"Индекс КемГУ: {d1[0]['metaDataProperty']['GeocoderMetaData']['Address']['postal_code']}")
