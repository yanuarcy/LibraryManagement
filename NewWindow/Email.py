import smtplib, ssl
from getpass import getpass



message = """\
Subject: HELLOO kali ini kita kluarkan dri fungsi!!

    Hellowww there kita coba apkah berhasil iya manieezz!           """ 


def KirimEmail():
    port = 587  # For starttls
    smtp_server = "smtp.office365.com"
    sender_email = "yanuarcahyo567@gmail.com"
    receiver_email = input("Enter receiver email: ")
    password = getpass("Enter your password: ")
    # Subject = "HELLOO kali ini kita kluarkan dri fungsi!!" 
    # Textt = "Hellowww there kita coba apkah berhasil iya manieezz!"
    # message = """\
    # Subject: haaiiiiiii yanuarr

    #             Haii ini aku yanuar yg ganteng          """
    


    print("Sending mail...")
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        print("mail send")

    # def SendMailf(self):
    #     print("Sending mail...")
    #     context = ssl.create_default_context()
    #     with smtplib.SMTP(smtp_server, port) as server:
    #         server.ehlo()  # Can be omitted
    #         server.starttls(context=context)
    #         server.ehlo()  # Can be omitted
    #         server.login(sender_email, password)
    #         server.sendmail(sender_email, receiver_email, message)
    #         print("mail send")

if __name__ == "__main__":
    KirimEmail()

    