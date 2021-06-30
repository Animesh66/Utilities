import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)  # SSL is required to send the email in secured manner
# it required the IP of the mail server and the PORT number
server.login("sendermail@email.com", "password")
server.sendmail("senderemail@email.com", "receiveremail@email.com", "Email body")
server.quit()
