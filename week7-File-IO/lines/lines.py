import sys

if len(sys.argv)< 2 :
    sys.exit("Too few command-line arguments")
elif len(sys.argv)>2 :
    sys.exit("Too many command-line arguments")
file = sys.argv[1]
if not file.endswith(".py") :
    sys.exit("Not a Python file")
try:
    with open(file, "r") as file :
        lines = 0
        for line in file:
            line = line.lstrip().rstrip()
            if line.startswith("#") :
                pass
            elif line == "" :
                pass
            else:
                lines += 1
    print(lines)

except FileNotFoundError :
    sys.exit("File does not exist")
