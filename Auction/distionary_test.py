programing_dictionarry = {
    "Bug": "A bug is an error or flaw in a computer program that causes it to behave unexpectedly or incorrectly.",
    "Function": "A function is a block of code designed to perform a specific task. Functions are used to organize code, make it reusable, and improve readability.",
    
}

# print(programing_dictionarry["Bug"])

# programing_dictionarry["Loop"] = "The action of doing something over and over again."

# empty_dictionary = {}

# # programing_dictionarry = {}
# # print(programing_dictionarry)

# programing_dictionarry["Bug"] = "A moth in your computer."

# # print(programing_dictionarry["Bug"])


# for key in programing_dictionarry:
#     print(key)
#     print(programing_dictionarry[key])

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# travel_log = {
#     "France": ["France", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"],
# }

# print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]

# print(nested_list[2][1])

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 8,
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
}

print(travel_log["Germany"]["cities_visited"][2])