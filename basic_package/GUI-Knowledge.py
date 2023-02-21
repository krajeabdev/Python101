from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox
GUI = Tk() # นี่ืคือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') # นี่คือชื่อโปรแกรม
GUI.geometry ('500x400') # นี่คือขนาดโปรแกรม

B1 = ttk.Button(GUI,text='มีเงินอยู่กี่บาท')
B1.pack(ipadx=20,ipady=20)

L1 = Label(GUI,text='โปรแกรมบันทึกความรู้',font=('Angsan New',30),fg='green')
L1.place(x=30,y=20)
#########



def Button2():
    text = 'ตอนนี้มีเงินในบัญชีอยู่ 300 บาท'
    messagebox.showinfo('เงินในบัญชี', text)
                        

FB1 = Frame(GUI) # คล้ายกระดาน
FB1.place(x=100,y=80)
B2 = ttk.Button(FB1,text='มีเงินอยู่กี่บาท',command=Button2)
B2.pack(ipadx=20,ipady=20) 
########

def Button3():
    text = 'Python 101 Math'
    messagebox.showinfo('วิชาเรียนวันที่ 10-20 ก.พ. ง ', text)

FB2 = Frame(GUI) # คล้ายกระดาน
FB2.place(x=100,y=180)
B3 = ttk.Button(FB1,text='สัปดาห์นี้เรียนวิชาอะไร',command=Button3)
B3.pack(ipadx=20,ipady=20) 


GUI.mainloope()
