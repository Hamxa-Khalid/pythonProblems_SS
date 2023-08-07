# "3 - Write a Python program that accepts a sequence of comma-separated numbers
# from the user and generates a list and a tuple of those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')"

numbers = input("Enter numbers separated with comma: ")
my_list = numbers.split(", ")

my_tuple = tuple(my_list)

print(F"Input Is {numbers} ")
print(F"My List Is {my_list}")
print(F"My Tuple Is {my_tuple}")
