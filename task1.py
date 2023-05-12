import requests


def request_map(filename, url):
    response = requests.get(url)

    if not response:
        print("Error:")
        print("HTTP status:", response.status_code, "(", response.reason, ")")
        return 0

    with open(f'maps/{filename}.png', 'wb') as file:
        file.write(response.content)

    return 1


def task1():
    a = request_map("task1/map1a", "https://static-maps.yandex.ru/1.x/?ll=86.093496,55.351368"
                                   "&spn=0.0015,0.0015&pt=86.093496,55.351368,org&l=map")
    print(a)

    b = request_map("task1/map1b", "https://static-maps.yandex.ru/1.x/?ll=86.030379,55.337171&z=12&l=map")
    print(b)

    c = request_map("task1/map1c", "https://static-maps.yandex.ru/1.x/?ll=86.086088,55.397158&z=10&l=map")
    print(c)

    d = request_map("task1/map1d", "https://static-maps.yandex.ru/1.x/?ll=2.295068,48.857954&z=17&l=sat")
    print(d)

    e = request_map("task1/map1e", "https://static-maps.yandex.ru/1.x/?ll=158.852478,53.254810"
                                   "&pt=158.852478,53.254810&z=10&l=sat")
    print(e)

    f = request_map("task1/map1f", "https://static-maps.yandex.ru/1.x/?ll=108.749065,53.454226&z=6&l=sat")
    print(f)

    g = request_map("task1/map1g", "https://static-maps.yandex.ru/1.x/?ll=63.292713,45.918652&z=13&l=sat")
    print(g)

task1()