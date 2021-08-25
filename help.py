from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os           #for access the folder
import numpy as np
from time import strftime
from datetime import datetime
import csv
from tkinter import filedialog


class HelpDesk:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")



        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"C:\Users\Dark Demon\Desktop\Face Recognition system\img\IT-help-desk-adobe.jpg")
        img_top=img_top.resize((1530,750),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=750)

        developer_label=Label(f_lbl,text="Contact Us With Given Below Platform",font=("times new roman",40,"bold"),bg="white",fg="royalblue")
        developer_label.place(x=350,y=100)

        developer_label=Label(f_lbl,text="Email ID ",font=("times new roman",40,"bold"),bg="white",fg="royalblue")
        developer_label.place(x=600,y=200)

        developer_label=Label(f_lbl,text="ujjwalrawat2000@gmail.com",font=("times new roman",40,"bold"),bg="white",fg="royalblue")
        developer_label.place(x=400,y=300)

        developer_label=Label(f_lbl,text="Contact Through Instagram",font=("times new roman",40,"bold"),bg="white",fg="royalblue")
        developer_label.place(x=400,y=400)

        developer_label=Label(f_lbl,text="Insta ID-> @_rawat_ujjawal_",font=("times new roman",40,"bold"),bg="white",fg="royalblue")
        developer_label.place(x=400,y=500)




if __name__== "__main__":
    root=Tk()
    obj=HelpDesk(root)
    root.mainloop()