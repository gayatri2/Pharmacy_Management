'''from tkinter import*
import MySQLdb
root=Tk()
def retrieve_rows(Sno):
    conn = MySQLdb.connect(host='localhost', database='d1', user='root', password='amazing')
    cursor = conn.cursor()
    str = "select *  from medicines where Sno = '%d'"
    args = (Sno)
    cursor.execute(str % args)
    print(Sno)
    row=cursor.fetchone()
    if row is not None:
        lbl=Label(text=row).place(x=50, y=200)
    #cursor.close()
    #conn.close()
def display(self):
    str=e1.get()
    lbl = Label(text='You entered:' +str).place(x=50, y=150)
    retrieve_rows(int(str))
f=Frame(root,height=350,width=600)
f.propagate(0)
f.pack()
l1=Label(text='Enter med no to be searched:')
e1=Entry(f, width=15)
e1.bind("<Return>", display)
l1.place(x=50, y=100)
e1.place(x=300, y=100)
root.mainloop()'''


