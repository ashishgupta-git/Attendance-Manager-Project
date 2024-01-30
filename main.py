from cProfile import label
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from time import*
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


from pyautogui import *
from pywhatkit import *

class WhatsApp:
    def __init__(self,root):
        self.root=root
        self.root.title("Unlimited WhatsApp Message")
        self.root.geometry("520x880+0+0")

        self.mobile=StringVar()
        self.message=StringVar()
        self.times=IntVar()
        

        img=Image.open("grey2.jpg")
        img=img.resize((1920,1080))
        self.photoimg=ImageTk.PhotoImage(img)
        lbl_img=Label(self.root,image=self.photoimg,borderwidth=0,bg="black")
        lbl_img.place(x=0,y=0,width=1920,height=1080)


        frame=Frame(lbl_img,bg="darkslategrey")
        frame.place(x=10,y=170,height=250,width=255)

        lblheader=Label(self.root,text="UNLIMITED WHATSAPP MESSEGE",bg="steelblue",fg="white",font=('times new roman',11,'bold'))
        lblheader.place(x=10,y=100,width=255,height=70)

        lbl1=Label(frame,text="Enter mobile number : ",bg="darkslategrey",fg="white",font=('times new roman',11))
        lbl1.grid(row=0,column=0,padx=0,pady=10,sticky=W)
        entry1=ttk.Entry(frame, textvariable=self.mobile,font=('times new roman',11,'bold'),width=11)
        entry1.grid(row=0,column=1,pady=10,sticky=W)

        lbl2=Label(frame,text="Enter Message for send : ",bg="darkslategrey",fg="white",font=('times new roman',11))
        lbl2.grid(row=1,column=0,padx=0,pady=10,sticky=W)
        entry2=ttk.Entry(frame, textvariable=self.message,font=('times new roman',11,'bold'),width=11)
        entry2.grid(row=1,column=1,pady=10,sticky=W)

        lbl3=Label(frame,text="How many times send : ",bg="darkslategrey",fg="white",font=('times new roman',11))
        lbl3.grid(row=2,column=0,padx=0,pady=10,sticky=W)
        entry3=ttk.Entry(frame, textvariable=self.times,font=('times new roman',11,'bold'),width=11)
        entry3.grid(row=2,column=1,pady=10,sticky=W)


        btn=Button(frame,text="Submit",command=self.send,font=('times new roman',15,'bold'),bd=10,fg="white",bg="blue",cursor="hand2")
        btn.grid(row=3,columnspan=2,pady=10)


        lab_pk=Label(self.root,text="Created By- Ashish Gupta",fg="white",bg="steelblue",font=('times new roman',15,'bold')).place(y=390,x=9,width=255)

        # print(self.times.get())
         
       

    def send(self):
        h=int(time.strftime("%H"))
        m=int(time.strftime("%M"))
    
        if len(self.mobile.get())!=10:
            messagebox.showerror("Error","Please Enter 10 Digit Number",parent=self.root)
            return
        elif self.message.get()=="":
            messagebox.showerror("Error","Please Enter Your message",parent=self.root)
            return
        elif self.times.get()==0:
            messagebox.showerror("Error","Please Enter How many times send message",parent=self.root)
        else:
            x=messagebox.askyesno("Sure","Are you sure for send message")
        if x==True:
            try:
                sendwhatmsg(f'+91 {self.mobile.get()}',self.message.get(),h,(m+1))


                for i in range(self.times.get()-1):
                    typewrite(self.message.get())
                    press('enter')
            except Exception as es:
                messagebox.showerror('Error',f'Due To : {str(es)}',parent=self.root)
        else:
            return
        


if __name__=="__main__":
    root=Tk()
    obj=WhatsApp(root)
    root.mainloop()
    WhatsApp().run()



