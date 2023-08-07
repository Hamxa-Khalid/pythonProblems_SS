# 2 - Write a Python program that accepts the user's first and last name
# and prints them in reverse order with a space between them.

first_name = input("Enter your First Name: ")
last_name = input("Enter your Last Name: ")

print(f"Reverse of {first_name} & {last_name} is: {first_name[::-1]} {last_name[::-1]}")

