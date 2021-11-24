import smtplib
server = smtplib.SMTP_SSL("smtp.gmail.com" , 465)
email = "YOUR GMAIL ID"
password = "YOUR GMAIL PASSWORD"
target = "EMAIL ID OF PERSON YOU WANT TO SEND MAIL" 
server.login(email, password)
server.sendmail(email , target , "YOUR MESSAGE")
print("Sent Mail")
server.quit()