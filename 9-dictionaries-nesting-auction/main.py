programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
    }

print(programming_dictionary["Bug"])
print(programming_dictionary)
#Creeating an empty dictionary
empty_dictionary = {}

#Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

#Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

#Nesting

# Nesting a List in a Dictionary
# Path: 9-dictionaries-nesting-auction\main.py
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a Dictionary in a Dictionary
# Path: 9-dictionaries-nesting-auction\main.py
travel_log = {
    "France": {"cities_visited":  ["Paris", "Lille", "Dijon"], "total_visits": 12},  
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

# Nesting Dictionaries in Lists
# Path: 9-dictionaries-nesting-auction\main.py
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
]

def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["total_visits"] = times_visited
    new_country["cities_visited"] = cities_visited
    travel_log.append(new_country)
    
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
