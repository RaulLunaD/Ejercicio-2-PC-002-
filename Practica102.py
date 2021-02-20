# Creado por Raul Jahziel

import tkinter
from email import encoders
from email.mime.base import MIMEBase
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import ssl

# =============================================================================

vt = tkinter.Tk()

vt.geometry("685x450")

vt.config(bg = "black")

# vt.iconbitmap("mail.ico")

vt.title("Correos")

def enviar():
    de = caja1.get()
    pswd = caja2.get()
    to = caja3.get()
    subject = caja4.get()
    msg = caja5.get()
    meme = caja6.get()
    
    message = MIMEMultipart()
    message["From"] = de
    message["To"] = to
    message["Subject"] = subject


    message.attach(MIMEText(msg, 'plain'))


    filename = meme


    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

  
    encoders.encode_base64(part)


    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )


    message.attach(part)


    context = ssl.create_default_context()
    with smtplib.SMTP("smtp.office365.com", 587) as server:
        server.ehlo()
        server.starttls(context=context)
        server.login(de, pswd)
        server.sendmail(
            de, to, message.as_string()
        )
    pls = tkinter.Label(vt, text = "ENVIADO!!!", font = "Arial 13", bg = "black", fg = "blue")
    pls.place(x=20, y= 290)

# ============================================================================
    
pl = tkinter.Label(vt, text = "ENVIA UN ARCHIVO POR CORREO ELECTRONICO A TUS AMIGOS!", font = "Arial 14", bg = "black", fg = "white")
pl.place(x=35, y= 10)

pl1 = tkinter.Label(vt,text = "Usuario (Correo Electronico de Uanl): ", font = "Arial 10", bg = "black", fg = "white")
pl1.place(x = 20, y = 50)
caja1 = tkinter.Entry(vt, width = 30, font = "Arial 10", bg = "gray")
caja1.place(x = 248, y = 50)

pl2 = tkinter.Label(vt,text = "Contraseña: ", font = "Arial 10", bg = "black", fg = "white")
pl2.place(x = 20, y = 90)
caja2 = tkinter.Entry(vt, width = 30, font = "Arial 10", bg = "gray", fg = "gray")
caja2.place(x = 100, y = 90)

pl3 = tkinter.Label(vt,text = "Destinatario: ", font = "Arial 10", bg = "black", fg = "white")
pl3.place(x = 20, y = 130)
caja3 = tkinter.Entry(vt, width = 30, font = "Arial 10", bg = "gray")
caja3.place(x = 100, y = 130)

pl4 = tkinter.Label(vt,text = "Asunto: ", font = "Arial 10", bg = "black", fg = "white")
pl4.place(x = 20, y = 170)
caja4 = tkinter.Entry(vt, width = 30, font = "Arial 10", bg = "gray")
caja4.place(x = 100, y = 170)

pl5 = tkinter.Label(vt,text = "Mensaje: ", font = "Arial 10", bg = "black", fg = "white")
pl5.place(x = 20, y = 210)
caja5 = tkinter.Entry(vt, font = "Arial 10", width = 80 , bg = "gray")
caja5.place(x = 100, y = 210)


pl6 = tkinter.Label(vt,text = "Archivo: ", font = "Arial 10", bg = "black", fg = "white")
pl6.place(x = 20, y = 250)
caja6 = tkinter.Entry(vt, width = 35,font = "Arial 10", bg = "gray")
caja6.place(x = 100, y = 250)

boton1 = tkinter.Button(vt, command = enviar, text = "Enviar", width = 6, height = 2, bg = "gray", fg = "black")
boton1.place(x = 610, y = 250)

# ============================================================================

vt.mainloop()