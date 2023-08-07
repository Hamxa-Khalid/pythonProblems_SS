# 1 - Write a Python program to display the current date and time.
from datetime import datetime

now = datetime.now()
current = now.strftime("%d-%b-%Y %H:%M:%S %a")
print("Current date and time =", current)
