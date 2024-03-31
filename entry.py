from tkinter import * 
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class entryClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("INVENTRY MANAGEMENT SYSTEM")
        self.root.config(bg="white")
        self.root.focus_force()
        #=========================================================
        # All variabesl
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        
        self.var_item_id=StringVar()
        self.var_sub=StringVar()
        self.var_Quantity=StringVar()
        self.var_name=StringVar()
        self.var_sub_q=StringVar()
        
        
       
        self.var_sub_A=StringVar()
        self.var_sub_B=StringVar()
        
        self.var_sub_C=StringVar()
        self.var_sub_D=StringVar()
      
        
        
        
        
        
        
        
        
        
        

        #SEARCHFRAME====
        SearchFrame=LabelFrame(self.root,text="Search table",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)        
        
        #===OPTINS==
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Name"),state="readonly",justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=180)        
        cmb_search.current(0)
        
        
        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)        
        btn_seach=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)        
        #title=====
        title=Label(self.root,text="Product Details",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1000)
        
        
        #=====Content====
        
        #ROW1=============================
        lbl_itemid=Label(self.root,text="Item No",font=("goudy old style",15),bg="white").place(x=50,y=150)
        lbl_sub=Label(self.root,text="S.assembly",font=("goudy old style",15),bg="white").place(x=350,y=150)
        lbl_Quantity=Label(self.root,text="Quantity",font=("goudy old style",15),bg="white").place(x=750,y=150)
      
        txt_itemid=Entry(self.root,textvariable=self.var_item_id,font=("goudy old style",15),bg="lightyellow").place(x=150,y=150,width=180)
    
        cmb_sub=ttk.Combobox(self.root,textvariable=self.var_sub,values=("Select","Sub.A","Sub.B","Sub.C","SUB.D"),state="readonly",justify=CENTER,font=("goudy old style",15))
        cmb_sub.place(x=500,y=150,width=180)       
        cmb_sub.current(0)
        
        txt_Quantity=Entry(self.root,textvariable=self.var_Quantity,font=("goudy old style",15),bg="lightyellow").place(x=850,y=150,width=180)
        
        #ROW2============================================================
        
        lbl_Name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=190)
        lbl_Sub_q=Label(self.root,text="Sub.Q",font=("goudy old style",15),bg="white").place(x=350,y=190)
       
        txt_NAME=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=150,y=190,width=180)
        txt_Sub_q=Entry(self.root,textvariable=self.var_sub_q,font=("goudy old style",15),bg="lightyellow").place(x=500,y=190,width=180)     
      
        #ROW3================================================================
        
       
        lbl_sub_A=Label(self.root,text="sub_A.",font=("goudy old style",15),bg="white").place(x=50,y=230)
        lbl_sub_B=Label(self.root,text="sub_B",font=("goudy old style",15),bg="white").place(x=350,y=230)
        
        txt_sub_A=Entry(self.root,textvariable=self.var_sub_A,font=("goudy old style",15),bg="lightyellow").place(x=150,y=230,width=180)
        txt_sub_B=Entry(self.root,textvariable=self.var_sub_B,font=("goudy old style",15),bg="lightyellow").place(x=500,y=230,width=180) 
        
        
        #row4================================   =============================
        
        
        lbl_sub_C=Label(self.root,text="sub_C.",font=("goudy old style",15),bg="white").place(x=50,y=270)
        lbl_sub_D=Label(self.root,text="sub_D.",font=("goudy old style",15),bg="white").place(x=500,y=270)
       
        self.txt_sub_C=Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.txt_sub_C.place(x=150,y=270,width=300,height=60)
        self.txt_sub_D=Entry(self.root,textvariable=self.var_sub_D,font=("goudy old style",15),bg="lightyellow")
        self.txt_sub_D.place(x=600,y=270,width=150) 
      
      
        #===BUTTONS================================================================
        
        btn_ADD=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=500,y=305,width=110,height=28)        
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=620,y=305,width=110,height=28)        
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=740,y=305,width=110,height=28)        
        btn_Clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=860,y=305,width=110,height=28)        
              
       
       #====product DETAILS=======================================================
        entry_frame=Frame(self.root,bd=5,relief=RIDGE)
        entry_frame.place(x=0,y=350,relwidth=1,height=350)
        scrolly=Scrollbar(entry_frame,orient=VERTICAL)
        scrollx=Scrollbar(entry_frame,orient=HORIZONTAL)
       
        self.ProductTable=ttk.Treeview(entry_frame,columns=("itemno", "name", "quantity", "sub", "sub_q","sub_A","sub_B","sub_C","sub_D"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        
        scrollx.config(command=self.ProductTable.xview)
        scrolly.config(command=self.ProductTable.yview)
        
        self.ProductTable.heading("itemno",text="Item no")
        self.ProductTable.heading("name",text="Name")
        
        self.ProductTable.heading("quantity",text="Quantity")
        
        self.ProductTable.heading("sub",text="subasembly")
        
        self.ProductTable.heading("sub_q",text="sub_quantity")
        self.ProductTable.heading("sub_A",text="sub_A")
        self.ProductTable.heading("sub_B",text="sub_B")
        self.ProductTable.heading("sub_C",text="sub_C")
        self.ProductTable.heading("sub_D",text="sub_D")
        
        
        self.ProductTable["show"]="headings"
        
        
        
        self.ProductTable.column("itemno",width=90)
        self.ProductTable.column("name",width=100)
        
        self.ProductTable.column("quantity",width=100)
        
        self.ProductTable.column("sub",width=100)
        
        self.ProductTable.column("sub_q",width=100)
          
        self.ProductTable.column("sub_A",width=100)
          
        self.ProductTable.column("sub_B",width=100)
          
        self.ProductTable.column("sub_C",width=100)
          
        self.ProductTable.column("sub_D",width=100)
        
        
       
        
        
        
            
        self.ProductTable.pack(fill=BOTH,expand=1)
        self.ProductTable.bind("<ButtonRelease -1>",self.get_data)
        self.show()

    def add(self):
       con=sqlite3.connect(database=r'ims.db')
       cur=con.cursor()
       try:
          if self.var_item_id.get()=="":
             messagebox.showerror("Error","Item No Must be required",parent=self.root)

          else:
             cur.execute("Select * from product where itemno=?",(self.var_item_id.get(),))
             row=cur.fetchone()
             if row!=None:
                messagebox.showerror("Error","This ITEM NO  already assigned try different",parent=self.root)
             else:
                cur.execute("Insert into product (itemno,name,quantity,sub,sub_q,sub_A,sub_B,sub_C,sub_D) values(?,?,?,?,?,?,?,?,?)",(
                   
                
                   
                   self.var_item_id.get(),
                   self.var_name.get(),
                   self.var_sub_A.get(),
                   self.var_sub.get(),
                   self.var_Quantity.get(),
                                            
                   self.var_sub_q.get(),
                             
                   self.var_sub_B.get(),
                   
                   self.txt_sub_C.get('1.0',END),
                   self.var_sub_D.get()
                 ))                                                                                                                  
                
                
                con.commit()
                messagebox.showinfo("Success","Table Added Successfully",parent=self.root)
                self.show()



       except Exception as ex:
          messagebox.showerror("Error",f"Error due to : {str(ex)}")            

    def show(self):
       con=sqlite3.connect(database=r'ims.db')
       cur=con.cursor()
       try:
          cur.execute("select * from product")
          rows=cur.fetchall()
          self.ProductTable.delete(*self.ProductTable.get_children())
          for row in rows:
             self.ProductTable.insert('',END,values=row)
       
       except Exception as ex:
          messagebox.showerror("Error",f"Error due to : {str(ex)}")   

    def get_data(self,ev):
       f=self.ProductTable.focus()
       content=(self.ProductTable.item(f))
       row=content['values'] 
       #print(row) 
       self.var_item_id.set(row[0]),
       self.var_name.set(row[1]),
       self.var_sub_A.set(row[2]),
       self.var_sub.set(row[3]),
       self.var_Quantity.set(row[4]),
                                            
       self.var_sub_q.set(row[5]),
                                       
       self.var_sub_B.set(row[7]),
       
       self.txt_sub_C.delete('1.0',END),
       self.txt_sub_C.insert(END,row[9])
       self.var_sub_D.set(row[10])

    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
          if self.var_item_id.get()=="":
             messagebox.showerror("Error","ITEM NO Must be required",parent=self.root)

          else:
             cur.execute("Select * from product where itemno=?",(self.var_item_id.get(),))
             row=cur.fetchone()
             if row==None:
                messagebox.showerror("Error","Invalid item no",parent=self.root)
             else:
                cur.execute("Update product set name=?,sub_A=?,quantity=?,sub=?,sub_q=?,sub_B=?,sub_C=?,sub_D=? where itemno=?",(
                   
                
                   
                   
                   self.var_name.get(),
                   self.var_sub_A.get(),
                   self.var_sub.get(),
                   self.var_Quantity.get(),
                                            
                   self.var_sub_q.get(),
                                         
                   self.var_sub_B.get(),
                   
                   self.txt_sub_C.get('1.0',END),
                   self.var_sub_D.get(),
                   self.var_item_id.get()
                 ))                                                                                                                  
                
                
                con.commit()
                messagebox.showinfo("Success","Product Updated Successfully",parent=self.root)
                self.show()



        except Exception as ex:
          messagebox.showerror("Error",f"Error due to : {str(ex)}")   

    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
           if self.var_item_id.get()=="":
             messagebox.showerror("Error","ITEM NO Must be required",parent=self.root)

           else:
             cur.execute("Select * from product where itemno=?",(self.var_item_id.get(),))
             row=cur.fetchone()
             if row==None:
                messagebox.showerror("Error","Invalid Item no",parent=self.root)
             else:
                op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                if op==True:
                   cur.execute("delete from product where itemno=?",(self.var_item_id.get(),))
                   con.commit()
                   messagebox.showinfo("Delete","item Deleted Successfully",parent=self.root)
                   
                   self.clear()
           
           
        except Exception as ex:
          messagebox.showerror("Error",f"Error due to : {str(ex)}")   


    def clear(self):
        
       self.var_item_id.set(""),
       self.var_name.set(""),
       self.var_sub_A.set(""),
       
       self.var_Quantity.set(""),
                                            
       self.var_sub_q.set(""),
      
                                            
       self.var_sub_B.set(""),
       
       self.txt_sub_C.delete('1.0',END),
       
       self.var_sub_D.set("")
       self.var_searchtxt.set("")
       self.var_searchby.set("Select")
       self.show()

    def search(self):    
       con=sqlite3.connect(database=r'ims.db')
       cur=con.cursor()
       try:
          if self.var_searchby.get()=="Select":
             messagebox.showerror("Error","Select Search By Option",parent=self.root)
          elif self.var_searchby.get()=="":
             messagebox.showerror("Error","Search Input Required",parent=self.root)
          else:  
             cur.execute("select * from product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
             rows=cur.fetchall()
             if len(rows)!=0:
                self.ProductTable.delete(*self.ProductTable.get_children())
                for row in rows:
                     self.ProductTable.insert('',END,values=row)
             else:
                messagebox.showerror("Error","No Record Found",parent=self.root)        
       
       except Exception as ex:
          messagebox.showerror("Error",f"Error due to : {str(ex)}") 
       

       
   


if __name__ == "__main__":       
 root=Tk()
 obj=entryClass(root)
 root.mainloop()
