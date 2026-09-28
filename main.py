#Part A
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

# Part B
def list_all_ingredients(ingredients):
    print("Ingredients:")
    for item in ingredients:
        print(f"- {item}")

burger_ingredients = [
    "Ground Beef",
    "Salt",
    "Pepper",
    "Bun",
    "Cheese",
    "Lettuce",
    "Tomato",
    "Onion",
    "Ketchup",
    "Mayonnaise",
    "Smoked Paprika",
    "Garlic Powder"
    "Frozen French Fries"
]

list_all_ingredients(burger_ingredients)

#Part C
def make_loaded_fries(meat, cheese, topping, sauce):
    return (
        "Loaded Fries!\n"
        "Layer 1: French Fries\n"
        f"Layer 2: {meat}\n"
        f"Layer 3: {cheese}\n"
        f"Layer 4: {topping} with {sauce}"
    )

dish = make_loaded_fries("Seasoned Ground Beef", "Melted Cheddar Cheese", "Diced Tomato and Onions", "Special Sauce")

print(dish)

# Part D
def add_spice(dish, spice="paprika"):
    print(f"Adding a dash of {spice} to the {dish}. Hits the spot!")


add_spice("Loaded Fries")

#Part E
def welcome_message():
    print("Welcome to the kitchen! Today we're making burgers.")

def heat_grill():
    print("Heating the grill to medium-high... ready!")

def list_ingredients(*items):
    print("Ingredients:", ", ".join(items))

def make_dish(patty, bun):
    return f"{patty} on a {bun}"

def add_toppings(dish, *toppings):
    print(f"Adding {', '.join(toppings)} to your {dish}.")



def cook_recipe():
    welcome_message()
    heat_grill()
    list_ingredients("Beef Patty", "Brioche Bun", "Lettuce", "Tomato", "Cheese")
    dish = make_dish("Beef Patty with cheese", "Brioche Bun")
    print("Dish created:", dish)
    add_toppings(dish, "Lettuce", "Tomato", "Special Sauce")
    print("Burger is ready to eat!")


cook_recipe()
