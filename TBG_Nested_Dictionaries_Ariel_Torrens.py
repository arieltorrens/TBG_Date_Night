# RPG Nested Dictionaries - Ariel Torrens
# May 4, 2022

# This code prints three dictionaries about
# characters, food, and locations and their
# descriptions which uses loops to print the
# statements.

characters = {                                                                # Creates nested dictionary for characters and traits
    "Joe":                                                                    # Creates data set for Joe's traits
    { "age": "27", "height": "5'11",
    "likes": "Wine", "dislikes": "cheese"},
    "Y/N":                                                                    # Creates data set for Y/N's traits
    { "age": "24", "height": "5'5",
    "likes": "surfing at the beach", "dislikes": "seafood"},
    "Waiter":                                                                 # Creates data set for the waiter's traits
    { "age": "39", "height": "6'1",
    "likes": "flirting", "dislikes": "dumb customers"},
    }

for name, char_info in characters.items():                                    # Creates loop for printing characters, traits and descriptions
    age = char_info["age"]                                                    # Creates variable for age item
    height = char_info["height"]                                              # Creates variable for height item
    likes = char_info["likes"]                                                # Creates variable for likes item
    dislikes = char_info["dislikes"]                                          # Creates variable for dislikes item
    print(f'\n{name}:')                                         
    print(f'{name} is {age} years old')
    print(f'{name} is {height}')
    print(f'{name} likes {likes}')
    print(f'{name} dislikes {dislikes}')

food = {                                                                      # Creates dictionary for food and descriptions
    "Spaghetti and  meatballs":                                               # Creates data set
    { "desc": "House made pasta with tomato sauce and pork meatballs"},        
    "Lobster":                                                                # Creates data set 
    { "desc": "A roasted rock lobster tail with butter"},
    "Shrimp linguine":                                                        # Creates data set
    { "desc": "Creamy linguine with juicy shrimp topped with lemon juice"},
    }

print("\nFood menu:")                                                         # Prints food menu title
for food, food_info in food.items():                                          # Creates loop for printingg food and their descriptions
    desc = food_info["desc"]                                                  # Creates variable for food desc
    print(f'{food} is {desc}')                                                # Prints a sentence with food name and description                    

locations = {                                                                 # Creates dictionary for locations and descriptions
    "Table":                                                                  # Creates data set
    { "desc": "The table for two you're sitting at across from Joe"},
    "Bathroom":                                                               # Creates data set
    { "desc": "The ladies washroom"},           
    "Home":                                                                   # Creates data set
    { "desc": "Your home, not far from the restaurant"},
    }

print("\nLocations:")                                                         # Prints locations title
for locations, locat_info in locations.items():                               # Creats loop for printing locations and descriptions
    desc = locat_info["desc"]                                                 # Creates variable for location description
    print(f'{locations}: {desc}')                                             # Prints location followed by description

