from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime 
from student import Student
import os
from train import Train
from face_recognition import Face_recognition
from attendance import Attendance
from developer import Developer
from help import HelpDesk



class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #first image
        img=Image.open(r"C:\Users\Dark Demon\Desktop\Face Recognition system\img\gehu-dehradun.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #second image
        img1=Image.open(r"C:\Users\Dark Demon\Desktop\Face Recognition system\img\Facial-Recognition-Technology-in-Attendance-1.png")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #thrid image
        img2=Image.open(r"C:\Users\Dark Demon\Desktop\Face Recognition system\img\1576563781phpQj94TQ.jpeg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)


        

        #background image
        img3=Image.open(r"C:\Users\Dark Demon\Desktop\Face Recognition system\img\gehu-dehradun (1).jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        #----------time---------

        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000,time)
        lbl=Label(bg_img,font=('times new romen',14,'bold'),background="black",foreground='white')
        lbl.place(x=700,y=50,width=120,height=40)
        time()


        #Student button
        img4=Image.open(r"C:\Users\Dark Demon\Desktop\Face Recognition system\img\our-students.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=40,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=40,y=300,width=220,height=40)


        #Detect button
        img5=Image.open(r"C:\Users\Dark Demon\Desktop\Face Recognition system\img\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=300,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=300,y=300,width=220,height=40)

        #Attendance button
        img6=Image.open(r"C:\Users\Dark Demon\Desktop\Face Recognition system\img\attendance.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=1000,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1000,y=300,width=220,height=40)

        #Help Desk button
        img7=Image.open(r"C:\Users\Dark Demon\Desktop\Face Recognition system\img\help-desk-customer-care-icon-260nw-712468252.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1280,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1280,y=300,width=220,height=40)

        #Graphic era Logo
        imglogo=Image.open(r"C:\Users\Dark Demon\Desktop\Face Recognition system\img\unnamed.png")
        imglogo=imglogo.resize((220,220),Image.ANTIALIAS)
        self.photoimglogo=ImageTk.PhotoImage(imglogo)

        f_lbl=Label(bg_img,image=self.photoimglogo)
        f_lbl.place(x=650,y=250,width=220,height=220)


        #Train button
        img8=Image.open(r"C:\Users\Dark Demon\Desktop\Face Recognition system\img\train.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=40,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=40,y=580,width=220,height=40)

        #Photos button
        img9=Image.open(r"C:\Users\Dark Demon\Desktop\Face Recognition system\img\photo.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=300,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Photo",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=300,y=580,width=220,height=40)

        #Developer button
        img10=Image.open(r"C:\Users\Dark Demon\Desktop\Face Recognition system\img\developer.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=1000,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1000,y=580,width=220,height=40)

        #Exit button
        img11=Image.open(r"C:\Users\Dark Demon\Desktop\Face Recognition system\img\flat-exit-web-icon-on-260nw-526360771.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.exit)
        b1.place(x=1280,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.exit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1280,y=580,width=220,height=40)



    def open_img(self):
        os.startfile("data")

    def exit(self):
        self.exit=tkinter.messagebox.askyesno("Face Recognition","Are You Want To Exit This Project.",parent=self.root)
        if self.exit>0:
            self.root.destroy()

        else:
            return




        #---Functions button---

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)


    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)


    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=HelpDesk(self.new_window)




if __name__== "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()