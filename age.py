from datetime import datetime


def calculate_age(birth_date):
    birth_date = datetime.strptime(birth_date, "%d-%m-%Y")
    today = datetime.today()  # current date
    age = today.year - birth_date.year

    # adjust age if birthday hasn't occurred yet this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    return age


input_date = input("What is your date of birth? (DD-MM-YYYY): ")
age = calculate_age(input_date)
print(f"Age is: {age} years old.")
