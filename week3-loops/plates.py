def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
def is_valid(s):
    for char in s :
        if 2<=len(s)<=6 :
            if s[0].isalpha() and s[1].isalpha():
                if ponc(s) == True and zero(s) == True and middle(s) == True:
                    return True
        else :
            return False
def zero(s):
    let=""
    dig=""
    for char in s :
        if char.isdigit():
            dig += char
        else:
            let += char
    if dig.startswith("0") :
        return False
    else :
        return True
def middle(s):
    digit_seen = False
    for char in s:
        if char.isdigit():
            digit_seen = True
        elif digit_seen and char.isalpha():
            return False
    return True
def ponc(s):
    for char in s :
        if char in [" ",".","!",",","?",":",";"]:          #if not char.isalnum():
            return False
    return True


main()
