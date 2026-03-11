from datetime import date
import re
import sys
import inflect
p= inflect.engine()

def main():
    birth_date = input("Date of Birth: ")
    try:
        year, month, day = check_birthday(birth_date)
    except:
        sys.exit("Invalid date")
    output = minutes(year,month,day).capitalize()
    print(output + " minutes")
def minutes(year, month, day):
    date_birth = date(int(year), int(month), int(day))
    date_today = date.today()
    sub = date_today - date_birth
    minutes = sub.days*24*60
    output = p.number_to_words(minutes, andword="")
    return output

def check_birthday(birth_date):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birth_date):
        year, month, day = birth_date.split("-")
        return year, month, day


if __name__ == "__main__":
    main()
