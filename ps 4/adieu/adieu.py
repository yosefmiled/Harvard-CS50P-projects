import inflect
p = inflect.engine()

try :
    names = []
    while True:
        h = input("Name: ")
        names.append(h)

except EOFError:
    print('')
    print(f"Adieu, adieu, to {p.join(names)}")

