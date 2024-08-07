# import smtplib
#
# email = "mytaxes.mas@gmail.com"
# password = "osxv sofl vywk zyyn"
# with smtplib.SMTP('smtp.gmail.com') as connection:
#     connection.starttls()
#     connection.login(user=email, password=password)
#     connection.sendmail(from_addr=email, to_addrs="yaroslava.masliiy@gmail.com", msg="Subject:Hello\n\nThis is my first email with smtp")
#
# import datetime as dt
# now = dt.datetime.now()
# now = dt.datetime(year=2024, month=7, day=22)
# week_day = now.weekday()
# print(week_day)


import datetime as dt
import random, smtplib
import pandas

# 1. Update the birthdays.csv +
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME]
# with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.

email ="mytaxes.mas@gmail.com"
password  = "osxv sofl vywk zyyn"
wishes = []


def check_what_is_day_today():
    today = dt.datetime.now()
    today_tuple = (today.month, today.day)
    return (today_tuple)

def check_who_have_birthday():
    today=check_what_is_day_today()
    data = pandas.read_csv('birthdays.csv')
    birthday_dict = {(data_row["month"], data_row["day"]): data_row for index, data_row in data.iterrows()}
    print(birthday_dict)
    if today in birthday_dict:
        birthday_person = birthday_dict[today]
        current_file = f"letter_templates/letter_{random.randint(1,3)}.txt"
        with open(current_file) as letter_file:
            contents = letter_file.read()
            contents  = contents.replace('[NAME]', birthday_person['name'])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email, to_addrs=birthday_person['email'],
                                msg=f"Subject:Congradulations with your BD\n\n{contents}")


# with open ("quotes.txt") as file:
#     data = file.readlines()
#     wishes = random.choice(data)
#     print(wishes)

# #sent_email()
# check_what_is_day_today()
check_who_have_birthday()