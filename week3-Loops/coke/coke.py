def main():
    price = 50
    print(f"Amount Due: {price}")
    sub(price)

def sub(price):
    while price > 0:
            coin = int(input("Insert Coin: "))
            if coin in [5, 10, 25]:
                price -= coin
                if price <= 0 :
                    print (f"Change Owed: {abs(price)}")
                    break
                else :
                    print(f"Amount Due: {price}")
            else :
                print(f"Amount Due: {price}")
                continue
main()
