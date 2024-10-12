import random

menus = {
    'Pad Thai': ['Rice Noodles', 'Egg', 'Shrimp', 'Tofu', 'Peanuts', 'Garlic'],
    'Green Curry': ['Coconut Milk', 'Green Curry Paste', 'Chicken', 'Bamboo Shoots', 'Basil'],
    'Fried Rice': ['Rice', 'Egg', 'Pork', 'Garlic', 'Carrot', 'Peas'],
    'Tom Yum Soup': ['Shrimp', 'Mushrooms', 'Lemongrass', 'Lime', 'Chili Paste'],
    'Som Tum': ['Papaya', 'Tomatoes', 'Peanuts', 'Garlic', 'Lime', 'Fish Sauce']
}

all_ingredients_data = {
    'Rice Noodles': {'price': 30, 'quantity': 1000},
    'Egg': {'quantity': 30},
    'Shrimp': {'quantity': 40},
    'Tofu': {'quantity': 300},
    'Peanuts': {'quantity': 50},
    'Garlic': {'quantity': 60},
    'Coconut Milk': {'quantity': 700},
    'Green Curry Paste': {'quantity': 200},
    'Chicken': {'quantity': 5000},
    'Bamboo Shoots': {'quantity': 300},
    'Basil': {'quantity': 60},
    'Rice': {'quantity': 7000},
    'Pork': {'quantity': 5000},
    'Carrot': {'quantity': 4},
    'Peas': {'quantity': 100},
    'Mushrooms': {'quantity': 200},
    'Lemongrass': {'quantity': 100},
    'Lime': {'quantity': 10},
    'Chili Paste': {'quantity': 200},
    'Papaya': {'quantity': 3},
    'Tomatoes': {'quantity': 6},
    'Fish Sauce': {'quantity': 200}
}

food_ingredients_data = {
    'PadThai_data': {
        'Rice Noodles': {'quantity': 200},
        'Egg': {'quantity': 2},
        'Shrimp': {'quantity': 5},
        'Tofu': {'quantity': 20},
        'Peanuts': {'quantity': 5},
        'Garlic': {'quantity': 3}
    },
    'GreenCurry_data': {
        'Coconut Milk': {'quantity': 400},
        'Green Curry Paste': {'quantity': 100},
        'Chicken': {'quantity': 5},
        'Bamboo Shoots': {'quantity': 100},
        'Basil': {'quantity': 30}
    },
    'FriedRice_data': {
        'Rice': {'quantity': 300},
        'Egg': {'quantity': 2},
        'Pork': {'quantity': 5},
        'Garlic': {'quantity': 3},
        'Carrot': {'quantity': 1},
        'Peas': {'quantity': 100}
    },
    'TomYumSoup_data': {
        'Shrimp': {'quantity': 5},
        'Mushrooms': {'quantity': 100},
        'Lemongrass': {'quantity': 2},
        'Lime': {'quantity': 1},
        'Chili Paste': {'quantity': 100}
    },
    'SomTum_data': {
        'Papaya': {'quantity': 1},
        'Tomatoes': {'quantity': 2},
        'Peanuts': {'quantity': 5},
        'Garlic': {'quantity': 3},
        'Lime': {'quantity': 1},
        'Fish Sauce': {'quantity': 200}
    }
}

orders_monday = ['PadThai_data', 'FriedRice_data',
                 'PadThai_data', 'TomYumSoup_data',
                 'SomTum_data', 'FriedRice_data',
                 'PadThai_data', 'FriedRice_data',
                 'PadThai_data', 'TomYumSoup_data',
                 'SomTum_data', 'FriedRice_data']

def calculate_ingredients(order_list):
    total_ingredients = {}
    for menu in order_list:
        if menu in food_ingredients_data:
            ingredients = food_ingredients_data[menu]
            for ingredient, details in ingredients.items():
                quantity = details['quantity']
                if ingredient in total_ingredients:
                    total_ingredients[ingredient]['quantity'] += quantity
                else:
                    total_ingredients[ingredient] = {'quantity': quantity}
    return total_ingredients

def check_inventory(total_ingredients, all_ingredients_data):
    purchase_list = {}
    for ingredient, details in total_ingredients.items():
        required_quantity = details['quantity']
        available_quantity = all_ingredients_data.get(ingredient, {}).get('quantity', 0)
        
        if available_quantity < required_quantity:
            purchase_list[ingredient] = required_quantity - available_quantity
    return purchase_list


total = calculate_ingredients(orders_monday)

purchase_list = check_inventory(total, all_ingredients_data)

print("Total Ingredients Needed:")
for ingredient, details in total.items():
    print(f" - {ingredient}: Quantity = {details['quantity']}")

print("\nIngredients to Purchase:")
if purchase_list:
    for ingredient, quantity_needed in purchase_list.items():
        print(f" - {ingredient}: Quantity needed = {quantity_needed}")
else:
    print("No additional ingredients needed.")