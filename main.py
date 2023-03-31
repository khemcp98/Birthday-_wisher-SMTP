import random
import os
import pandas as pd
import smtplib
import datetime as dt

user = 'youremail@gmail.com'
password = 'abcd12345'

PLACEHOLDER = '[NAME]'
now = dt.datetime.now()
month = now.month
day = now.day

letter_path = 'letter_templates'
letter = os.listdir(letter_path)

dates = pd.read_csv('birthdays.csv')
date = dates.to_dict(orient='records')
for birthday in date:
    if month == birthday['month'] and day == birthday['day']:
        with open(f'letter_templates/{random.choice(letter)}') as file:
            text = file.read()
            replaced_text = text.replace(PLACEHOLDER, birthday['name'])

        with smtplib.SMTP('smtp.gmail.com') as smtp:
            smtp.starttls()
            smtp.login(user=user, password=password)
            smtp.sendmail(from_addr=user,
                          to_addrs=birthday['email'],
                          msg=f'Subject:Happy Birthday\n\n{replaced_text}')
