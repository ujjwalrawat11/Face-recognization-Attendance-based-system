from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import numpy as np




class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")



        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="royalblue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"C:\Users\Dark Demon\Desktop\Face Recognition system\img\developer.png")
        img_top=img_top.resize((1530,750),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=750)


        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1020,y=0,width=500,height=300)

        img_top_1=Image.open(r"C:\Users\Dark Demon\Desktop\Face Recognition system\img\IMG_6324.jpg")
        img_top_1=img_top_1.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top_1=ImageTk.PhotoImage(img_top_1)

        f_lbl=Label(main_frame,image=self.photoimg_top_1)
        f_lbl.place(x=300,y=0,width=200,height=200)

        #developer info

        developer_label=Label(main_frame,text="HELLO,",font=("times new roman",15,"bold"),bg="white")
        developer_label.place(x=0,y=5)

        developer_label=Label(main_frame,text="My Name Is Ujjawal Rawat",font=("times new roman",15,"bold"),bg="white")
        developer_label.place(x=0,y=40)

        developer_label=Label(main_frame,text="Persuing Computer Science",font=("times new roman",15,"bold"),bg="white")
        developer_label.place(x=0,y=80)

        developer_label=Label(main_frame,text="From Graphic Era Hill University",font=("times new roman",15,"bold"),bg="white")
        developer_label.place(x=0,y=120)

        developer_label=Label(main_frame,text="6th Semester",font=("times new roman",15,"bold"),bg="white")
        developer_label.place(x=0,y=160)

        developer_label=Label(main_frame,text="Section - C",font=("times new roman",15,"bold"),bg="white")
        developer_label.place(x=0,y=200)







if __name__== "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()