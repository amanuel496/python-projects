import datetime as dt
import random
import smtplib
import pandas as pd

MY_EMAIL = <email>
PASSWORD = <password>


def main():
    birthdays = (pd.read_csv("./birthdays.csv")).to_dict(orient='split')["data"]
    month = dt.datetime.now().month
    day = dt.datetime.now().day

    for birthday in birthdays:
        if month == birthday[3] and day == birthday[4]:
            name = birthday[0]
            email = birthday[1]

            with open("./letter_templates/letter_1.txt") as letter_file:
                letter_1 = letter_file.readlines()
            with open("./letter_templates/letter_1.txt") as letter_file:
                letter_2 = letter_file.readlines()
            with open("./letter_templates/letter_1.txt") as letter_file:
                letter_3 = letter_file.readlines()

            letter = random.choice([letter_1, letter_2, letter_3])

            letter[0] = letter[0].replace("[NAME]", name)
            result = ''.join(letter)
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL, to_addrs=email, msg=f"Subject: Birthday Wish\n\n{result}")


if __name__ == "__main__":
    main()
