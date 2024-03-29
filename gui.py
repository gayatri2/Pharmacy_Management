from tkinter import *

import pymysql

conn = pymysql.connect(host='localhost', database='d1', user='root', password='amazing')
cursor = conn.cursor()


class MyLogin:
    def __init__(self, root):
        self.f = Frame(root, height=350, width=500)
        self.f.propagate(0)
        self.f.pack()
        self.message1 = Message(root, text='Note : All the entries are case sensitive!')
        self.message1.place(x=5, y=100)
        self.b1 = Button(root, text='Existing User', command=self.buttonclickeu)
        self.b1.place(x=20, y=50)
        self.b2 = Button(root, text='New User', command=self.buttonclicknu)
        self.b2.place(x=100, y=50)

    def buttonclickeu(self):
        self.l1 = Label(self.f, text='Enter Username:')
        self.l1.place(x=200, y=100)
        self.e1 = Entry(self.f, width=25)
        self.e1.place(x=200, y=150)
        self.l2 = Label(self.f, text='Enter Password:')
        self.l2.place(x=200, y=180)
        self.e2 = Entry(self.f, width=25, show='*')
        self.e2.place(x=200, y=200)
        self.e2.bind("<Return>", self.displayeu)

    def displayeu(self, event):
        username = self.e1.get()
        password = self.e2.get()

        self.verify(username, password)

    def verify(self, username, password):
        cursor.execute("select*from login")
        rows = cursor.fetchall()
        flag = 0
        for row in rows:
            if username in row[0] and password in row[1]:
                flag = 1
                break
        if flag == 1:
            self.m1 = Message(self.f, text='Login Successful!', width=400)
            self.m1.pack()
            self.b1 = Button(root, text='Medicine details', command=self.secwin)
            self.b1.place(x=200, y=300)
            self.b2 = Button(root, text='Patient details', command=self.patdet)
            self.b2.place(x=350, y=300)
        else:
            self.m1 = Message(self.f, text='Oops!Username or password is incorrect!', width=400)
            self.m1.pack()

    def secwin(self):
        window = Tk()
        window.title('Medicine details')
        window.geometry('250x200')
        self.lbl1 = Label(window, text='Search for medicines:').pack()
        self.lbl = Label(window, text='Search by:')
        self.lbl.pack()
        self.lb = Listbox(window, height=7, width=24, selectmode=SINGLE)
        self.lb.pack()

        for i in ['Sno', 'Name', 'MedCode', 'Category']:
            self.lb.insert(END, i)
        self.lb.bind('<<ListboxSelect>>', self.onselect)

    def onselect(self, event):
        # self.lst = []
        window = Tk()
        window.geometry('150x150')
        self.f = Frame(window, height=350, width=600)
        self.f.propagate(0)
        self.f.pack()
        index = self.lb.curselection()
        if 0 in index:
            self.winmedsno()
        if 1 in index:
            self.winmedname()
        if 2 in index:
            self.winmedcode()
        if 3 in index:
            self.winmedcat()

    def winmedsno(self):
        self.l1 = Label(self.f, text="Enter the medicine Sno to be searched for:")
        self.l1.place(x=50, y=50)
        self.e1 = Entry(self.f, width=15)
        self.e1.place(x=50, y=75)
        self.e1.bind("<Return>", self.dispmedsno)

    def winmedname(self):
        self.l2 = Label(self.f, text="Enter the medicine Name to be searched for:")
        self.l2.place(x=50, y=50)
        self.e2 = Entry(self.f, width=15)
        self.e2.place(x=50, y=75)
        self.e2.bind("<Return>", self.dispmedname)

    def winmedcode(self):
        self.l3 = Label(self.f, text="Enter the medicine code to be searched for:")
        self.l3.place(x=50, y=50)
        self.e3 = Entry(self.f, width=15)
        self.e3.place(x=50, y=75)
        self.e3.bind("<Return>", self.dispmedcode)

    def winmedcat(self):
        self.l4 = Label(self.f, text="Enter the medicine category to be searched for:")
        self.l4.place(x=50, y=50)
        self.e4 = Entry(self.f, width=15)
        self.e4.place(x=50, y=75)
        self.e4.bind("<Return>", self.dispmedcat)

    def dispmedcode(self, event):
        str2 = self.e3.get()
        self.lbl4 = Label(text='You entered:' + str2).place(x=50, y=200)
        self.medcode(str2)

    def dispmedcat(self, event):
        str3 = self.e4.get()
        self.lbl3 = Label(text='You entered:' + str3).place(x=50, y=200)
        self.medcat(str3)

    def medcode(self, MedCode):
        cursor.execute("select* from medicines")
        str = "select * from medicines where MedCode = '%s'"
        args = (MedCode)
        cursor.execute(str % args)
        row = cursor.fetchall()
        if row is not None:
            sw1 = Tk()
            sw1.geometry('200x200')
            lbl4 = Label(sw1, text=row).place(x=50, y=50)
        cursor.close()
        conn.close()

    def medcat(self, Category):
        cursor.execute("select* from medicines")
        str = "select * from medicines where Category = '%s'"
        args = (Category)
        cursor.execute(str % args)
        row = cursor.fetchall()
        if row is not None:
            sw1 = Tk()
            sw1.geometry('200x200')
            lbl4 = Label(sw1, text=row).place(x=50, y=50)
        cursor.close()
        conn.close()

    def medname(self, Name):
        cursor.execute("select* from medicines")
        str = "select * from medicines where Name = '%s'"
        args = (Name)
        cursor.execute(str % args)
        row = cursor.fetchall()
        if row is not None:
            sw1 = Tk()
            sw1.geometry('200x200')
            lbl4 = Label(sw1, text=row).place(x=50, y=50)

        cursor.close()
        conn.close()

    def dispmedname(self, event):
        str1 = self.e2.get()
        self.lbl3 = Label(text='You entered:' + str1).place(x=50, y=200)
        self.medname(str1)

    def medsno(self, Sno):
        window = Tk()
        window.geometry('200x200')
        cursor.execute("select* from medicines")
        str = "select * from medicines where Sno = '%s'"
        args = (Sno)
        cursor.execute(str % args)
        row = cursor.fetchone()
        if row is not None:
            sw1 = Tk()
            sw1.geometry('200x200')
            lbl4 = Label(sw1, text=row).place(x=50, y=50)
        else:
            lb = Label(window, text='Sno not found!').place(x=50, y=50)
        cursor.close()
        conn.close()

    def dispmedsno(self, event):
        str = self.e1.get()
        self.lbl3 = Label(text='You entered:' + str).place(x=50, y=200)
        self.medsno(int(str))

    def buttonclicknu(self):
        self.m1 = Message(self.f, text='Welcome! ', width=400)
        self.m1.pack()
        self.b1 = Button(root, text='Temporary Login', command=self.reg)
        self.b1.place(x=200, y=50)
        self.b1 = Button(root, text='Quit', command=self.closewindow)
        self.b1.place(x=200, y=90)

    def reg(self):
        self.l1 = Label(self.f, text='Enter a username:')
        self.l1.place(x=50, y=200)
        self.e1 = Entry(self.f, width=25)
        self.e1.place(x=180, y=200)
        self.e1.bind("<Return>", self.displaynu)

    def displaynu(self, event):
        userreg = self.e1.get()
        self.check(userreg)

    def check(self, userreg):
        cursor.execute("select*from login")
        rows = cursor.fetchall()
        flag = 0
        for row in rows:
            if userreg in row[0]:
                flag = 1
                break
        if flag == 1:
            self.m1 = Message(self.f, text='Username already taken!', width=400)
            self.m1.pack()

        else:
            self.m2 = Message(self.f, text='Username available!', width=400)
            self.m2.pack()
            self.l1 = Label(self.f, text=' Enter code:')
            self.l1.place(x=50, y=250)
            self.e1 = Entry(self.f, width=25)
            self.e1.place(x=180, y=250)

            self.e1.bind("<Return>", self.display1)

    def display1(self, event):

        p1 = self.e1.get()
        self.tempcheck(p1)

    def tempcheck(self, p1):
        f = open('pw.txt', 'r')
        flag = 0
        for word in f:
            if p1 in word:
                flag = 1
                break
        if flag == 0:
            self.m = Message(self.f, text='Oops!Temorary Login unsuccessful!', width=400)
            self.m.place(x=180, y=300)
        else:
            self.m1 = Message(self.f, text='Temporary login successful!', width=400)
            self.m1.place(x=180, y=290)
            self.b4 = Button(root, text='Patient Details', command=self.patdet).place(x=350, y=300)

    def patdet(self):
        window = Tk()
        window.geometry('200x200')
        self.bu1 = Button(window, text='Existing', command=self.showpatdet).place(x=20, y=20)
        self.bu2 = Button(window, text='New').place(x=100, y=20)

    def showpatdet(self):
        window = Tk()
        window.geometry('500x500')
        self.l1 = Label(window, text='Enter Patient ID :')
        self.l1.place(x=200, y=100)
        self.e1 = Entry(window, width=25)
        self.e1.place(x=200, y=150)
        self.l2 = Label(window, text='Enter First Name:')
        self.l2.place(x=200, y=180)
        self.e6 = Entry(window, width=25)
        self.e6.place(x=200, y=200)
        self.e6.bind("<Return>", self.displaypatdet)

    def displaypatdet(self, event):
        pid = self.e1.get()
        pfn = self.e6.get()

        self.verifypat(pid, pfn)

    def verifypat(self, pid, pfn):
        window = Tk()
        window.geometry('600x600')
        cursor.execute("select*from patients")
        rows = cursor.fetchall()
        flag = 1
        for row in rows:
            if pid in row[1] and pfn in row[2]:
                flag = 0
                break
        if flag == 1:

            self.m1 = Message(window, text='Oops!Patient details not found!', width=400)
            self.m1.pack()
        else:
            self.m1 = Message(window, text='Patient details found!', width=400)
            self.m1.pack()
            self.l1 = Label(window, text='Medicine Name :').place(x=200, y=100)
            self.e1 = Entry(window, width=25)
            self.e1.place(x=200, y=150)
            self.l2 = Label(window, text='Dose :').place(x=400, y=100)
            self.e2 = Entry(window, width=25)
            self.e2.place(x=400, y=150)
            self.e2.bind("<Return>", self.display2)

    def display2(self, event):

        searchmedname = self.e1.get()
        searchdose = self.e2.get()
        self.verifymed(searchmedname, searchdose)

    def verifymed(self, searchmedname, searchdose):
        window = Tk()
        window.geometry('200x200')
        cursor.execute("select*from medicines")
        rows = cursor.fetchall()
        flag = 0
        for row in rows:
            if searchmedname in row[1] and searchdose in row[3]:
                flag = 1
                break
        if flag == 1:
            self.m1 = Message(window, text='Medicine available!', width=400)
            self.m1.pack()
        else:
            self.m2 = Message(window, text='Medicine not available!', width=400)
            self.m2.pack()

    def closewindow(self):
        root.destroy()
        exit()


root = Tk()
ml = MyLogin(root)
root.title("Login")
root.mainloop()