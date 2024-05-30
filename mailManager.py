from flask_mail import Message, Mail
from os import environ


def sendMail(mail:Mail, data:dict, archive=None):
    subject = data["subject"]
    #En caso de que sea uno solo, si necesitas enviar a varios, deves crear en tu vista html un selector multiple, recuperar los datos
    #y crear una lista con dichos recipientes
    recipient = data["recipient"]

    #Es el mensaje que deseas enviar en el cuerpo de tu correo
    body = data["body"]

    #Creas tu mensaje
    message = Message(subject = subject, sender=environ["MAIL_USERNAME"], recipients=[recipient])

    #Adjuntas el cuerpo
    message.body = body

    if archive != None:
        #Adjuntas tu archivo al mail
        message.attach(archive.filename, 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', archive.read())

    mail.send(message)