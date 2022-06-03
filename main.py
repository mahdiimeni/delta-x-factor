from x_factor import x_factor
from tabulate import tabulate

pages = input("How many pages do you want to check?! > ")
table = tabulate(x_factor(int(pages)))

print(table)
