import random

# เมนูอาหารและวัตถุดิบที่ใช้
menus = {
    'Pad Thai': ['Rice Noodles', 'Egg', 'Shrimp', 'Tofu', 'Peanuts', 'Garlic'],
    'Green Curry': ['Coconut Milk', 'Green Curry Paste', 'Chicken', 'Bamboo Shoots', 'Basil'],
    'Fried Rice': ['Rice', 'Egg', 'Pork', 'Garlic', 'Carrot', 'Peas'],
    'Tom Yum Soup': ['Shrimp', 'Mushrooms', 'Lemongrass', 'Lime', 'Chili Paste'],
    'Som Tum': ['Papaya', 'Tomatoes', 'Peanuts', 'Garlic', 'Lime', 'Fish Sauce']
}

# ข้อมูลวัตถุดิบ
all_ingredients_data = {
    'Rice Noodles': {'quantity': 1000},
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

# ข้อมูลวัตถุดิบสำหรับเมนู
food_ingredients_data = {
    'Pad Thai': {
        'Rice Noodles': {'quantity': 200},
        'Egg': {'quantity': 2},
        'Shrimp': {'quantity': 5},
        'Tofu': {'quantity': 20},
        'Peanuts': {'quantity': 5},
        'Garlic': {'quantity': 3}
    },
    'Green Curry': {
        'Coconut Milk': {'quantity': 400},
        'Green Curry Paste': {'quantity': 100},
        'Chicken': {'quantity': 5},
        'Bamboo Shoots': {'quantity': 100},
        'Basil': {'quantity': 30}
    },
    'Fried Rice': {
        'Rice': {'quantity': 300},
        'Egg': {'quantity': 2},
        'Pork': {'quantity': 5},
        'Garlic': {'quantity': 3},
        'Carrot': {'quantity': 1},
        'Peas': {'quantity': 100}
    },
    'Tom Yum Soup': {
        'Shrimp': {'quantity': 5},
        'Mushrooms': {'quantity': 100},
        'Lemongrass': {'quantity': 2},
        'Lime': {'quantity': 1},
        'Chili Paste': {'quantity': 100}
    },
    'Som Tum': {
        'Papaya': {'quantity': 1},
        'Tomatoes': {'quantity': 2},
        'Peanuts': {'quantity': 5},
        'Garlic': {'quantity': 3},
        'Lime': {'quantity': 1},
        'Fish Sauce': {'quantity': 200}
    }
}

# ฟังก์ชันสุ่มออร์เดอร์สำหรับ 7 วัน
def generate_weekly_orders():
    return {day: random.choices(list(menus.keys()), k=random.randint(1, 3)) for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']}

# ฟังก์ชันคำนวณวัตถุดิบ
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

# ฟังก์ชันเช็คสต็อกวัตถุดิบ
def check_inventory(total_ingredients, all_ingredients_data):
    purchase_list = {}
    for ingredient, details in total_ingredients.items():
        required_quantity = details['quantity']
        available_quantity = all_ingredients_data.get(ingredient, {}).get('quantity', 0)
        
        if available_quantity < required_quantity:
            purchase_list[ingredient] = required_quantity - available_quantity
    return purchase_list

# ฟังก์ชันจัดอันดับความสำคัญของวัตถุดิบตามการใช้งาน (Ranking)
def rank_ingredients(orders_week):
    ingredient_usage = {}
    
    # นับจำนวนครั้งที่แต่ละวัตถุดิบถูกใช้งาน
    for day, orders in orders_week.items():
        total_ingredients = calculate_ingredients(orders)
        for ingredient, details in total_ingredients.items():
            quantity = details['quantity']
            if ingredient in ingredient_usage:
                ingredient_usage[ingredient] += quantity
            else:
                ingredient_usage[ingredient] = quantity
    
    # จัดอันดับตามจำนวนการใช้งาน (มากไปน้อย)
    ranked_ingredients = sorted(ingredient_usage.items(), key=lambda x: x[1], reverse=True)
    
    return ranked_ingredients

# ฟังก์ชันพยากรณ์ปริมาณที่ต้องซื้อ
def forecast_purchase(ranked_ingredients, purchase_list):
    forecast = {}
    
    # ประมาณการปริมาณที่ต้องซื้อจากรายการวัตถุดิบที่ต้องซื้อ
    for ingredient, _ in ranked_ingredients:
        needed_quantity = purchase_list.get(ingredient, 0)
        # พิจารณาจากการใช้งานในสัปดาห์ที่แล้ว
        if needed_quantity > 0:
            forecast[ingredient] = needed_quantity
        else:
            forecast[ingredient] = 0  # ถ้าไม่ต้องซื้อก็ใส่เป็น 0

    return forecast

# สุ่มออร์เดอร์สำหรับ 7 วัน
orders_week = generate_weekly_orders()

# แสดงออร์เดอร์ที่สุ่มได้
print("Weekly Orders:")
for day, orders in orders_week.items():
    print(f"{day}: {orders}")

# คำนวณวัตถุดิบจากออร์เดอร์ทั้งสัปดาห์
total = {}
for day, orders in orders_week.items():
    daily_total = calculate_ingredients(orders)
    for ingredient, details in daily_total.items():
        if ingredient in total:
            total[ingredient]['quantity'] += details['quantity']
        else:
            total[ingredient] = details

# เช็คสต็อกวัตถุดิบ
purchase_list = check_inventory(total, all_ingredients_data)

# แสดงข้อมูลวัตถุดิบที่ต้องการ
print("\nTotal Ingredients Needed:")
for ingredient, details in total.items():
    print(f" - {ingredient}: Quantity = {details['quantity']}")

print("\nIngredients to Purchase:")
if purchase_list:
    for ingredient, quantity_needed in purchase_list.items():
        print(f" - {ingredient}: Quantity needed = {quantity_needed}")
else:
    print("No additional ingredients needed.")

# แสดงลำดับความสำคัญของวัตถุดิบ
ranked_ingredients = rank_ingredients(orders_week)
print("\nRanked Ingredients by Usage:")
for rank, (ingredient, usage) in enumerate(ranked_ingredients, 1):
    print(f"{rank}. {ingredient}: used {usage} times")

# พยากรณ์ปริมาณที่ต้องซื้อ
forecast = forecast_purchase(ranked_ingredients, purchase_list)
print("\nForecast Purchase Quantities:")
for ingredient, quantity in forecast.items():
    print(f" - {ingredient}: Quantity to purchase = {quantity}")
