def main():
    camel=input("camelCase: ")
    convert(camel)
    
def convert(phrase):
    n = 0
    for l in phrase :
        n=n+1
        if l.islower():
            print(l, end='')
        else:
            if n == 1 :
                print(l.lower(),end='')
            else:
                print(f"_{l.lower()}",end='')
main()
