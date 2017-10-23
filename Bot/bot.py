import random as rd

nums = []
for t in range(10):
    nums.append(rd.randint(0, 100))
    print(sorted(nums))
