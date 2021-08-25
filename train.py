from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os           #for access the folder
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        
        
        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"C:\Users\Dark Demon\Desktop\Face Recognition system\img\facialrecognition.png")
        img_top=img_top.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=325)

        #----button-----
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=550,y=380,width=400,height=60)

        title_lbl=Label(self.root,text="CLICK ON ABOVE  BUTTON",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=400,y=430,width=700,height=45)

        #---left arrow---
        img_left_arrow=Image.open(r"C:\Users\Dark Demon\Desktop\Face Recognition system\img\left.jpg")
        img_left_arrow=img_left_arrow.resize((200,100),Image.ANTIALIAS)
        self.photoimg_left_arrow=ImageTk.PhotoImage(img_left_arrow)

        f_lbl=Label(self.root,image=self.photoimg_left_arrow)
        f_lbl.place(x=1150,y=380,width=200,height=100)

         #---right arrow---
        img_right_arrow=Image.open(r"C:\Users\Dark Demon\Desktop\Face Recognition system\img\right.jpg")
        img_right_arrow=img_right_arrow.resize((200,100),Image.ANTIALIAS)
        self.photoimg_right_arrow=ImageTk.PhotoImage(img_right_arrow)

        f_lbl=Label(self.root,image=self.photoimg_right_arrow)
        f_lbl.place(x=200,y=380,width=200,height=100)



        img_bottom=Image.open(r"C:\Users\Dark Demon\Desktop\Face Recognition system\img\face2.jpg")
        img_bottom=img_bottom.resize((1530,400),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=475,width=1530,height=400)

       
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')          #gray scale image 
            imageNp=np.array(img,'uint8')               #unit8--->datatype
            id=int(os.path.split(image)[1].split('.')[1])


            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)

        #---------train classifier and save------
        clf=cv2.face.LBPHFaceRecognizer_create()            #---use LBPH algorithm--
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset completed..!!! ")








if __name__== "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()