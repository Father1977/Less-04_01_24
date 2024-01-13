import json
import random

some_name = ['Alex', 'Max', 'Nikit']
some_city = ['Minsk', 'Gomel', 'Vitebsk']

list_obj = [{
    "name": random.choice(some_name),
    "city": random.choice(some_city),
    "age": random.randint(20, 50)
} for _ in range(5)]

with open("file.json", "w") as file:
    json.dump(list_obj, file)


with open("file.json", "r") as file:
    data = json.load(file)

print(data)

for item in data:
    print(item)
