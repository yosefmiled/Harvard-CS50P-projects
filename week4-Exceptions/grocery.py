list = []
while True :
    try:
        item = input("").strip().upper()
        list.append(item)
    except EOFError:
        break

count = {}
for item in list :
    if item in count :
        count[item] += 1
    else :
        count[item] = 1

counts = sorted(count.keys())

for item in counts:
    print(f'{count[item]} {item}')




