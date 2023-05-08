from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # ======== Variables ========
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_SecurityQ = StringVar()
        self.var_SecurityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()



        # ======== background ========
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\Yanuar\Downloads\Bg.jpg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # ======== left image ========
        self.bg1 = ImageTk.PhotoImage(file=r"C:\Users\Yanuar\Downloads\Bg.jpg")
        bg_lbl = Label(self.root, image=self.bg1)
        bg_lbl.place(x=50, y=100,width=470, height=550)

        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        register_lbl = Label(frame, text = 'REGISTER HERE', font = ('Times New Roman', 20, 'bold'), bg = 'white', fg = 'darkgreen')
        register_lbl.place(x = 20, y = 20)

        # ================= Label and Entry ======================

        # ========== row 1 ==========
        fname = Label(frame, text = 'First Name', font = ('Times New Roman', 15, 'bold'), bg = 'white', fg = 'black')
        fname.place(x=50, y=100)

        self.fname_entry = ttk.Entry(frame, textvariable= self.var_fname,font = ('Times New Roman', 15))
        self.fname_entry.place(x=50, y=130, width=250)

        l_name = Label(frame, text='Last Name', font=('times new roman', 15, 'bold'), bg='white', fg='black')
        l_name.place(x=370, y=100)

        self.txt_lname = ttk.Entry(frame, textvariable= self.var_lname,font=('times new roman', 15))
        self.txt_lname.place(x=370, y=130, width=250)

        # ========== row 2 ==========
        contact = Label(frame, text='Contact No', font=('times new roman', 15, 'bold'), bg='white', fg='black')
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(frame, textvariable= self.var_contact, font=('times new roman', 15))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame, text='Email', font=('times new roman', 15, 'bold'), bg='white', fg='black')
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(frame, textvariable= self.var_email, font = ('times new roman', 15))
        self.txt_email.place(x=370, y=200, width=250)

        # ========== row 3 ==========
        security_Q = Label(frame, text = 'Select Security Questions', font = ('times new roman', 15, 'bold'), bg = 'white', fg = 'black')
        security_Q.place(x = 50, y = 240)

        self.combo_security_Q = ttk.Combobox(frame, textvariable= self.var_SecurityQ, font = ('times new roman', 15), state='readonly')
        self.combo_security_Q['values'] = ('Select','What is your pet name?', 'What is your mother name?', 'What is your father name?')
        self.combo_security_Q.place(x = 50, y = 270, width = 250)
        self.combo_security_Q.current(0)


        security_A = Label(frame, text='Security Answer', font=('times new roman', 15, 'bold'), bg='white', fg='black')
        security_A.place(x=370, y=240)

        self.txt_security = ttk.Entry(frame, textvariable= self.var_SecurityA, font=('times new roman', 15))
        self.txt_security.place(x=370, y=270, width=250)

        # ========== row 4 ==========
        pswd = Label(frame, text='Password', font=('times new roman', 15, 'bold'), bg='white', fg='black')
        pswd.place(x=50, y=310)

        self.txt_pswd = ttk.Entry(frame, textvariable= self.var_pass, font=('times new roman', 15))
        self.txt_pswd.place(x=50, y=340, width=250)

        confirm_pswd = Label(frame, text='Confirm Password', font=('times new roman', 15, 'bold'), bg='white', fg='black')
        confirm_pswd.place(x=370, y=310)

        self.txt_confirm_pswd = ttk.Entry(frame, textvariable= self.var_confpass, font=('times new roman', 15))
        self.txt_confirm_pswd.place(x=370, y=340, width=250)

        # ========== checkbutton ==========
        self.var_check = IntVar()
        checkbtn = Checkbutton(frame, variable= self.var_check, text='I agree to the terms and conditions', font=('times new roman', 12, 'bold'), onvalue = 1, offvalue = 0)
        checkbtn.place(x=50, y=380)

        # ========== button ==========
        img = Image.open(r"C:\Users\Yanuar\Downloads\Register.jpg")
        img = img.resize((200, 50), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame, image=self.photoimage, command=self.register_data, borderwidth=0, cursor='hand2', font= ('Times New Roman', 15, 'bold'),fg='white')
        b1.place(x=40, y=420, width=200)

        img1 = Image.open(r"C:\Users\Yanuar\Downloads\Login.png")
        img1 = img1.resize((200, 50), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, image=self.photoimage1, command=self.reset_login,borderwidth=0, cursor='hand2', font= ('Times New Roman', 15, 'bold'), fg='white')
        b1.place(x=350, y=420, width=200)


    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_SecurityQ.get() == "Select":
            messagebox.showerror("Error", "Please fill all the fields", parent=self.root)
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password and Confirm Password must be same", parent=self.root)
        elif self.var_pass.get() == "" or self.var_confpass.get() == "":
            messagebox.showerror("Error", "Please fill the Password and Confirm Password", parent=self.root)
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree our terms and condition", parent=self.root)
        else:
            conn = mysql.connector.connect(host='localhost', user='root', password='Bobo@ho567', database='mydata')
            my_cursor = conn.cursor()
            query = ("Select * from register where email = %s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "Email already exist, please try another email", parent=self.root)
            else:
                my_cursor.execute("Insert into register values(%s, %s, %s, %s, %s, %s, %s)",(
                                                                                                    self.var_fname.get(),
                                                                                                    self.var_lname.get(),
                                                                                                    self.var_contact.get(),
                                                                                                    self.var_email.get(),
                                                                                                    self.var_SecurityQ.get(),
                                                                                                    self.var_SecurityA.get(),
                                                                                                    self.var_pass.get()
                                                                                                    ))
            conn.commit()
            conn.close()
            if row != None:
                messagebox.showerror("Error", "Email already exist, please try another email", parent=self.root)
            else:
                messagebox.showinfo("Success", "You have successfully registered", parent=self.root)


    def reset_login(self):
        self.root.destroy()











if __name__ == '__main__':
    root = Tk()
    app = Register(root)
    root.mainloop()