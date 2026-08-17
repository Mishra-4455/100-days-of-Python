travel_log = [
    {
     "Country" : "India",
     "States" : ["West Bengal", "Andra Pradesh", "Karnataka"],
     "Times visited" : 13, 
    },
    {
     "Country" : "Japan",
     "Prefectures" : ["Tokyo", "Kyoto", "Miyagi"],
     "Times visited" : 15,
    },
]

def add_new_country(Count, places, visit):
    new_country = {}
    new_country["country"] = Count
    new_country["States"] = places
    new_country["Times visited"] = visit
    travel_log.append(new_country)

add_new_country("France", 8, ["Paris", "Lille", "Dijon"])
print(travel_log)