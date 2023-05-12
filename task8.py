import requests
from task7 import get_coordinates

kemerovo = get_coordinates('Kemerovo')
leninsk_kuznetskiy = get_coordinates('Ленинск-Кузнецкий')
novokuznetsk = get_coordinates('Новокузнецк')
sheregesh = get_coordinates('Шерегеш')

url = f"https://static-maps.yandex.ru/1.x/?l=map&pt={kemerovo[0]},{kemerovo[1]}," \
      f"pm2dgl1~{leninsk_kuznetskiy[0]},{leninsk_kuznetskiy[1]}," \
      f"pm2dgl2~{novokuznetsk[0]},{novokuznetsk[1]},pm2dgl3~{sheregesh[0]},{sheregesh[1]}," \
      f"pm2dgl4&pl=c:FF000080,w:5,{kemerovo[0]},{kemerovo[1]}," \
      f"{leninsk_kuznetskiy[0]},{leninsk_kuznetskiy[1]}," \
      f"{novokuznetsk[0]},{novokuznetsk[1]},{sheregesh[0]},{sheregesh[1]}"

response = requests.get(url)

if response:
    with open('maps/task8/map.png', 'wb') as f:
        f.write(response.content)
else:
    print("Error:")
    print(url)
    print("HTTP Status:", response.status_code, "(", response.reason, ")")
