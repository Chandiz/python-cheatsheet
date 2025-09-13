###################  Lists  ####################

########  Basics  #########

fruits = ["apple", "banana", "cherry"]

print(fruits[0])      # access → "apple"
print(fruits[-1])     # last item → "cherry"

fruits.append("date") # add item
fruits.insert(1, "kiwi")  # insert at index
fruits.remove("banana")   # remove by value
popped = fruits.pop()     # remove last item


####################  Slicing  ################

nums = [0,1,2,3,4,5]
print(nums[2:5])   # [2, 3, 4]
print(nums[:3])    # [0, 1, 2]
print(nums[::2])   # [0, 2, 4]


###################  List Comprehension ###############

squares = [x**2 for x in range(5)]  # [0,1,4,9,16]
evens = [x for x in range(10) if x % 2 == 0]  # [0,2,4,6,8]


