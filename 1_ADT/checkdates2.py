from bag import Bag
from date import Date

def main():
    born_before = Date(6, 1, 1988)
    bag = Bag()

    date = prompt_and_extract_date()
    while date is not None:
        bag.add(date)
        date = prompt_and_extract_date()

    for date in bag:
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