# import smtplib
#
# user = "ferhatadibelli9@gmail.com"
# password = "***************"
#
# with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
#     connection.starttls()
#     connection.login(user= user, password= password)
#     connection.sendmail(
#         from_addr=user,
#         to_addrs="ferhat@codeventure.co",
#         msg="Subject:Hello\n\n This is body of content"
#     )

import datetime as dt

now = dt.datetime.now()
print(now.weekday())
print(dt.datetime(year=2303, month=3, day=23))