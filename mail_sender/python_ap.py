# go over to out gmail account and setup 2 facto authentication 
# generete app pasword 
# create a funcation to send the mail 



from email.message import EmailMessage
from app2 import password
import ssl
import smtplib




email_sender = 'xxxxxx@gmail.com'
email_password = password

email_reciver = 'rosihe9215@3mkz.com'

subject = "Your Subject"

body = """
When you watch video, please hit subscribe
"""


em = EmailMessage()

em['From'] = email_sender
em['To'] = email_reciver
em['subject'] = subject
em.set_content(body)



context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:

    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciver, em.as_string())