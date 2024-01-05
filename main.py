# def get_str_len(string_to_check: str) -> int:
#     return -len(string_to_check)


# animals = ["ferret", "vole", "dog", "gecko"]

# print(sorted(animals, key=get_str_len))

#########
# from typing import Callable


# def add_two_nums(a: int, b: int) -> int:
#     return a + b


# def add_another_two_nums(number: int, number_func: Callable):
#     return number_func(2, number)

# print(add_another_two_nums(number=4, number_func=add_two_nums))


# def get_str_len(string_to_check: str) -> int:
#     return -len(string_to_check)


# animals = ["ferret", "vole", "dog", "gecko"]

# print(sorted(animals, key=get_str_len))

#########
# from typing import Callable


# def add_two_nums(a: int, b: int) -> int:
#     return a + b


# def add_another_two_nums(number_func: Callable):
#     return number_func


# # print(add_another_two_nums(number=4, number_func=add_two_nums))
# value = add_another_two_nums(number_func=add_two_nums)
# print(value(2, 4))
# print(type(value), value.__name__)

#########

reverse = lambda s: s[::-1]
print(reverse("I am a string"))
# 'gnirts a ma I'


print(callable(lambda s: s[::-1]))
# True

animals = ["ferret", "vole", "dog", "gecko"]
print(sorted(animals, key=lambda s: -len(s)))
# ['ferret', 'gecko', 'vole', 'dog']
