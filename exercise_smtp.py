import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email_id = 'abdulmalikmohamed360@gmail.com'
receiver_email_id = ['thapelo@lifechoices.co.za', 'kiyaamudienkhan@gmail.com', 'uthmaanbreda@gmail.com', "abdullah.isaacs@gmail.com"]
password = input("Enter your password: ")
subject = "Link up at Uthmaan's place"
msg = MIMEMultipart()
msg['From'] = sender_email_id
msg['To'] = ",".join(receiver_email_id)
msg['Subject'] = subject
body = "When are we going to have the braai?\n"
body = body + "Thapelo is supplying the meat"
msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()
s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

s.login(sender_email_id, password)


s.sendmail(sender_email_id, receiver_email_id, text)

s.quit()
