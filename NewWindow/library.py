from timeit import default_timer as timer
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from PIL import Image, ImageDraw, ImageFont
import mysql.connector
import datetime
import time



class LibraryNode(object):
    def __init__(self, data=None, next_node=None):
        self.Membertipe = data['MemberType']
        self.PRN = data['PRN']
        self.ID = data['ID']
        self.firstnme = data['FirstName']
        self.lastname = data['LastName']
        self.addrs1 = data['Address1']
        self.addrs2 = data['Address2']
        self.postcode = data['PostCode']
        self.mobile = data['Mobile']
        self.BookId = data['BookId']
        self.BookTitle = data['BookTitle']
        self.BookAuthor = data['BookAuthor']
        self.DateBorrow = data['DateBorrow']
        self.DateDue = data['DateDue']
        self.DaysOnBook = data['DaysOnBook']
        self.DateReturn = data['DateReturn']
        self.DateOverDue = data['OverDue']
        self.ActualPrice = data['ActualPrice']
        self.next_node = next_node

class LibraryManagementSystem(object):
    def __init__(self, root, head=None, tail=None):
        global listbox, listBooks, txtFirstName

        self.head = head
        self.tail = tail
        self.MmbrTipe = ""
        self.PrN = ""
        self.Idd = ""
        self.FirstNme = ""
        self.LastNme = ""
        self.Addrs1 = ""
        self.Addrs2 = ""
        self.PostCde = ""
        self.Moble = ""
        self.BookIdd = ""
        self.BookTtle = ""
        self.BookAuth = ""
        self.DateBorrw = ""
        self.DateDuee = ""
        self.DaysOnBok = ""
        self.Daterturn = ""
        self.DateOverD = ""
        self.ActualPric = ""


        self.root = root
        self.root.title("Aplikasi - Any Books")
        self.root.geometry("1550x800+0+0")

        # =========================== Variables ===========================
        self.var_member = StringVar()
        self.var_prn = StringVar()
        self.var_id = StringVar()
        self.var_firstname = StringVar()
        self.var_lastname = StringVar()
        self.var_address1 = StringVar()
        self.var_address2 = StringVar()
        self.var_postcode = StringVar()
        self.var_mobile = StringVar()
        self.var_bookid = StringVar()
        self.var_booktitle = StringVar()
        self.var_author = StringVar()
        self.var_dateborrowed = StringVar()
        self.var_datedue = StringVar()
        self.var_daysonbook = StringVar()
        self.var_lateratefine = StringVar()
        self.var_dateoverdue = StringVar()
        self.var_finalprice = StringVar()
        self.var_Duee = StringVar()
        self.var_DLast = StringVar()




        lbltittle = Label(self.root, text="ANY BOOKS", font=("times new roman", 50, "bold"), bg="grey20", fg="dark orange", bd=20, relief=RIDGE, padx=2, pady=6)
        lbltittle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="grey20")
        frame.place(x=0, y=130, width=1530, height=400)

        # ==========================  Frame Left ==========================
        DataFrameLeft = LabelFrame(frame, text="Library Membership Information", bg="grey50", fg="cyan", font=("times new roman", 12, "bold"), bd=12, relief=RIDGE)
        DataFrameLeft.place(x=0, y=5, width=840, height=350)

        lblMember = Label(DataFrameLeft, text="Member Type", font=("arial", 13, "bold"), bg="grey50", padx=2, pady=6)
        lblMember.grid(row=0, column=0, sticky=W)
        comMember = ttk.Combobox(DataFrameLeft, textvariable=self.var_member, state="readonly", font=("arial", 12, "bold"), width=28)
        comMember["values"] = ("Admin Staff", "Student", "Lecturer")
        comMember.grid(row=0, column=1)

        lblPRN_No = Label(DataFrameLeft, text="PRN No:", font=("arial", 12, "bold"), bg="grey50", padx=2)
        lblPRN_No.grid(row=1, column=0, sticky=W)
        txtPRN_No = Entry(DataFrameLeft, textvariable=self.var_prn, font=("arial", 13, "bold"), width=30)
        txtPRN_No.grid(row=1, column=1)

        lblTitle = Label(DataFrameLeft, text="ID No:", font=("arial", 12, "bold"), bg="grey50", padx=2, pady=4)
        lblTitle.grid(row=2, column=0, sticky=W)
        txtTitle = Entry(DataFrameLeft, textvariable=self.var_id, font=("arial", 13, "bold"), width=30)
        txtTitle.grid(row=2, column=1)

        lblFirstName = Label(DataFrameLeft, text="First Name", font=("arial", 12, "bold"), bg="grey50", padx=2, pady=6)
        lblFirstName.grid(row=3, column=0, sticky=W)
        txtFirstName = Entry(DataFrameLeft, textvariable=self.var_firstname, font=("arial", 13, "bold"), width=30)
        txtFirstName.grid(row=3, column=1)

        lblLastName = Label(DataFrameLeft, text="Last Name", font=("arial", 12, "bold"), bg="grey50", padx=2, pady=6)
        lblLastName.grid(row=4, column=0, sticky=W)
        txtLastName = Entry(DataFrameLeft, textvariable=self.var_lastname, font=("arial", 13, "bold"), width=30)
        txtLastName.grid(row=4, column=1)

        lblAddres1 = Label(DataFrameLeft, text="Address1", font=("arial", 12, "bold"), bg="grey50", padx=2, pady=6)
        lblAddres1.grid(row=5, column=0, sticky=W)
        txtAddres1 = Entry(DataFrameLeft, textvariable=self.var_address1, font=("arial", 13, "bold"), width=30)
        txtAddres1.grid(row=5, column=1)

        lblAddres2 = Label(DataFrameLeft, text="Address2", font=("arial", 12, "bold"), bg="grey50", padx=2, pady=6)
        lblAddres2.grid(row=6, column=0, sticky=W)
        txtAddres2 = Entry(DataFrameLeft, textvariable=self.var_address2, font=("arial", 13, "bold"), width=30)
        txtAddres2.grid(row=6, column=1)

        lblPostCode = Label(DataFrameLeft, text="Post Code", font=("arial", 12, "bold"), bg="grey50", padx=2, pady=4)
        lblPostCode.grid(row=7, column=0, sticky=W)
        txtPostCode = Entry(DataFrameLeft, textvariable=self.var_postcode, font=("arial", 13, "bold"), width=30)
        txtPostCode.grid(row=7, column=1)

        lblMobile = Label(DataFrameLeft, text="Mobile", font=("arial", 12, "bold"), bg="grey50", padx=2, pady=6)
        lblMobile.grid(row=8, column=0, sticky=W)
        txtMobile = Entry(DataFrameLeft, textvariable=self.var_mobile, font=("arial", 13, "bold"), width=30)
        txtMobile.grid(row=8, column=1)

        lblBookId = Label(DataFrameLeft, text="Book ID:", font=("arial", 12, "bold"), bg="grey50", padx=2)
        lblBookId.grid(row=0, column=2, sticky=W)
        txtBookId = Entry(DataFrameLeft, textvariable=self.var_bookid, font=("arial", 13, "bold"), width=30)
        txtBookId.grid(row=0, column=3)

        lblBookTitle = Label(DataFrameLeft, text="Book Title:", font=("arial", 12, "bold"), bg="grey50", padx=2, pady=6)
        lblBookTitle.grid(row=1, column=2, sticky=W)
        txtBookTitle = Entry(DataFrameLeft, textvariable=self.var_booktitle, font=("arial", 13, "bold"), width=30)
        txtBookTitle.grid(row=1, column=3)

        lblAuthor = Label(DataFrameLeft, text="Author Name:", font=("arial", 12, "bold"), bg="grey50", padx=2, pady=6)
        lblAuthor.grid(row=2, column=2, sticky=W)
        txtAuthor = Entry(DataFrameLeft, textvariable=self.var_author, font=("arial", 13, "bold"), width=30)
        txtAuthor.grid(row=2, column=3)

        lblDataBorrowed = Label(DataFrameLeft, text="Date Borrowed:", font=("arial", 12, "bold"), bg="grey50", padx=2, pady=6)
        lblDataBorrowed.grid(row=3, column=2, sticky=W)
        txtDataBorrowed = Entry(DataFrameLeft, textvariable=self.var_dateborrowed, font=("arial", 13, "bold"), width=30)
        txtDataBorrowed.grid(row=3, column=3)

        lblDateDue = Label(DataFrameLeft, text="Date Due:", font=("arial", 12, "bold"), bg="grey50", padx=2, pady=6)
        lblDateDue.grid(row=4, column=2, sticky=W)
        txtDateDue = Entry(DataFrameLeft, textvariable=self.var_datedue, font=("arial", 13, "bold"), width=30)
        txtDateDue.grid(row=4, column=3)

        lblDaysOnBook = Label(DataFrameLeft, text="Days on Book:", font=("arial", 12, "bold"), bg="grey50", padx=2, pady=6)
        lblDaysOnBook.grid(row=5, column=2, sticky=W)
        txtDaysOnBook = Entry(DataFrameLeft, textvariable=self.var_daysonbook, font=("arial", 13, "bold"), width=30)
        txtDaysOnBook.grid(row=5, column=3)

        lblLateReturnFine = Label(DataFrameLeft, text="Late Return Fine:", font=("arial", 12, "bold"), bg="grey50", padx=2, pady=6)
        lblLateReturnFine.grid(row=6, column=2, sticky=W)
        txtLateReturnFine = Entry(DataFrameLeft, textvariable=self.var_lateratefine, font=("arial", 13, "bold"), width=30)
        txtLateReturnFine.grid(row=6, column=3)

        lateDateOverDate = Label(DataFrameLeft, text="Date Over Due:", font=("arial", 12, "bold"), bg="grey50", padx=2, pady=6)
        lateDateOverDate.grid(row=7, column=2, sticky=W)
        txtDateOverDate = Entry(DataFrameLeft, textvariable=self.var_dateoverdue, font=("arial", 13, "bold"), width=30)
        txtDateOverDate.grid(row=7, column=3)

        lblActualPrice = Label(DataFrameLeft, text="Actual Price:", font=("arial", 12, "bold"), bg="grey50", padx=2, pady=6)
        lblActualPrice.grid(row=8, column=2, sticky=W)
        txtActualPrice = Entry(DataFrameLeft, textvariable=self.var_finalprice, font=("arial", 13, "bold"), width=30)
        txtActualPrice.grid(row=8, column=3)



        # ==========================  Frame Right ==========================
        DataFrameRight = LabelFrame(frame, text="Book Details              ", bg="grey50", fg="cyan", font=("times new roman", 12, "bold"), bd=12, relief=RIDGE, padx=5)
        DataFrameRight.place(x=850, y=5, width=610, height=350)

        btnAddData = Button(DataFrameRight, command=self.addBook_Window, text= "+", width= 10, font=("arial", 12, "bold"), bg="red", fg="white")
        btnAddData.place(x= 100, y= -20, width= 30, height= 20)

        btnPrintData = Button(DataFrameRight, command=self.PrintData, text= "Print", width= 10, font=("arial", 12, "bold"), bg="red", fg="white")
        btnPrintData.place(x= 490, y= -20, width= 50, height= 25)

        self.textBox = Text(DataFrameRight, width=32, height=16, padx= 2, pady= 6,font=("arial", 12, "bold"))
        self.textBox.grid(row=0, column=2)

        listScrollbar = Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0, column=1, sticky='ns')

        listBooks = []

        def SelectBook(event=""):
            value = str(self.listBox.get(self.listBox.curselection()))
            conn = mysql.connector.connect(host="localhost", user="root", password="Bobo@ho567", database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from book where BookName = %s", (value,))
            row = my_cursor.fetchall()

            d1 = datetime.date.today()
            d2 = datetime.timedelta(days=15)
            d3 = d1+d2

            self.var_bookid.set(row[0][0])
            self.var_booktitle.set(row[0][1])
            self.var_author.set(row[0][2])
            self.var_finalprice.set(row[0][3])
            self.var_dateborrowed.set(d1)
            self.var_datedue.set(d3)
            self.var_daysonbook.set(15)
            self.var_lateratefine.set("Rp. 30.000")
            self.var_dateoverdue.set("NO")            



        self.listBox = Listbox(DataFrameRight, width=25, height=16, font=("arial", 12, "bold"))
        self.listBox.bind('<<ListboxSelect>>', SelectBook)
        self.listBox.grid(row=0, column=0, padx=4)
        listScrollbar.config(command=self.listBox.yview)

        # for items in listBooks:
        #     self.listBox.insert(END, items)


        # ========================== Button Frame ==========================
        Framebutton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="grey20")
        Framebutton.place(x=0, y=530, width=1530, height=60)

        btnAddData = Button(Framebutton, command=self.add_Linked, text="Add Data", width=23, font=("arial", 12, "bold"), bg="red", fg='white')
        btnAddData.grid(row=0, column=0)
        btnShowData = Button(Framebutton, command=self.showData, text="Show Data", width=23, font=("arial", 12, "bold"), bg="red", fg='white')
        btnShowData.grid(row=0, column=1)
        btnUpdateData = Button(Framebutton, command=self.update_data, text="Update", width=23, font=("arial", 12, "bold"), bg="red", fg='white')
        btnUpdateData.grid(row=0, column=2)
        btnDeleteData = Button(Framebutton, command=self.Delete, text="Delete", width=23, font=("arial", 12, "bold"), bg="red", fg='white')
        btnDeleteData.grid(row=0, column=3)
        btnResetData = Button(Framebutton, command=self.reset, text="Reset", width=23, font=("arial", 12, "bold"), bg="red", fg='white')
        btnResetData.grid(row=0, column=4)
        btnExitData = Button(Framebutton, command=self.Exit, text="Exit", width=23, font=("arial", 12, "bold"), bg="red", fg='white')
        btnExitData.grid(row=0, column=5)

        # btnSearchData = Button(Framebutton, text="S", width=3, font=("arial", 12, "bold"), bg="blue", fg='white')
        # btnSearchData.grid(row=0, column=6)


        # ========================== Informations Frame ==========================
        FrameDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="grey20")
        FrameDetails.place(x=0, y=590, width=1530, height=210)

        Table_frame = Frame(FrameDetails, bd=6, relief=RIDGE, bg="grey20")
        Table_frame.place(x=0, y=2, width=1460, height=190)

        xscroll = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(Table_frame, orient=VERTICAL)
        self.library_table = ttk.Treeview(Table_frame, column= ("MemberType", "PRNO", "Title", "Firstname"
                                                                , "Lastname", "Addres1", "Addres2", "PostID"
                                                                , "Mobile", "BookID", "BookTitle", "Author"
                                                                , "DateBorrowed", "DateDue", "Days", "DaysLeft", "LateReturnFine"
                                                                , "DateOverDue", "FinalPrice"), xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)


        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
        

        self.library_table.heading("MemberType", text="Member Type")
        self.library_table.heading("PRNO", text="PRN No")
        self.library_table.heading("Title", text="Title")
        self.library_table.heading("Firstname", text="First name")
        self.library_table.heading("Lastname", text="Last name")
        self.library_table.heading("Addres1", text="Addres1")
        self.library_table.heading("Addres2", text="Addres2")
        self.library_table.heading("PostID", text="Post ID")
        self.library_table.heading("Mobile", text="Mobile")
        self.library_table.heading("BookID", text="Book ID")
        self.library_table.heading("BookTitle", text="Book Title")
        self.library_table.heading("Author", text="Author")
        self.library_table.heading("DateBorrowed", text="Date Of Borrowed")
        self.library_table.heading("DateDue", text="Date Due")
        self.library_table.heading("Days", text="DaysOnBook")
        self.library_table.heading("DaysLeft", text="Days Left")
        self.library_table.heading("LateReturnFine", text="LateReturnFine")
        self.library_table.heading("DateOverDue", text="DateOverDue")
        self.library_table.heading("FinalPrice", text="Final Price")

        self.library_table['show']='headings'
        self.library_table.pack(fill=BOTH, expand=1)

        self.library_table.column("MemberType", width=100)
        self.library_table.column("PRNO", width=100)
        self.library_table.column("Title", width=100)
        self.library_table.column("Firstname", width=100)
        self.library_table.column("Lastname", width=100)
        self.library_table.column("Addres1", width=100)
        self.library_table.column("Addres2", width=100)
        self.library_table.column("PostID", width=100)
        self.library_table.column("Mobile", width=100)
        self.library_table.column("BookID", width=100)
        self.library_table.column("BookTitle", width=100)
        self.library_table.column("Author", width=100)
        self.library_table.column("DateBorrowed", width=100)
        self.library_table.column("DateDue", width=100)
        self.library_table.column("Days", width=100)
        self.library_table.column("DaysLeft", width=100)
        self.library_table.column("LateReturnFine", width=100)
        self.library_table.column("DateOverDue", width=100)
        self.library_table.column("FinalPrice", width=100)

        
        self.ListBooksSementara()
        self.data_sementara()
        self.library_table.bind("<ButtonRelease-1>", self.get_cursor)
    
    def PrintData(self):
        self.ItemPrint = str(self.textBox.get(index1="1.0", index2="end"))
        self.image = Image.open('LibraryMngmnt\\TemplateData1.png')
        self.draw = ImageDraw.Draw(self.image)
        self.points1 = 20, 40
        self.font1 = ImageFont.truetype("arial.ttf", 18)
        self.draw.text(self.points1, self.ItemPrint, "black", font=self.font1)
        self.image.save(rf'{txtFirstName.get()}.png')
        self.image.show()
    
    def addBook_Window(self):
        self.new_window = Toplevel(self.root)
        self.app = AddBook(self.new_window)

    
    def add_Linked(self):
        self.add_data({
            'MemberType': self.var_member.get(),
            'PRN': self.var_prn.get(),
            'ID': self.var_id.get(),
            'FirstName': self.var_firstname.get(),
            'LastName': self.var_lastname.get(),
            'Address1': self.var_address1.get(),
            'Address2': self.var_address2.get(),
            'PostCode': self.var_postcode.get(),
            'Mobile': self.var_mobile.get(),
            'BookId': self.var_bookid.get(),
            'BookTitle': self.var_booktitle.get(),
            'BookAuthor': self.var_author.get(),
            'DateBorrow': self.var_dateborrowed.get(),
            'DateDue': self.var_datedue.get(),
            'DaysOnBook': self.var_daysonbook.get(),
            'DateReturn': self.var_lateratefine.get(),
            'OverDue': self.var_dateoverdue.get(),
            'ActualPrice': self.var_finalprice.get(),

        })



    def add_data(self, data):
        global d3
        start = timer()
        conn = mysql.connector.connect(host="localhost", user="root", password="Bobo@ho567", database="mydata")
        my_cursor = conn.cursor()
        d1 = datetime.date.today()
        d2 = datetime.timedelta(days= int(self.var_daysonbook.get()))
        d3 = d1+d2
        d4 = d3 - d1
        self.var_datedue.set(d3)
        self.var_Duee = d3
        self.var_DLast = d4.days

        new_node = LibraryNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.MmbrTipe = (new_node.Membertipe)
            self.PrN = (new_node.PRN)
            self.Idd = (new_node.ID)
            self.FirstNme = (new_node.firstnme)
            self.LastNme = (new_node.lastname)
            self.Addrs1 = (new_node.addrs1)
            self.Addrs2 = (new_node.addrs2)
            self.PostCde = (new_node.postcode)
            self.Moble = (new_node.mobile)
            self.BookIdd = (new_node.BookId)
            self.BookTtle = (new_node.BookTitle)
            self.BookAuth = (new_node.BookAuthor)
            self.DateBorrw = (new_node.DateBorrow)
            self.DateDuee = (new_node.DateDue)
            self.DaysOnBok = (new_node.DaysOnBook)
            self.Daterturn = (new_node.DateReturn)
            self.DateOverD = (new_node.DateOverDue)
            self.ActualPric = (new_node.ActualPrice)

        else:
            self.tail.next_node = new_node
            self.tail = new_node
            self.MmbrTipe = (new_node.Membertipe)
            self.PrN = (new_node.PRN)
            self.Idd = (new_node.ID)
            self.FirstNme = (new_node.firstnme)
            self.LastNme = (new_node.lastname)
            self.Addrs1 = (new_node.addrs1)
            self.Addrs2 = (new_node.addrs2)
            self.PostCde = (new_node.postcode)
            self.Moble = (new_node.mobile)
            self.BookIdd = (new_node.BookId)
            self.BookTtle = (new_node.BookTitle)
            self.BookAuth = (new_node.BookAuthor)
            self.DateBorrw = (new_node.DateBorrow)
            self.DateDuee = (new_node.DateDue)
            self.DaysOnBok = (new_node.DaysOnBook)
            self.DateOverD = (new_node.DateOverDue)
            self.ActualPric = (new_node.ActualPrice)



        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                                                                                                                self.MmbrTipe,
                                                                                                                self.PrN,
                                                                                                                self.Idd,
                                                                                                                self.FirstNme,
                                                                                                                self.LastNme,
                                                                                                                self.Addrs1,
                                                                                                                self.Addrs2,
                                                                                                                self.PostCde,
                                                                                                                self.Moble,
                                                                                                                self.BookIdd,
                                                                                                                self.BookTtle,
                                                                                                                self.BookAuth,
                                                                                                                self.DateBorrw,
                                                                                                                self.var_Duee,
                                                                                                                self.DaysOnBok,
                                                                                                                self.var_DLast,
                                                                                                                self.Daterturn,
                                                                                                                self.DateOverD,
                                                                                                                self.ActualPric
                                                                                                            ))

        conn.commit()
        self.data_sementara()
        conn.close()
        messagebox.showinfo("Success", "Data has been added", parent=self.root)
        end = timer()
        print("Waktu yang dibutuhkan untuk menambah data Customer: ", end - start)



    def update_data(self):
        global d3
        conn = mysql.connector.connect(host="localhost", user="root", password="Bobo@ho567", database="mydata")
        my_cursor = conn.cursor()
        d1 = datetime.date.today()
        d2 = datetime.timedelta(days= int(self.var_daysonbook.get()))
        d3 = d1+d2
        d4 = d3 - d1
        self.var_Duee = d3
        self.var_DLast = d4.days
        my_cursor.execute("update library set Member=%s, ID=%s, FirstName=%s, LastName=%s, Address1=%s, Address2=%s, PostID=%s, Mobile=%s, BookID=%s, BookTitle=%s, Author=%s, DateBorrowed=%s, DateDue=%s, DaysOnBook=%s, DaysLeft=%s, LateRateFine=%s, DateOverDue=%s, FinalPrice=%s where PRN_NO=%s", (
                            self.var_member.get(),
                            self.var_id.get(),
                            self.var_firstname.get(),
                            self.var_lastname.get(),
                            self.var_address1.get(),
                            self.var_address2.get(),
                            self.var_postcode.get(),
                            self.var_mobile.get(),
                            self.var_bookid.get(),
                            self.var_booktitle.get(),
                            self.var_author.get(),
                            self.var_dateborrowed.get(),
                            self.var_Duee,
                            self.var_daysonbook.get(),
                            self.var_DLast,
                            self.var_lateratefine.get(),
                            self.var_dateoverdue.get(),
                            self.var_finalprice.get(),
                            self.var_prn.get(),                                                          
                            ))

        conn.commit()
        self.data_sementara()
        self.reset()
        conn.close()
        messagebox.showinfo("Success", "Data has been updated", parent=self.root)


    def data_sementara(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="Bobo@ho567", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from library")
        row = my_cursor.fetchall()

        if len(row) != 0:
            self.library_table.delete(*self.library_table.get_children())
            for i in row:
                self.library_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_now = self.library_table.focus()
        content = self.library_table.item(cursor_now)
        row = content['values']

        self.var_member.set(row[0])
        self.var_prn.set(row[1])
        self.var_id.set(row[2])
        self.var_firstname.set(row[3])
        self.var_lastname.set(row[4])
        self.var_address1.set(row[5])
        self.var_address2.set(row[6])
        self.var_postcode.set(row[7])
        self.var_mobile.set(row[8])
        self.var_bookid.set(row[9])
        self.var_booktitle.set(row[10])
        self.var_author.set(row[11])
        self.var_dateborrowed.set(row[12])
        self.var_datedue.set(row[13])
        self.var_daysonbook.set(row[14])
        # self.var_DLast.set(row[15])
        self.var_lateratefine.set(row[16])
        self.var_dateoverdue.set(row[17])
        self.var_finalprice.set(row[18])

    def showData(self):
        self.textBox.insert(END, "Member Type:      " + self.var_member.get() + "\n")
        self.textBox.insert(END, "PRN No:                " + self.var_prn.get() + "\n")
        self.textBox.insert(END, "ID No:                     " + self.var_id.get() + "\n")
        self.textBox.insert(END, "First Name:           " + self.var_firstname.get() + "\n")
        self.textBox.insert(END, "Last Name:           " + self.var_lastname.get() + "\n")
        self.textBox.insert(END, "Address 1:            " + self.var_address1.get() + "\n")
        self.textBox.insert(END, "Address 2:            " + self.var_address2.get() + "\n")
        self.textBox.insert(END, "Post Code:           " + self.var_postcode.get() + "\n")
        self.textBox.insert(END, "Mobile No:            " + self.var_mobile.get() + "\n")
        self.textBox.insert(END, "Book ID:                " + self.var_bookid.get() + "\n")
        self.textBox.insert(END, "Book Title:            " + self.var_booktitle.get() + "\n")
        self.textBox.insert(END, "Author:                  " + self.var_author.get() + "\n")
        self.textBox.insert(END, "Date Borrowed:  " + self.var_dateborrowed.get() + "\n")
        self.textBox.insert(END, "Date Due:             " + self.var_datedue.get() + "\n")
        self.textBox.insert(END, "DaysOnBook:     " + self.var_daysonbook.get() + "\n")
        self.textBox.insert(END, "LateRateFine:     " + self.var_lateratefine.get() + "\n")
        self.textBox.insert(END, "DateOverDue:     " + self.var_dateoverdue.get() + "\n")
        self.textBox.insert(END, "FinallPrice:          " + self.var_finalprice.get() + "\n")


    def reset(self):
        self.var_member.set("")
        self.var_prn.set("")
        self.var_id.set("")
        self.var_firstname.set("")
        self.var_lastname.set("")
        self.var_address1.set("")
        self.var_address2.set("")
        self.var_postcode.set("")
        self.var_mobile.set("")
        self.var_bookid.set("")
        self.var_booktitle.set("")
        self.var_author.set("")
        self.var_dateborrowed.set("")
        self.var_datedue.set("")
        self.var_daysonbook.set("")
        self.var_lateratefine.set("")
        self.var_dateoverdue.set("")
        self.var_finalprice.set("")
        self.textBox.delete("1.0", END)

    def Exit(self):
        Exit = messagebox.askyesno("Library Management System", "Do you want to exit?", parent=self.root)
        if Exit > 0:
            self.root.destroy()
            return
        

    def Delete(self):
        if self.var_prn.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "Please select the Member", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Bobo@ho567", database="mydata")
            my_cursor = conn.cursor()
            query = "delete from library where PRN_NO = %s"
            value = (self.var_prn.get(),)
            my_cursor.execute(query, value)

            conn.commit()
            self.data_sementara()
            self.reset()
            conn.close()

            messagebox.showinfo("Success", "Member has been deleted", parent=self.root)

    def ListBooksSementara(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="Bobo@ho567", database="mydata")
        my_cursor = conn.cursor()
        query = "select BookName from book"
        my_cursor.execute(query)
        result = my_cursor.fetchall()
        
        self.listBox.delete(0, END)

        for ItemPrint in result:
            Item = str(ItemPrint)
            self.listBox.insert(END, Item[2:-3])
        conn.commit()
        conn.close()

    def Update_DaysLeft(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="Bobo@ho567", database="mydata")
        my_cursor = conn.cursor()
        d3 = self.var_datedue.get()
        d4 = datetime.date.today()
        d5 = d3 - d4
        self.var_DaysLeft = d5.days

        my_cursor.execute("update library set DaysLeft = %s where PRN_NO = %s", (
                                self.var_DaysLeft, 
                                self.var_prn.get()
                                ))

        conn.commit()
        conn.close()


class BookNode(object):
    def __init__(self, data=None, next_node=None):
        self.Bukidd = data['BookID']
        self.BukName = data['BookName']
        self.Athorname = data['AuthorName']
        self.ActPric = data['ActualPrice']
        self.next_node = next_node    


class AddBook(object):
    def __init__(self, root, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.Bukid = ""
        self.Bukname = ""
        self.Authname = ""
        self.Actlpric = ""

        self.root = root
        self.root.geometry('500x300')
        self.root.resizable(0,0)
        self.root.title("Add Book")
        self.root.configure(background='grey50')


        self.var_BookID = StringVar()
        self.var_BookName = StringVar()
        self.var_AuthorName = StringVar()
        self.var_ActualPrice = StringVar()


        BookID = Label(root, text = 'Book ID', font = ('Times New Roman', 15, 'bold'), bg = 'grey50', fg = 'black')
        BookID.place(x=50, y=50)

        self.BookID_entry = Entry(root, textvariable=self.var_BookID, font = ('Times New Roman', 15))
        self.BookID_entry.place(x=230, y=50, width=200)

        BookName = Label(root, text = 'Book Name', font = ('Times New Roman', 15, 'bold'), bg = 'grey50', fg = 'black')
        BookName.place(x=50, y=100)

        self.BookName_entry = Entry(root, textvariable=self.var_BookName, font = ('Times New Roman', 15))
        self.BookName_entry.place(x=230, y=100, width=200)

        AuthorName = Label(root, text = 'Author Name', font = ('Times New Roman', 15, 'bold'), bg = 'grey50', fg = 'black')
        AuthorName.place(x=50, y=150)

        self.AuthorName_entry = Entry(root, textvariable=self.var_AuthorName, font = ('Times New Roman', 15))
        self.AuthorName_entry.place(x=230, y=150, width=200)

        ActualPrice = Label(root, text = 'Actual Price', font = ('Times New Roman', 15, 'bold'), bg = 'grey50', fg = 'black')
        ActualPrice.place(x=50, y=200)

        self.ActualPrice_entry = Entry(root, textvariable=self.var_ActualPrice, font = ('Times New Roman', 15))
        self.ActualPrice_entry.place(x=230, y=200, width=200)

        Cancelbtn = Button(root, command=self.Exit, text = 'Cancel', font = ('Times New Roman', 12, 'bold'), bg = 'red', fg = 'white')
        Cancelbtn.place(x=250, y=250, width=70, height=30)        

        Addbtn = Button(root, command=self.AddBook_Linked, text = 'Add', font = ('Times New Roman', 12, 'bold'), bg = 'red', fg = 'white')
        Addbtn.place(x=350, y=250, width=60, height=30)
        
    def Exit(self):
        self.root.destroy()

    def AddBook_Linked(self):
        self.Addbook({
            'BookID': self.var_BookID.get(),
            'BookName': self.var_BookName.get(),
            'AuthorName': self.var_AuthorName.get(),
            'ActualPrice': self.var_ActualPrice.get()
        })

    def Addbook(self, data):
        start = timer()
        variable = LibraryManagementSystem(root)
        conn = mysql.connector.connect(host="localhost", user="root", password="Bobo@ho567", database="mydata")
        my_cursor = conn.cursor()

        new_node = BookNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.Bukid = (new_node.Bukidd)
            self.Bukname = (new_node.BukName)
            self.Authname = (new_node.Athorname)
            self.Actlpric = (new_node.ActPric)

        else:
            self.tail.next_node = new_node
            self.tail = new_node
            self.Bukid = (new_node.Bukidd)
            self.Bukname = (new_node.BukName)
            self.Authname = (new_node.Athorname)
            self.Actlpric = (new_node.ActPric)


        query = "insert into book values(%s, %s, %s, %s)"
        value = (self.Bukid, self.Bukname, self.Authname, self.Actlpric)
        my_cursor.execute(query, value)

        conn.commit()
        variable.ListBooksSementara()
        conn.close()

        messagebox.showinfo("Success", "Book has been added", parent=self.root)
        end = timer()
        print("Waktu yang dibutuhkan untuk menambah data Buku: ", end - start)
        self.root.destroy()
    
        
    




if __name__ == '__main__':
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()