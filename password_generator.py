# Task 3
# Password Generator
import random
import string
password_complexity = input('Write the complexity of Password: 1.Weak 2.Moderate 3.Strong : ')
if password_complexity == "Weak" or password_complexity == "weak":
    all_characters = string.ascii_lowercase + string.digits
if password_complexity == "Moderate" or password_complexity == "moderate":
    all_characters = string.ascii_letters + string.digits
if password_complexity == "Strong" or password_complexity == "strong":
    all_characters = string.ascii_letters + string.digits + string.punctuation
password_length = input("Please specify the desired length of Password: ")
if '.' in password_length:
    password_length = input("Please write the integer for the desired length of Password: ")
password_length = int(password_length)
if password_length <= 0:
    password_length = int(input("Please write the character greater than 0 for the desired length of Password: "))
for i in range(password_length):
    password = random.choice(all_characters)
    print(password, end='')


