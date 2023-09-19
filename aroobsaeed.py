# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
rivers = [{"name": "Nile", "length": 4157},
          {"name": "Yangtze", "length": 3434},
          {"name": "Murray-Darling", "length": 2310},
          {"name": "Volga", "length": 2290},
          {"name": "Mississippi", "length": 2540},
          {"name": "Amazon", "length": 3915}]

#Task 1
for name in rivers: print(name["name"])


total = 0
for length in rivers:
    total += length["length"]
print("total length :",total)


for name in rivers:
    if name["name"].startswith("M"):
        print(name)
for i in range(len(rivers)):
    print(rivers[i]["name"])
    print("Length in kilometers of", rivers[i]["name"], rivers[i]["length"]*1.6)

#Task 2:
def overlap(u, v):
    return [x for x in u if x in v]

print(overlap([1.0, 2.0, 4.5], [2.0, 4.5, 5.0]))
def join(u, v):
    bucket = [x for x in u]
    bucket += [x for x in v if x not in u]
    return bucket

print(join([1.0, 2.0, 4.5], [2.0, 4.5, 5.0]))

def get_names(spicy_foods):
    names = []
    for food in spicy_foods:
        names.append(food["name"])
    return names

spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

print(get_names(spicy_foods))


def get_spiciest_foods(spicy_foods):
    spiciest_foods = []
    for food in spicy_foods:
        if food["heat_level"] > 5:
            spiciest_foods.append(food)
    return spiciest_foods
print(get_spiciest_foods(spicy_foods))

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level_emojis = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}.")
print(print_spicy_foods(spicy_foods))       
        
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"].lower() == cuisine.lower():
            return food
    return None



def print_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food["heat_level"] > 5]
    print_spicy_foods(spiciest_foods)
print(print_spiciest_foods(spicy_foods))

def average_heat_level(spicy_foods):
    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    average = total_heat_level // len(spicy_foods)
    return average
print(average_heat_level(spicy_foods))