"""
Extracts a collection of birth dates from the user and determines if each individual is at least 21 years of age
"""
from date import Date

def main():
    born_before = Date(6, 1, 1988)

    # Extract birth dates from the user and determine if 21 or older
    date = prompt_and_extract_date()
    print(date)
    while date is not None:
        if date <= born_before:
            print("Is at least 21 years of age: ", date)
        date = prompt_and_extract_date()

# Prompts for and extracts the Gregorian date components
# Returns a Date object or None when the user has finished entering dates
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