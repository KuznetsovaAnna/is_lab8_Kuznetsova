from task7 import get_coordinates


cities = input('Enter a comma-separated list of cities: ').split(',')
southernmost_city = cities[0]

for city in cities:
    if get_coordinates(city)[1] < get_coordinates(southernmost_city)[1]:
        southernmost_city = city

print(f'The southernmost city: {southernmost_city}')
