import smtplib
from dotenv import load_dotenv
import os

my_email = os.getenv
my_password = os.getenv("PASSWORD")

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=my_password)
connection.sendmail(from_addr=my_email, to_addrs="my_email", msg="Subject:Hello\n\nThis is the body of my email.") 
connection.close()