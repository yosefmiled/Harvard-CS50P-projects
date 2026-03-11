def main():
    greeting = str(input("Greeting: ")).lower().strip()
    print(f"${value(greeting)}")

def value(greeting):
    if greeting.startswith("h"):
        return 20
    elif greeting.startswith("hello"):
        return 0
    else :
        return 100

if __name__ == "__main__":
    main()
