from tkinter import * 
from PIL import Image,ImageTk
from employee import employeeClass
from supplier import supplierClass
from products import productclass
from entry import entryClass

class IMS:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("INVENTRY MANAGEMENT SYSTEM")
        self.root.config(bg="white")
        
        
        #====TITLE===#
        self.icon_title=PhotoImage(file="images/logo1.png")
        title=Label(self.root,text="INVENTORY MANAGEMENT SYSTEM",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
        
        #==BTN==#
        btn_logout=Label(self.root,text="Logout",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1150,y=10,width=150,height=50)
        
        #clock#
        self.lbl_clock=Label(self.root,text="Welcome to INVENTRY MANAGEMENT SYSTEM \t\t  Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15,),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        
        
        
        #left menu#
        self.Menu_logo=Image.open("images/menu_im.png")
        self.Menu_logo=self.Menu_logo.resize((200,200),Image.BILINEAR)
        self.Menu_logo=ImageTk.PhotoImage(self.Menu_logo)
        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=565)
        
        lbl_menu_logo=Label(LeftMenu,image=self.Menu_logo)
        lbl_menu_logo.pack(side=TOP,fill=X)
        self.icon_side=PhotoImage(file="images/side.png")
        LBL_MENU=Label(LeftMenu,text="MENU",font=("times new roman",20,),bg="#009688",).pack(side=TOP,fill=X)
        
         
        BTN_EMPLOYEE=Button(LeftMenu,text="Employee",command=self.employee,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,relief=RIDGE,cursor="hand2").pack(side=TOP,fill=X)
        BTN_Supplier=Button(LeftMenu,text="Supplier",command=self.supplier,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,relief=RIDGE,cursor="hand2").pack(side=TOP,fill=X)
        BTN_Products=Button(LeftMenu,text="Products",command=self.product,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,relief=RIDGE,cursor="hand2").pack(side=TOP,fill=X)
         
        BTN_Entry=Button(LeftMenu,text="Entries",command=self.entry,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,relief=RIDGE,cursor="hand2").pack(side=TOP,fill=X)
       
        BTN_Sales=Button(LeftMenu,text="Sales",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,relief=RIDGE,cursor="hand2").pack(side=TOP,fill=X)
        BTN_Exit=Button(LeftMenu,text="Exit",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,relief=RIDGE,cursor="hand2").pack(side=TOP,fill=X)
        
        
        #====CONTENT====#
        self.lbl_employee=Label(self.root,text="Total Employee\n[0]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)
        
        self.lbl_Supplier=Label(self.root,text="Total SUPPLIER\n[0]",bd=5,relief=RIDGE,bg="#ff5722",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_Supplier.place(x=650,y=120,height=150,width=300)
        self.lbl_Category=Label(self.root,text="Total Category\n[0]",bd=5,relief=RIDGE,bg="#009688",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_Category.place(x=1000,y=120,height=150,width=300)
        self.lbl_Product=Label(self.root,text="Total Product\n[0]",bd=5,relief=RIDGE,bg="#607d8b",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_Product.place(x=300,y=300,height=150,width=300)
        self.lbl_Sales=Label(self.root,text="Total Sales\n[0]",bd=5,relief=RIDGE,bg="#ffc107",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_Sales.place(x=650,y=300,height=150,width=300)
        
      
       
       
       #FOOTER#
        lbl_footer=Label(self.root,text="IMS-inventry management system|For any quries--------**",font=("times new roman",10,),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)

#==================================================================================================================================================================================================================
    def employee(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=employeeClass(self.new_win)
    def supplier(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=supplierClass(self.new_win)
    def product(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=productclass(self.new_win)
    def entry(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=entryClass(self.new_win)
    
    
if __name__ == "__main__":       
 root=Tk()
 obj=IMS(root)
 

root.mainloop()
