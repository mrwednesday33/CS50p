import sys
import csv
from tabulate import tabulate

if len(sys.argv) != 2 or not sys.argv[1].endswith(".csv"):
    sys.exit("Usage: python pizza.py file.csv")

try:
    with open(sys.argv[1], newline="") as file:
        rows = csv.reader(file)
        header = next(rows)
        table = [row for row in rows]
        print(tabulate(table, headers=header, tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")
except csv.Error:
    sys.exit("Not a CSV file")
