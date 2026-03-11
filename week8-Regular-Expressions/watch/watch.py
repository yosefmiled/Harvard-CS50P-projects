import re

def main():
    print(parse(input("HTML: ")))

def parse(s):

    if match := re.search(r"^<iframe([\w*|\d*| *])src= ?\"https?://(www\.)?youtube\.com/embed/([a-z0-9]+)\"", s , re.IGNORECASE) :
        return f"https://youtu.be/{match.group(3)}"
    else:
        return None


if __name__ == "__main__" :
    main()


'''
http://youtube.com/embed/xvFZjo5PgG0
https://youtube.com/embed/xvFZjo5PgG0
https://www.youtube.com/embed/xvFZjo5PgG0

https://youtu.be/xvFZjo5PgG0
'''
