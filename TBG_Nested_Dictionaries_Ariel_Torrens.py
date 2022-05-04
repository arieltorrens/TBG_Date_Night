# RPG Nested Dictionaries - Ariel Torrens
# May 4, 2022

# This code

characters = {
    "Joe":
    { "age": "27", "height": "5'11",
    "likes": "Wine", "dislikes": "cheese"},
    "Y/N":
    { "age": "24", "height": "5'5",
    "likes": "surfing at the beach", "dislikes": "seafood"},
    "Waiter":
    { "age": "39", "height": "6'1",
    "likes": "flirting", "dislikes": "dumb customers"},
    }

for name, char_info in characters.items():
    age = char_info["age"]
    height = char_info["height"]
    likes = char_info["likes"]
    dislikes = char_info["dislikes"]
    print(f'\n{name}:')
    print(f'{name} is {age} years old')
    print(f'{name} is {height}')
    print(f'{name} likes {likes}')
    print(f'{name} dislikes {dislikes}')

food = {
    "Spaghetti and  meatballs":
    { "desc": "House made pasta with tomato sauce and pork meatballs"},
    "Lobster":
    { "desc": "A roasted rock lobster tail with butter"},
    "Shrimp linguine":
    { "desc": "Creamy linguine with juicy shrimp topped with lemon juice"},
    }

print("\nFood menu:")
for food, food_info in food.items():
    desc = food_info["desc"]
    print(f'{food} is {desc}')

locations = {
    "Table":
    { "desc": "The table for two you're sitting at across from Joe"},
    "Bathroom":
    { "desc": "The ladies washroom"},
    "Home":
    { "desc": "Your home, not far from the restaurant"},
    }

print("\nLocations:")
for locations, locat_info in locations.items():
    desc = locat_info["desc"]
    print(f'{locations}: {desc}')


