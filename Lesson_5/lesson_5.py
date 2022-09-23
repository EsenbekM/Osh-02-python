# import calculator
# from calculator import addition
# from calculator import subtruction as s
# from calculator import *
#
#
# print(calculator.mult(2, 2))
# print(addition(8, 9))
# print(s(5, 3))

# from random import randint
#
# print(randint(1, 100))

# import datetime
#
# # print(datetime.datetime.now())
#
# now = datetime.datetime.now().date()
# yesterday = datetime.datetime(2022, 9, 22).date()
#
# print(type(now), now)
# print(type(yesterday), yesterday)
#
# date_x = '12/08/2004'
# date_x_datetime = datetime.datetime.strptime(date_x, "%d/%m/%Y").date()
#
# print(date_x_datetime)
#
# print(now - date_x_datetime)
#
# time_start = datetime.datetime.now()
#
# for i in range(1_000_000):
#     print("Hello")
#
# print(datetime.datetime.now() - time_start)

# from termcolor import cprint
#
# cprint("Hello world", color="red", on_color="on_green", attrs=['bold', 'underline'])

from decouple import config

passw = config("PASSWORD", cast=int)
token = config("TOKEN", default="hahaha")

print(type(passw), passw)
print(token)

