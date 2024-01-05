# Write a Python program to find if a given string starts with a given character using Lambda. Output:True or False

my_string = "troleibusas"
my_char = "T"

check_first_char = lambda given_string, given_character: given_string.startswith(given_character)

print(check_first_char(my_string, my_char))
