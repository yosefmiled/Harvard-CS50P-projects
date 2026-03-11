import sys
import csv

if len(sys.argv) < 3 :
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3 :
    sys.exit("Too many command-line arguments")
fileOne = sys.argv[1]
fileTwo = sys.argv[2]
if not fileOne.endswith(".csv") or not fileTwo.endswith(".csv") :
    sys.exit("Not a CSV file")
try:
    with open(fileOne, "r") as file :
        reader = csv.DictReader(file)
        with open(fileTwo, "w" ) as file :
            fieldnames = ["first","last","house"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for row in reader :
                lastname, firstname = row["name"].split(",")
                writer.writerow({
                    "first":firstname.strip(),
                    "last":lastname,
                    "house":row["house"]})

except FileNotFoundError :
    sys.exit("File does not exist")


