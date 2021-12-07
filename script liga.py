import smtplib
import csv
import random
from email.message import EmailMessage
contacts = []
name = []
emailaddress = ''
password = ''
with open('lista.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for line in csv_reader:
        contacts.append(line[1])
        name.append(line[0])
msg = EmailMessage()
msg['Subject'] = 'Secret Santa Match'
msg['From'] = emailaddress
ordine = list(range(0, len(contacts)))
random.shuffle(ordine)
ok = 1
c = 0
while ok != 0:
    print(ordine)
    c = 0
    for line in ordine:
        if line == ordine.index(line):
            c += 1
    if c == 0:
        ok = 0
    else:
        random.shuffle(ordine)
# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#     for line in contacts:
#         msg['To'] = line
#         msg.set_content(name[ordine[contacts.index(line)]])
#         smtp.login(emailaddress, password)
#         smtp.send_message(msg)
#         del msg['To']
