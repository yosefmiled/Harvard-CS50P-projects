def main():
    word = input("Input: ")
    print(shorten(word))


def shorten(word):
    for char in word :
        if char in ["a","A","i","I","e","E","u","U","o","O"]:
            word = word.replace(char, "")
    return word


if __name__ == "__main__":
    main()
