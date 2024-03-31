import sqlite3
def create_db():
    con=sqlite3.connect(database=r'ims.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,contact text,dob text,doj text,pass text,utype text,address text,salary text)")
    con.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS product(itemno INTEGER PRIMARY KEY AUTOINCREMENT,name text,sub_A text,sub_B text,sub_C text,sub_D text,sub_q text,sub text,quantity text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT,name text,contact text,desc text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS comp_robo1(ItemNo INTEGER PRIMARY KEY, ComponentDescription TEXT,Quantity INTEGER,Subassembly TEXT, SubassemblyQuantity INTEGER)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS SubassemblyA(ItemNo INTEGER PRIMARY KEY, ComponentDescription TEXT, Quantity INTEGER)")
    con.commit()
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS SubassemblyB(ItemNo INTEGER PRIMARY KEY, ComponentDescription TEXT, Quantity INTEGER)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS SubassemblyC(ItemNo INTEGER PRIMARY KEY, ComponentDescription TEXT, Quantity INTEGER)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS SubassemblyD(ItemNo INTEGER PRIMARY KEY, ComponentDescription TEXT, Quantity INTEGER)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS ManufacturedComponents( ItemNo INTEGER PRIMARY KEY, ComponentDescription TEXT, Quantity INTEGER,ManufacturingLeadTime INTEGER)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS Suppliers2(SupplierName TEXT,ContactPerson TEXT,ComponentDescription TEXT,UnitPrice REAL,LeadTime INTEGER)")
    con.commit()




    cur.execute("CREATE TABLE IF NOT EXISTS comp_robo2(ItemNo INTEGER PRIMARY KEY, ComponentDescription TEXT,Quantity INTEGER,Subassembly TEXT, SubassemblyQuantity INTEGER)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS comp_robo3(ItemNo INTEGER PRIMARY KEY, ComponentDescription TEXT,Quantity INTEGER,Subassembly TEXT, SubassemblyQuantity INTEGER)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS comp_robo4(ItemNo INTEGER PRIMARY KEY, ComponentDescription TEXT,Quantity INTEGER,Subassembly TEXT, SubassemblyQuantity INTEGER)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS comp_robo5(ItemNo INTEGER PRIMARY KEY, ComponentDescription TEXT,Quantity INTEGER,Subassembly TEXT, SubassemblyQuantity INTEGER)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS comp_robo6(ItemNo INTEGER PRIMARY KEY, ComponentDescription TEXT,Quantity INTEGER,Subassembly TEXT, SubassemblyQuantity INTEGER)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS comp_robo7(ItemNo INTEGER PRIMARY KEY, ComponentDescription TEXT,Quantity INTEGER,Subassembly TEXT, SubassemblyQuantity INTEGER)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS comp_robo8(ItemNo INTEGER PRIMARY KEY, ComponentDescription TEXT,Quantity INTEGER,Subassembly TEXT, SubassemblyQuantity INTEGER)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS comp_robo9(ItemNo INTEGER PRIMARY KEY, ComponentDescription TEXT,Quantity INTEGER,Subassembly TEXT, SubassemblyQuantity INTEGER)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS comp_robo10(ItemNo INTEGER PRIMARY KEY, ComponentDescription TEXT,Quantity INTEGER,Subassembly TEXT, SubassemblyQuantity INTEGER)")
    con.commit()


create_db()    

