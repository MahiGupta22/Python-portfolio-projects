# Creating a dictionary
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}
# Retrieving a value from a dictionary
print(programming_dictionary["Function"])
# Adding more items to a dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
# Creating an empty dictionary
empty_dictionary = {}
# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)
# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)
# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

#STUDENT SCORES
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
student_grades ={}
names=[]
names=student_scores.keys()
for i in names:
    if 100>=student_scores.get(i)>=91:
        Grade="Outstanding"
    elif 90>=student_scores.get(i)>=81:
        Grade="Exceeds Expectations"
    elif 80>=student_scores.get(i)>=71:
        Grade="Acceptable"
    elif 70>=student_scores.get(i)>=0:
        Grade="Fail"
    else:
        print("invalid")
    student_grades[i]=Grade
print(student_grades)

#NESTED LISTS AND DICTIONARY
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested List in Dictionary

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"],
# }

# print Lille
# print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]
# print(nested_list[2][1])

# Nested dictionary in a dictionary
travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}
print(travel_log["Germany"]["cities_visited"][2])

