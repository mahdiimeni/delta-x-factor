from x_factor import x_factor
from tabulate import tabulate


def main():
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

    return tabulate_table


print(main())
