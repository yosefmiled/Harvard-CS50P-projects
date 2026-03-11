def main():
    fr = input("Fraction: ")
    print(convert(fr))
def convert(fr):
    while True :
        try:
            percentage = round((int(fr.split("/")[0])/int(fr.split("/")[1]))*100)
            if not 0<=percentage<=100 :
                fr = input("Fraction: ")
            elif percentage <= 1 :
                return "E"
            elif percentage >= 99 :
                return "F"
            else :
                return f"{percentage}%"
        except ValueError:
            fr = input("Fraction: ")
        except ZeroDivisionError:
            fr = input("Fraction: ")
        else:
            fr = input("Fraction: ")
main()

"""
def main():
    while True:
        fr = input("Fraction: ")
        try:
            print(convert(fr))
            break
        except (ValueError, ZeroDivisionError):
            continue


def convert(fr):
    x, y = fr.split("/")
    x, y = int(x), int(y)

    if y == 0 or x > y:
        raise ValueError

    percentage = round((x / y) * 100)

    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
"""
