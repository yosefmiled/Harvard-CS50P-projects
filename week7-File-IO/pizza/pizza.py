import csv
from tabulate import tabulate
import sys

if len(sys.argv) < 2 :
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2 :
    sys.exit("Too many command-line arguments")
file = sys.argv[1]
if not file.endswith(".csv"):
    sys.exit("Not a CSV file")


with open(file, "r") as file :
    reader = csv.reader(file)
    table = []
    for row in reader :
        table.append(row)
    print(tabulate(table, headers = "firstrow" , tablefmt="grid"))


