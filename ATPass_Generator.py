
# APass_Generator

import random
import string

letters = list("abcdefghijklmnopqrstuvwxyz" + "123456789" + "~!@#$%^&*()-|\/.><\"")

password = []

pass_length = int(input("Enter the password length : "))


def pass_generate():
    for i in range(pass_length):
        password.append(random.choice(letters))

    random.shuffle(password)
    print("".join(password))


pass_generate()
