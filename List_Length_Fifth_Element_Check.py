# "4 - Write a Python program that accepts a list of integers and calculates the length and the fifth element.
# Return true if the length of the list is 8 and the fifth element occurs thrice in the said list.
# Input: [19, 19, 15, 5, 5, 5, 1, 2]
# Output: True
# Input: [19, 15, 5, 7, 5, 5, 2]
# Output: False
# Input: [11, 12, 14, 13, 14, 13, 15, 14]
# Output: True
# Input: [19, 15, 11, 7, 5, 6, 2]
# Output: False"


def myfunction(mylist):
    if len(mylist) > 8 and mylist.count(mylist[4]) >= 3:
        return True
    else:
        return False


my_list = []
my_limit = int(input("Enter Limit Of Your List: "))
my_count = 0
while my_count < my_limit:
    my_value = input()
    my_list.append(my_value)
    my_count += 1

print(F"your input list is {my_list}")
print(myfunction(my_list))
