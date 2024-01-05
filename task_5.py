# Write a Python program to sort a list of tuples using Lambda.

# # Original list of tuples:
# [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# # Sorted the List of Tuples:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]


my_list = [("English", 88), ("Science", 90), ("Maths", 97), ("Social sciences", 82)]


tuple_sorting = sorted(my_list, key=lambda my_list: my_list[1])

print(tuple_sorting)
