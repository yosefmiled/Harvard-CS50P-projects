from pyfiglet import Figlet
import random
import sys
figlet = Figlet()

def main():

    list = figlet.getFonts()

    if len(sys.argv) == 1 :
        f = random.choice(list)
        figlet.setFont(font=f)

    elif len(sys.argv) == 3 :
        if sys.argv[2] not in list:
            sys.exit("Invalid usage")
        if sys.argv[1] not in ["-f" ,"--font"]:
            sys.exit("Invalid usage")
        f= sys.argv[2]
        figlet.setFont(font=f)

    else:
        sys.exit("Invalid usage")

    phrase = input("Input: ")
    print(figlet.renderText(phrase))

main()

