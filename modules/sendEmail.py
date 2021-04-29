import smtplib
from email.mime.text import MIMEText
from email.header import Header
from datetime import datetime
from settings.credentials import *

class SendEmail():
    def __init__(self):
        pass

    def sendEmail(self,system):
        to_email = open('C:/Automations/loadingTimeUrl/control/recepients.txt', 'r').readlines()
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login("" + CRD_EMAIL + "",
                     "" + CRD_PWD_EMAIL + "")
        body = "O sistema "+system+" está apresentando indisponibilidade.\n\n" \
               "Favor verificar.\n\n\n" \
               "Email automático."

        subject = "INDISPONIBILIDADE DE APLICAÇÃO"
        from_email = "" + CRD_EMAIL + ""
        to = to_email
        msg = MIMEText(body, 'plain', 'utf-8')
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = Header(from_email, 'utf-8')
        # msg['To'] = Header(to, 'utf-8')
        text = msg.as_string()

        try:
            server.sendmail(from_email, to_email, text)
            log = open('C:/Automations/loadingTimeUrl/control/logError.txt', 'a')
            log.writelines(str(datetime.now().strftime('%d/%m/%Y-%H:%M:%S') + ": Enviado email com sucesso sobre indisponibilidade do sistema " + system + "\n"))
            log.close()
        except:
            log = open('C:/Automations/loadingTimeUrl/control/logError.txt', 'a')
            log.writelines(str(datetime.now().strftime('%d/%m/%Y-%H:%M:%S') + ": Erro ao enviar email sobre indisponibilidade do sistema " + system + "\n"))
            log.close()