
def main():
    while True:
        try:
            fr = input("Fraction: ")
            pr = convert(fr)
            print(gauge(pr))
            break
        except (ValueError, ZeroDivisionError):
            continue


def convert(fraction):
    x, y = fraction.split("/")
    x, y = int(x), int(y)
    if y == 0 :
        raise ZeroDivisionError
    elif y < 0 or x > y or x < 0 :
        raise ValueError
    percentage = round((x / y) * 100)
    return percentage


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
