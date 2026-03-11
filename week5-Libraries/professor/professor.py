




import random

def main():
    level = get_level()
    n=0
    for i in range(10):
        while True :
            try:
                x = generate_integer(level)
                y = generate_integer(level)
                for i in range(3):
                    try:
                        rep=int(input(f"{x} + {y} = "))
                        v_rep = x+y
                        if rep == v_rep :
                            n+=1
                            break
                        else:
                            raise ValueError
                    except ValueError :
                            print("EEE")
                            if i == 2 :
                                print(f"{x} + {y} = {v_rep}")
                            continue
                break
            except ValueError :
                continue
    print(f"Score: {n}")

def get_level():
    while True :
        try:
            level=int(input("Level: "))
            levels=[1,2,3]
            if level not in levels :
                raise ValueError
            return level
        except ValueError :
            continue

def generate_integer(level):
    if level == 1 :
        x=random.randint(0,9)
    elif level == 2:
        x=random.randint(10,99)
    else :
        x=random.randint(100,999)
    return x

if __name__ == "__main__":
    main()
