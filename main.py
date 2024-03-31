from tkinter import*
from PIL import Image,ImageTk

class IMS:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1300x700+0+0")
        self.root.title("inventry management system for vidani automation ")
        
        
        #====title===#
        
        title=Label(self.root,text="INVENTRY MANAGEMENT SYSTEM",,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w").place(x=0,y=0,relwidth=1,height=70)
       
       
       #==BUTTON #
       
       
        root=Tk()
        obj=IMS(root)
        root.mainloop()
        