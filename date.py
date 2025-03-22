print("=== start date ===")

import datetime

# format Y-m-d
data = datetime.datetime.now()
print(data.strftime("%Y-%m-%d"))

# format d/m/Y
print(data.strftime("%d/%m/%Y %I:%M:%S %p"))

# get day of week
print(data.strftime("%A"))
print(data.strftime("%a"))
print(data.strftime("%w"))

# get month
print(data.strftime("%B"))
print(data.strftime("%b"))
print(data.strftime("%m"))

new = datetime.datetime(2020, 5, 17)
print(new.strftime("%Y-%m-%d"))
