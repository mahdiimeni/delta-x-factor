from x_factor import x_factor
from tabulate import tabulate

pages = input("How many pages do you want to check?! > ")

tabulate_header = [
    "market_cap_rank",
    "id",
    "symbol",
    "X Factor",
]

table = x_factor(int(pages))

tabulate_table = tabulate(
    table, headers=tabulate_header, showindex="always", tablefmt="psql"
)

print(tabulate_table)
