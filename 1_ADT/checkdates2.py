from bag import Bag
from date import Date

def main():
    born_before = Date(6, 1, 1988)
    print(born_before)
    bag = Bag()

    date = prompt_and_extract_date()
    while date is not None:
        bag.add(date)
        print(date)
        date = prompt_and_extract_date()

    print(len(bag))
    for date in bag:
        print(date)
        if date <= born_before:
            print("Should be atleast 21 years of age", date)


def prompt_and_extract_date():
    print("Enter a birth date.")
    month = int(input("month (0 to quit): "))
    if month == 0:
        return None
    else:
        day = int(input("day: "))
        year = int(input("year: "))
        return Date(month, day, year)

main()