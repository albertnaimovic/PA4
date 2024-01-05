# Write a Python program to square and cube every number in a given list of integers using Lambda.


square_and_cube = lambda my_list: ([x**2 for x in my_list], [x**3 for x in my_list])

my_list = [1, 2, 3, 4]

print(square_and_cube(my_list=my_list))
