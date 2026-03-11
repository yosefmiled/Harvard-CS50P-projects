import sys
from PIL import ImageOps
from PIL import Image
import os


def main():
    try:
        input, output = filenames()
        shirt = Image.open("shirt.png")
        w, h = shirt.size
        size = (w, h)
        with Image.open(input) as im :
            fit = ImageOps.fit(im , size)
            fit.paste(shirt, mask=shirt)
            fit.save(output)
    except FileNotFoundError:
        sys.exit("file not found")
        
def filenames() :
    if len(sys.argv) < 3 :
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3 :
        sys.exit("Too many command-line arguments")
    try:
        input = sys.argv[1]
        output = sys.argv[2]
        one, extI = os.path.splitext(input)
        two, extII = os.path.splitext(output)
        if extI != extII:
            raise SyntaxError
        elif extI and extII not in [".jpg",".jpeg",".png"]:
            raise TypeError
        return input, output
    except SyntaxError :
        sys.exit("Input and output have different extensions")
    except TypeError :
        sys.exit("Invalid input")


if __name__ == "__main__" :
    main()




