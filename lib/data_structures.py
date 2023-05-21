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

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return[food for food in spicy_foods if food['heat_level'] > 5]
    

def print_spicy_foods(spicy_foods):
     for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        heat_level_symbols = "🌶" * heat_level

        print(f"{name} ({cuisine}) | Heat Level: {heat_level_symbols}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None

def print_spiciest_foods(spicy_foods):
     for food in spicy_foods:
        if food["heat_level"] > 5:
            name = food["name"]
            cuisine = food["cuisine"]
            heat_level = "🌶" * food["heat_level"]
            print(f"{name} ({cuisine}) | Heat Level: {heat_level}")
    

def get_average_heat_level(spicy_foods):
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    num_foods = len(spicy_foods)
    average = total_heat / num_foods
    return (average)
    

def create_spicy_food(spicy_foods, spicy_food):
    return spicy_foods + [spicy_food]
