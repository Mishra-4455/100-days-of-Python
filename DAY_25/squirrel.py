import pandas

squirrels = pandas.read_csv("NYC_squirrel_data.csv")
# data = squirrels["Primary Fur Color"].to_list()
# black_c = 0
# cinnamon_c = 0
# grey_c = 0

# for i in data:
#     if i == "Gray":
#         grey_c += 1
#     elif i == "Cinnamon":
#         cinnamon_c += 1
#     else:
#         black_c += 1

black_c = len(squirrels[squirrels["Primary Fur Color"] == "Black"])
cinnamon_c = len(squirrels[squirrels["Primary Fur Color"] == "Cinnamon"])
grey_c = len(squirrels[squirrels["Primary Fur Color"] == "Grey"])

final_set = {
    "Fur Color" : ["grey", "cinnamon", "black"],
    "Count" : [grey_c, cinnamon_c, black_c]
}

squirrel = pandas.DataFrame(final_set)
squirrel .to_csv("squirrel_count.csv")