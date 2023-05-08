import datetime
import smtplib, ssl
from getpass import getpass
import time
import pyautogui as pg

# time.sleep(10)

# for i in range(500):
#     pg.write("HAAIII, KAMU LAGI APA")
#     pg.press("enter")


# tgl = int(input("Masukkan berapa lama peminjaman: "))
# d1 = datetime.date(2022, 3, 2)
# d2 = datetime.timedelta(days= tgl)
# d3 = d1+d2
# d4 = datetime.date.today()
# print(d1)
# print(d3)
# print(d2.days)
# d5 = d3 - d4
# print(d5.days)


# message = """\
# Subject: Library Management System

#     Mohon Maaf tepat pada hari ini waktu peminjaman anda telah habis!!
#     Dimohon untuk mengembalikan kembali buku yang telah anda pinjam.           """ 


# def KirimEmail():
#     port = 587  # For starttls
#     smtp_server = "smtp.office365.com"
#     sender_email = "yanuarcahyo567@gmail.com"
#     receiver_email = "yanuarcygithub1@gmail.com"
#     password = "boboho567"
#     print("Sending mail...")
#     context = ssl.create_default_context()
#     with smtplib.SMTP(smtp_server, port) as server:
#         server.ehlo()  # Can be omitted
#         server.starttls(context=context)
#         server.ehlo()  # Can be omitted
#         server.login(sender_email, password)
#         server.sendmail(sender_email, receiver_email, message)
#         print("mail send")

# if d5.days == 0:
#     KirimEmail()


# print("pomodoro starts now!")
# for i in range(1):
#     t = 10*60
#     while t:
#         mins = t // 60
#         secs = t % 60
#         timer = '{:02d}:{:02d}'.format(mins, secs)
#         print('' + timer, end='\r')
#         time.sleep(0.01)
#         t -= 1
#     print("break time")

# day = 1
# hour = day * 24
# minute = hour * 60
# second = minute * 60


# while True:
#     uin = d5.days
#     try:
#         when_to_stop = int(uin)
#         hour = when_to_stop * 24
#         minute = hour * 60
#         second = minute * 60
#         abc = abs(int(second))
#     except KeyboardInterrupt:
#         break
#     except:
#         print("Not a Number!")

#     while abc > 0:
#         m, s = divmod(abc, 60)
#         h, m = divmod(m, 60)
#         time_left = str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
#         print(time_left + "\r", end="")
#         time.sleep(1)
#         abc -= 1
#     break

