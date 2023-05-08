from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import datetime

from NewWindow import LibraryManagementSystem
# from Kriptografi import kriptografii
from NewWindow import Register


def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()



class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg = ImageTk.PhotoImage(file=r"C:\Users\Yanuar\Downloads\Bg.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        img1 = Image.open(r"C:\Users\Yanuar\Downloads\LogoLoginApp3.png")
        img1 = img1.resize((100, 100), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=730, y=175, width=100, height=100)

        get_str = Label(frame, text= "Get Started", font=('Times New Roman',20,'bold'), bg="black", fg="white")
        get_str.place(x=95, y=100)

        # Username
        username = Label(frame, text="Username", font=('Times New Roman',15,'bold'), bg="black", fg="white")
        username.place(x=70, y=155)
        self.txtuser = ttk.Entry(frame, font=('Times New Roman',15,'bold'))
        self.txtuser.place(x=40, y=180, width=270)

        # Password
        password = lbl = Label(frame, text="Password", font=('Times New Roman',15,'bold'), bg="black", fg="white")
        password.place(x=70, y=225)
        self.txtpass = ttk.Entry(frame, font=('Times New Roman',15,'bold'), show="*")
        self.txtpass.place(x=40, y=250, width=270)

        img2 = Image.open(r"C:\Users\Yanuar\Downloads\LogoLoginApp3.png")
        img2 = img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg1 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        lblimg1.place(x=650, y=323, width=25, height=25)

        img3 = Image.open(r"C:\Users\Yanuar\Downloads\2341515.png")
        img3 = img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg1 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        lblimg1.place(x=650, y=395, width=25, height=25)

        loginbtn = Button(frame,command=self.Login, text="Login", font=('Times New Roman',15,'bold'), bg="red", fg="white", bd=3, relief=RIDGE, activeforeground="white", activebackground="red")
        loginbtn.place(x=110, y=300, width=120, height=35)

        registerbtn = Button(frame, text="Register", command=self.register_window,font=('Times New Roman',10,'bold'), bg="black", fg="white",borderwidth=0, activeforeground="white", activebackground="black")
        registerbtn.place(x=-10, y=350, width=160)

        forgetbtn = Button(frame, text="Forget Password ?",command=self.forgot_password_window, font=('Times New Roman',10,'bold'), bg="black", fg="white",borderwidth=0, activeforeground="white", activebackground="black")
        forgetbtn.place(x=15, y=370, width=160)

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def Login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "Silahkan isi terlebih dahulu")
        elif self.txtuser.get() == 'admin' and self.txtpass.get() == 'asd':
            messagebox.showinfo("Login", "Login Berhasil")
            self.new_window = Toplevel(self.root)
            self.app = LibraryManagementSystem(self.new_window)
        else:
            conn = mysql.connector.connect(host='localhost', user='root', password='Bobo@ho567', database='mydata')
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email = %s and password = %s", (
                                                                                            self.txtuser.get(),
                                                                                             self.txtpass.get()
                                                                                            ))
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid Username & Password")
            else:
                open_main = messagebox.askyesno("YesNo", "Acces only admin")
                if open_main > 0:
                    self.new_window = Toplevel(self.root)
                    self.app = LibraryManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
            # self.root.destroy()


    def reset_password(self):
        if self.combo_security_Q.get() == "Select":
            messagebox.showerror("Error", "Silahkan pilih pertanyaan", parent = self.root2)
        elif self.txt_security.get() == "":
            messagebox.showerror("Error", "Silahkan isi pertanyaan", parent = self.root2)
        elif self.txt_newpass.get() == "":
            messagebox.showerror("Error", "Silahkan isi password baru", parent = self.root2)
        else:
            conn = mysql.connector.connect(host='localhost', user='root', password='Bobo@ho567', database='mydata')
            my_cursor = conn.cursor()
            qury = ("select * from register where email = %s and securityQ = %s and securityA = %s")
            vlaue = (self.txtuser.get(), self.combo_security_Q.get(), self.txt_security.get(),)
            my_cursor.execute(qury, vlaue)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Please enter the correct answer", parent = self.root2)
            else:
                query = ("update register set password = %s where email = %s")
                value = (self.txt_newpass.get(), self.txtuser.get())
                my_cursor.execute(query, value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info", "Your Password has been reset, please login new password", parent = self.root2)
                self.root2.destroy()




    def forgot_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Silahkan isi Username terlebih dahulu")
        else:
            conn = mysql.connector.connect(host='localhost', user='root', password='Bobo@ho567', database='mydata')
            my_cursor = conn.cursor()
            query = ("select * from register where email = %s")
            value = (self.txtuser.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror("Error", "Invalid Username")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")
                self.root2.configure(bg="black")  

                l = Label(self.root2, text="Forgot Password", font=('Times New Roman',20,'bold'), bg="black", fg="white")
                l.place(x=0, y=10, relwidth=1)

                security_Q = Label(self.root2, text = 'Select Security Questions', font = ('times new roman', 15, 'bold'), bg = 'black', fg = 'white')
                security_Q.place(x = 50, y = 80)

                self.combo_security_Q = ttk.Combobox(self.root2, font = ('times new roman', 15), state='readonly')
                self.combo_security_Q['values'] = ('Select','What is your pet name?', 'What is your mother name?', 'What is your father name?')
                self.combo_security_Q.place(x = 50, y = 110, width = 250)
                self.combo_security_Q.current(0)


                security_A = Label(self.root2, text='Security Answer', font=('times new roman', 15, 'bold'), bg='black', fg='white')
                security_A.place(x=50, y=150)

                self.txt_security = ttk.Entry(self.root2, font=('times new roman', 15, 'bold'))
                self.txt_security.place(x=50, y=180, width=250)

                new_password = Label(self.root2, text='New Password', font=('times new roman', 15, 'bold'), bg='black', fg='white')
                new_password.place(x=50, y=220)

                self.txt_newpass = ttk.Entry(self.root2, font=('times new roman', 15, 'bold'))
                self.txt_newpass.place(x=50, y=250, width=250)

                btn = Button(self.root2, text='Reset', command=self.reset_password ,font=('times new roman', 15, 'bold'), bg='red', fg='white')
                btn.place(x=50, y=290)









if __name__ == "__main__":
    main()