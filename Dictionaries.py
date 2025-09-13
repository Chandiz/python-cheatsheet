#################  Dictionaries ####################

################  Basics ######################

person = {"name": "Alice", "age": 25, "city": "Tokyo"}

print(person["name"])       # Alice
print(person.get("age"))    # 25

person["age"] = 26          # update
person["job"] = "Engineer"  # add
del person["city"]          # delete


######################  Looping  #######################

for key in person:
    print(key, person[key])

for key, value in person.items():
    print(key, value)

for value in person.values():
    print(value)


################  Dictionary Comprehension  ###################

squares = {x: x**2 for x in range(5)}
# {0:0, 1:1, 2:4, 3:9, 4:16}

