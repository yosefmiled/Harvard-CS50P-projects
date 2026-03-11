import random

def main():
    lvl = level()
    guess(lvl)

def level():
    while True:
        try:
            n = input("Level: ")
            if int(n)>0 :
                lvl = random.randint(1, int(n))
                return lvl
        except ValueError :
            continue

def guess(k):
    while True:
        try:
            n = int(input("Guess: "))
            if n>0 :
                if k > n :
                    print("Too small!")
                elif k < n :
                    print("Too large!")
                else :
                    print("Just right!")
                    break
        except ValueError :
            continue

main()
