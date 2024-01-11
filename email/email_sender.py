import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path    # or os.path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Aalya Vora'
email['to'] = 'avora110@gmail.com'
email['subject'] = 'sending 1st email'

email.set_content(html.substitute({'name': 'Aalya'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('avora110@gmail.com', 'A@lya240603!()')
  smtp.send_message(email)
  print('welcomeem!')