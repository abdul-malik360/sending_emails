import smtplib

s = smtplib.SMTP('smtp.gmail.com', 587)
sender_email_id = 'abdulmalikmohamed360@gmail.com'
receiver_email_id = 'kiyaamudienkhan@gmail.com'
password = input("Enter sender password")
s.starttls()
s.login(sender_email_id, password)
message = "Salaam bru, when we gonna dala the braai?\n"
message = message + "you must lemme know bro"

s.sendmail(sender_email_id, receiver_email_id, message)
s.quit()

