travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country , num_visits, cities_name):
  country = input("What is the name of the country? \n")
  num_visits = int(input("How many times did you visit? \n"))
  cities_name = input("Name the cities you visited (separated by a comma): \n")

  travel_log.append({"country": country, "visits": num_visits, "cities": cities_name })



#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)