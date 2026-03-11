months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ").strip()

    if "/" in date:
        try:
            m, d, y = date.split("/")
            m, d, y = int(m), int(d), int(y)
            if 1 <= m <= 12 and 1 <= d <= 31:
                print(f"{y:04}-{m:02}-{d:02}")
                break
        except ValueError:
            pass

    elif "," in date :
        try:
            parts = date.replace(",", "").split()
            if len(parts) == 3:
                m, d, y = parts
                d = int(d)
                y = int(y)
                m = months.index(m) + 1
                if 1 <= m <= 12 and 1 <= d <= 31:
                    print(f"{y:04}-{m:02}-{d:02}")
                    break
        except (ValueError, IndexError):
            pass

    continue




