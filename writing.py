cities = ["Adelaide", "Alice Springs", "Darwin", "Melbourne", "Sydney"]

with open("cities", 'w') as city_file:
    for city in cities:
        print(city, file=city_file)

cities = []

with open("cities", 'r') as city_file:
    cities = city_file.readlines()
    for city in cities:
        print(city )

    # for word in lines:
    #     print(word)