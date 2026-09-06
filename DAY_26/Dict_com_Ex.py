# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# words = sentence.split()

# word_len = {word:len(word) for word in words}
# print(word_len)

weather_r = {
    "Monday" : 12,
    "Tuesday" : 14,
    "Wednesday" : 15,
    "Thursday" : 14,
    "Friday" : 21,
    "Saturday" : 22,
    "Sunday" : 24,
}

Fahren = {day : (temp_c*9/5)+32 for (day , temp_c) in weather_r.items() }
print(Fahren)