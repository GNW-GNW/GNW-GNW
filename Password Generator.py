import random

lower_case = "abcdefghijklmonpqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMONPQRSTUVWXYZ"
number = "0123456789"
symbols = "!@#$%^&*()-_=/*-+`"

Use_for = lower_case + upper_case + number + symbols
length_for_pass = 10

password = "".join(random.sample(Use_for, length_for_pass))

print("Your Generated Password is " + password)