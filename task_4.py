# Write a Python program to extract year, month, date and time using Lambda.

# input:
# 2020-01-15 09:03:32.744178
# Sample Output:
# 2020
# 1
# 15
# 09:03:32.744178

# extract_date = lambda my_date:
from datetime import datetime

# my_date = "2020-01-15 09:03:32.744178"

# get_formatted_data = (
#     lambda my_date: f'{datetime.strptime(my_date, "%Y-%m-%d %H:%M:%S.%f").year}\n{datetime.strptime(my_date, "%Y-%m-%d %H:%M:%S.%f").month}\n{datetime.strptime(my_date, "%Y-%m-%d %H:%M:%S.%f").day}\n{datetime.strptime(my_date, "%Y-%m-%d %H:%M:%S.%f").time()}'
# )


my_date = datetime.now()

get_formatted_data = (lambda my_date: f"{my_date.year}\n{my_date.month}\n{my_date.day}\n{my_date.time()}\n")

print(get_formatted_data(my_date=my_date))
