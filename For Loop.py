######################For Loop#############################

# Iterate over a list
for item in [1, 2, 3]:
    print(item)

# Iterate over a range
for i in range(5):  # 0 → 4
    print(i)

# Iterate with index
nums = [10, 20, 30]
for i, val in enumerate(nums):
    print(i, val)


##################### While Loop ##########################

x = 0
while x < 5:
    print(x)
    x += 1


#################### Loop Controls ########################

for i in range(10):
    if i == 3:
        continue  # skip this iteration
    if i == 7:
        break     # stop loop
    print(i)
