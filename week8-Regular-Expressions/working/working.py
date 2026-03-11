import re

def main():
    print(convert(input("Hours: ")))
def convert(s):
    if match := re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$", s , re.IGNORECASE):
        if match.group(2) != None : h12 = int(match.group(2))
        else : h12 = 0
        if match.group(5) != None : h22 = int(match.group(5))
        else: h22 = 0
        h1, t1 = int(match.group(1)), match.group(3)
        h2, t2 = int(match.group(4)), match.group(6)
        if h1==12 and h12>0 or h2==12 and h22>0 or h12>=60 or h22>=60:
            raise ValueError
        else:
            if t1 == "PM" and h1 != 12: h1= h1+12
            elif t2 == "PM" and h2!= 12: h2= h2+12
            elif h1 == 12 : h1 = 0
            elif h2 == 12 : h2 = 0
        return f"{h1:02}:{h12:02} to {h2:02}:{h22:02}"
    else:
        raise ValueError

if __name__ == "__main__" :
    main()

'''
9:00 AM to 5:00 PM
9 AM to 5 PM
9:00 AM to 5 PM
9 AM to 5:00 PM
'''
