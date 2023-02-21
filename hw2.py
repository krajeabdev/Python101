from tkinter import *
from tkinter import ttk #them of tk
from tkinter import messagebox

GUI = Tk() #นี่คือหน้าจอหลักของโปรแกรม
GUI.title('คำนวณ BMI') #นี่คือชื่อโปรแกรม
GUI.geometry('500x400') #นี่คือขนาดโปรแกรม

L1= Label(GUI,text='คำนวณ BMI',font=('Angsana New',30),fg='blue')
L1.place(x=30,y=20)
##########
txtw = Label(GUI,text='น้ำหนัก (กิโลกรัม)',font=('Angsana New',20),fg='blue')
txtw.place(x=30,y=100)             
w   = Entry(GUI,bg='white',fg='red')
w.place(x=200,y=110)
w.focus()

txth = Label(GUI,text='ส่วนสูง (เซนติเมตร)',font=('Angsana New',20),fg='blue')
txth.place(x=30,y=150)             
h   = Entry(GUI,bg='white',fg='red')
h.place(x=200,y=160)

def ButtonCal():
    wval = float(w.get())
    hval = float(h.get())
    bmi  = str(round(wval/(hval/100)**2,2))
    messagebox.showinfo('Your BMI ' , bmi )
                        
    

FB1 = Frame(GUI)
FB1.place(x=200,y=200)
BCal = ttk.Button(FB1,text='คำนวณ',command=ButtonCal)
BCal.pack(ipadx=20, ipady=20)
