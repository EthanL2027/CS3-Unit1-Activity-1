# ACTIVITY #1: Cooking with Functions

# PART A:

def welcome_message():
    print("Welcome to Ethan's virtual kitchen, today we will learn how to make a delicious burger!")

def cook_burger():
    print("Shape ground beef into a patty and season with salt, pepper, garlic powder, and smoked paprika.")
    print("Heat a pan or grill over medium-high heat.")
    print("Cook the patty for 3-4 minutes per side and add cheese when you flip.")
    print("Mix together ketchup and mayonnaise and the seasonings listed to make a special sauce.")
    print("Place the sauce on the bottom bun, and on top add lettuce, and tomato.")

welcome_message()
cook_burger()

# PART B: 
def list_ingredients(main_ingredient, side_dish):
    print(f"Main Ingredient: {main_ingredient}")
    print(f"Side Dish: {side_dish}")

list_ingredients("Beef Patty", "French Fries")
list_ingredients("Beef Patty", "Onion Rings")

# Extra: prints every ingredient in a list
def list_all_ingredients():
    print("Ingredients:")
    print("Ground Beef")
    print("Salt")
    print("Pepper")
    print("Bun")
    print("American Cheese")
    print("Lettuce")
    print("Tomato")
    print("Onion")
    print("Ketchup")
    print("Mayonnaise")
    print("Smoked Paprika")
    print("Garlic Powder")


list_all_ingredients()

# PART C
def make_dish(ingredient1, ingredient2):
    return f"{ingredient1} and {ingredient2}!"

dish = make_dish("Beef Patty", "French Fries")
print(dish)

def make_loaded_fries(meat, cheese, topping, sauce):
    return (
        "Loaded Fries!\n"
        "Layer 1: French Fries\n"
        f"Layer 2: {meat}\n"
        f"Layer 3: {cheese}\n"
        f"Layer 4: {topping} with {sauce}"
    )

loaded_fries = make_loaded_fries("Seasoned Ground Beef", "Melted American Cheese", "Diced Tomato and Onions", "Special Sauce")
print(loaded_fries)

# PART D: 
def add_spice(dish, spice="paprika"):
    print(f"Adding a dash of {spice} to the {dish}. Hits the spot!")

add_spice("Loaded Fries !", "cayenne pepper")
add_spice("Loaded Fries")

# PART E: 
def cook_recipe():
    welcome_message()
    list_all_ingredients()
    cook_burger()
    fries = make_loaded_fries("Seasoned Ground Beef", "Melted American Cheese", "Diced Tomato and Onions", "Special Sauce")
    print(fries)
    add_spice("Loaded Fries")
    burger = make_dish("American Cheeseburger", "Loaded Fries")
    print("Dish created:", burger)
    print("Burger is ready to eat!")

cook_recipe()