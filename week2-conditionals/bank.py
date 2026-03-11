def start_w_H(grt):
    if grt.startswith("h"):
        return True
    else:
        return False
def start_w_Hello(grtt):
    if grtt.startswith("hello"):
        return True
    else:
        return False
def main():
    greeting = str(input("Greeting: ")).lower().strip()
    if start_w_Hello(greeting):
        print("$0")
    elif start_w_H(greeting):
        print("$20")
    else:
        print("$100")
main()

