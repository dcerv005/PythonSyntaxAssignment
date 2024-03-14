#Question 7 Task 1: Simple Logic Puzzle

water = True
tea_bag= True

making_tea = water and tea_bag

print(making_tea)

ingredients_making_tea = water or tea_bag

print(ingredients_making_tea)

making_tea = not water

print(making_tea)

#Question 7 Task 2: Validating Calculations

a = 5
b = 3
c = 2

combined = a + b * c

print(combined)


combined1 = (a + b) *c

print(combined1)

combined2 = combined == combined1

print(combined2)

#Question 7 Task 3: Mix and Match

mixed = a and b < c + a # outcome is True

print(mixed)