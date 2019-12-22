import smtplib, ssl

#port=465
port=587
password="2Run-re#6564"
message = "TE SARUT DULCE DE LANGA PRIETENA MEA CEA MAI BUNA, RASPI"
smtp_server = "smtp.gmail.com"
sender_email = "ivan.adelina02@gmail.com"
reciever_email = "brancsebastian@gmail.com"

context = ssl.create_default_context()

server = smtplib.SMTP(smtp_server, port)
server.starttls()
server.login(sender_email, password)
server.sendmail(sender_email, reciever_email, message)
server.quit()
