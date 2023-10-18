# Task 1
list = [1, 2, 3, 4, 5, 6, 7]

dict = {x: x**3 for x in list if x % 2 != 0}

print(dict)

# Task 2
list1 = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]

res_set = {x for x in list1 if x % 2 == 0}

print(res_set)

# Task 3
list2 = [x * 10 for x in range(10)]

print(list2)