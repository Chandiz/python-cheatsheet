###🐍 Python Small Scripts – CSV Reader & Sorting###

########## CSV Reader (Built-in csv module) #########

import csv

# Read CSV file
with open("data.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)   # read header row
    for row in reader:
        print(row)

# Read into Dict format
with open("data.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["age"])


################ Write CSV ###################

import csv

rows = [
    ["name", "age", "city"],
    ["Alice", 25, "Tokyo"],
    ["Bob", 30, "Osaka"]
]

with open("output.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)


##################  Sorting  ################

### Sorting list ###

nums = [5, 2, 9, 1]
nums.sort()          # [1, 2, 5, 9]
nums.sort(reverse=True)  # [9, 5, 2, 1]

# Sorted without modifying
sorted_nums = sorted(nums)

############## Sorting by Custom Key ###############

words = ["banana", "apple", "cherry"]
words.sort(key=len)  # ['apple', 'banana', 'cherry']


##############  Sort List of Dicts  ################

people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 20}
]

# Sort by age
sorted_people = sorted(people, key=lambda x: x["age"])
print(sorted_people)




