from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "ferhatadibelli9@gmail.com"
MY_PASSWORD = "rhtqxhmmdhezofol"

today = datetime.now()
today_tuple = (today.day, today.month)

#Generally use pandas with csv
data = pandas.read_csv("birthdays.csv")
birthdays_data = {(row["day"], row["month"]): row for (index, row) in data.iterrows()}

if today_tuple in birthdays_data:
    user_info = birthdays_data[today_tuple]
    # Generally use with open with txt
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt", mode="r") as file:
        content = file.read()
        new_content = content.replace("[NAME]", user_info["name"])
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="ferhat@codeventure.co",
            msg=f"Subject:Anniversary \n\n ${new_content} "
        )
