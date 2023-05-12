import math
import requests
from task7 import get_coordinates

#Название точки вводить на английском, например: Kemerovo New-York

def get_distance(point1, point2):
    lon1, lat1 = point1
    lon2, lat2 = point2
    r = 6371  # radius of the earth in km
    d_lat = (lat2 - lat1) * (math.pi / 180)
    d_lon = (lon2 - lon1) * (math.pi / 180)
    a = (pow(math.sin(d_lat / 2), 2) + math.cos(lat1 * 3.14159265359 / 180) * math.cos(lat2 * 3.14159265359 / 180)
         * pow(math.sin(d_lon / 2), 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = r * c

    return d


cities = input('Enter a list of geographical names: ').split(' ')
coordinates = []
summary_length = 0

for city in cities:
    coordinates.append(get_coordinates(city))

print(coordinates)

midpoint = coordinates[len(coordinates) // 2]
print(midpoint)


for i in range(len(coordinates) - 1):
    summary_length += get_distance((float(coordinates[i][0]), float(coordinates[i][1])),
                                   (float(coordinates[i + 1][0]), float(coordinates[i + 1][1])))

print(f'{summary_length} km')

label = f"{midpoint[0]},{midpoint[1]}"

url = f"https://static-maps.yandex.ru/1.x/?l=map&pl={','.join([f'{p[0]},{p[1]}' for p in coordinates])}&pt={label}&w:2"
response = requests.get(url)

if response:
    with open('maps/task10/map.png', 'wb') as f:
        f.write(response.content)
else:
    print("Error:")
    print(url)
    print("HTTP Status:", response.status_code, "(", response.reason, ")")
