import requests
import geocode_key as gk


def get_coordinates(address):
    response = requests.get(f'https://geocode-maps.yandex.ru/1.x/?apikey={gk.key}&geocode={address}&format=json')
    response_json = response.json()
    pos = response_json['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
    coordinates = pos.split(' ')

    return coordinates


def task7():
    city = get_coordinates('Кемерово')
    railway_station = get_coordinates('Кемерово, Кузнецкий проспект, 79')
    dispensary = get_coordinates('Кемерово, Сосновый бульвар, 6')
    museum = get_coordinates('Кемерово, улица Красная Горка, 17')
    park = get_coordinates('Кемерово, Парк Жукова')

    url = f"https://static-maps.yandex.ru/1.x/?ll={city[0]},{city[1]}&pt={railway_station[0]},{railway_station[1]}," \
          f"pm2dgm1~{dispensary[0]},{dispensary[1]},pm2rdm2~{museum[0]},{museum[1]}," \
          f"pm2blm3~{park[0]},{park[1]},pm2orm4&z=11&l=map"

    response = requests.get(url)

    if response:
        with open('maps/task7/map.png', 'wb') as f:
            f.write(response.content)
    else:
        print("Error:")
        print(url)
        print("HTTP Status:", response.status_code, "(", response.reason, ")")


task7()
