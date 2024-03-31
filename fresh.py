import sqlite3

def create_tables():
     # Connect to the database or create a new one if it doesn't exist
    conn = sqlite3.connect('inventoryV2.db')
    cursor = conn.cursor()
    # Create the main table (Bill of Materials) with foreign key constraints
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS robo1 (
        ItemNo INTEGER PRIMARY KEY,
        ComponentDescription TEXT,
        Quantity INTEGER,
        Subassembly TEXT,
        SubassemblyQuantity INTEGER,
        FOREIGN KEY(Subassembly) REFERENCES SubassemblyA(ItemNo) ON DELETE CASCADE,
        FOREIGN KEY(Subassembly) REFERENCES SubassemblyB(ItemNo) ON DELETE CASCADE,
        FOREIGN KEY(Subassembly) REFERENCES SubassemblyC(ItemNo) ON DELETE CASCADE,
        FOREIGN KEY(Subassembly) REFERENCES SubassemblyD(ItemNo) ON DELETE CASCADE
    );
    ''') 
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS robo2 (
        ItemNo INTEGER PRIMARY KEY,
        ComponentDescription TEXT,
        Quantity INTEGER,
        Subassembly TEXT,
        SubassemblyQuantity INTEGER,
        FOREIGN KEY(Subassembly) REFERENCES SubassemblyA(ItemNo) ON DELETE CASCADE,
        FOREIGN KEY(Subassembly) REFERENCES SubassemblyB(ItemNo) ON DELETE CASCADE,
        FOREIGN KEY(Subassembly) REFERENCES SubassemblyC(ItemNo) ON DELETE CASCADE,
        FOREIGN KEY(Subassembly) REFERENCES SubassemblyD(ItemNo) ON DELETE CASCADE
    );
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS robo3 (
        ItemNo INTEGER PRIMARY KEY,
        ComponentDescription TEXT,
        Quantity INTEGER,
        Subassembly TEXT,
        SubassemblyQuantity INTEGER,
        FOREIGN KEY(Subassembly) REFERENCES SubassemblyA(ItemNo) ON DELETE CASCADE,
        FOREIGN KEY(Subassembly) REFERENCES SubassemblyB(ItemNo) ON DELETE CASCADE,
        FOREIGN KEY(Subassembly) REFERENCES SubassemblyC(ItemNo) ON DELETE CASCADE,
        FOREIGN KEY(Subassembly) REFERENCES SubassemblyD(ItemNo) ON DELETE CASCADE
    );
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS robo4 (
        ItemNo INTEGER PRIMARY KEY,
        ComponentDescription TEXT,
        Quantity INTEGER,
        Subassembly TEXT,
        SubassemblyQuantity INTEGER,
        FOREIGN KEY(Subassembly) REFERENCES SubassemblyA(ItemNo) ON DELETE CASCADE,
        FOREIGN KEY(Subassembly) REFERENCES SubassemblyB(ItemNo) ON DELETE CASCADE,
        FOREIGN KEY(Subassembly) REFERENCES SubassemblyC(ItemNo) ON DELETE CASCADE,
        FOREIGN KEY(Subassembly) REFERENCES SubassemblyD(ItemNo) ON DELETE CASCADE
    );
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS robo5 (
        ItemNo INTEGER PRIMARY KEY,
        ComponentDescription TEXT,
        Quantity INTEGER,
        Subassembly TEXT,
        SubassemblyQuantity INTEGER,
        FOREIGN KEY(Subassembly) REFERENCES SubassemblyA(ItemNo) ON DELETE CASCADE,
        FOREIGN KEY(Subassembly) REFERENCES SubassemblyB(ItemNo) ON DELETE CASCADE,
        FOREIGN KEY(Subassembly) REFERENCES SubassemblyC(ItemNo) ON DELETE CASCADE,
        FOREIGN KEY(Subassembly) REFERENCES SubassemblyD(ItemNo) ON DELETE CASCADE
    );
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS robo6 (
        ItemNo INTEGER PRIMARY KEY,
        ComponentDescription TEXT,
        Quantity INTEGER,
        Subassembly TEXT,
        SubassemblyQuantity INTEGER,
        FOREIGN KEY(Subassembly) REFERENCES SubassemblyA(ItemNo) ON DELETE CASCADE,
        FOREIGN KEY(Subassembly) REFERENCES SubassemblyB(ItemNo) ON DELETE CASCADE,
        FOREIGN KEY(Subassembly) REFERENCES SubassemblyC(ItemNo) ON DELETE CASCADE,
        FOREIGN KEY(Subassembly) REFERENCES SubassemblyD(ItemNo) ON DELETE CASCADE
    );
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS robo7(
        ItemNo INTEGER PRIMARY KEY,
        ComponentDescription TEXT,
        Quantity INTEGER,
        Subassembly TEXT,
        SubassemblyQuantity INTEGER,
        FOREIGN KEY(Subassembly) REFERENCES SubassemblyA(ItemNo) ON DELETE CASCADE,
        FOREIGN KEY(Subassembly) REFERENCES SubassemblyB(ItemNo) ON DELETE CASCADE,
        FOREIGN KEY(Subassembly) REFERENCES SubassemblyC(ItemNo) ON DELETE CASCADE,
        FOREIGN KEY(Subassembly) REFERENCES SubassemblyD(ItemNo) ON DELETE CASCADE
    );
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS robo8 (
        ItemNo INTEGER PRIMARY KEY,
        ComponentDescription TEXT,
        Quantity INTEGER,
        Subassembly TEXT,
        SubassemblyQuantity INTEGER,
        FOREIGN KEY(Subassembly) REFERENCES SubassemblyA(ItemNo) ON DELETE CASCADE,
        FOREIGN KEY(Subassembly) REFERENCES SubassemblyB(ItemNo) ON DELETE CASCADE,
        FOREIGN KEY(Subassembly) REFERENCES SubassemblyC(ItemNo) ON DELETE CASCADE,
        FOREIGN KEY(Subassembly) REFERENCES SubassemblyD(ItemNo) ON DELETE CASCADE
    );
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS robo9 (
        ItemNo INTEGER PRIMARY KEY,
        ComponentDescription TEXT,
        Quantity INTEGER,
        Subassembly TEXT,
        SubassemblyQuantity INTEGER,
        FOREIGN KEY(Subassembly) REFERENCES SubassemblyA(ItemNo) ON DELETE CASCADE,
        FOREIGN KEY(Subassembly) REFERENCES SubassemblyB(ItemNo) ON DELETE CASCADE,
        FOREIGN KEY(Subassembly) REFERENCES SubassemblyC(ItemNo) ON DELETE CASCADE,
        FOREIGN KEY(Subassembly) REFERENCES SubassemblyD(ItemNo) ON DELETE CASCADE
    );
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS robo10 (
        ItemNo INTEGER PRIMARY KEY,
        ComponentDescription TEXT,
        Quantity INTEGER,
        Subassembly TEXT,
        SubassemblyQuantity INTEGER,
        FOREIGN KEY(Subassembly) REFERENCES SubassemblyA(ItemNo) ON DELETE CASCADE,
        FOREIGN KEY(Subassembly) REFERENCES SubassemblyB(ItemNo) ON DELETE CASCADE,
        FOREIGN KEY(Subassembly) REFERENCES SubassemblyC(ItemNo) ON DELETE CASCADE,
        FOREIGN KEY(Subassembly) REFERENCES SubassemblyD(ItemNo) ON DELETE CASCADE
    );
    ''')
    # Create subassembly tables (if not already created)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS SubassemblyA (
        ItemNo TEXT PRIMARY KEY,
        ComponentDescription TEXT,
        Quantity INTEGER
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS SubassemblyB (
        ItemNo TEXT PRIMARY KEY,
        ComponentDescription TEXT,
        Quantity INTEGER
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS SubassemblyC (
        ItemNo TEXT PRIMARY KEY,
        ComponentDescription TEXT,
        Quantity INTEGER
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS SubassemblyD (
        ItemNo TEXT PRIMARY KEY,
        ComponentDescription TEXT,
        Quantity INTEGER
    );
    ''')

    # Create the Manufactured Components table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ManufacturedComponents (
        ItemNo TEXT PRIMARY KEY,
        ComponentDescription TEXT,
        Quantity INTEGER,
        ManufacturingLeadTime INTEGER
    );
    ''')
    cursor.execute('''
CREATE TABLE IF NOT EXISTS Orders (
    OrderId INTEGER PRIMARY KEY AUTOINCREMENT,
    CustomerId INTEGER,
    ItemNo INTEGER,
    QuantityOrdered INTEGER,
    OrderDate DATE,
    FOREIGN KEY(ItemNo) REFERENCES BillOfMaterials(ItemNo) ON DELETE CASCADE
);
''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def insert_data(table_name, data):
    # Connect to the database
    conn = sqlite3.connect('inventoryV2.db')
    cursor = conn.cursor()

    # Insert data into the specified table
    for row in data:
        placeholders = ', '.join(['?' for _ in row])
        sql_statement = f'INSERT OR REPLACE INTO {table_name} VALUES ({placeholders});'
        cursor.execute(sql_statement, row)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


def main():
    create_tables()

    # Data for the BillOfMaterials table
    robo1_data = [
        (1, 'Robot Chassis', 1, None, None),
        (2, 'Motor Assembly', 2, 'SubassemblyA', 1),
        (3, 'Motor Driver Board', 1, 'SubassemblyA', 1),
        (4, 'Robot Controller Board', 1, None, None),
        (5, 'Arm Assembly', 1, 'SubassemblyB', 1),
        (6, 'Gripper Mechanism', 1, 'SubassemblyB', 1),
        (7, 'Sensor Array', 1, 'SubassemblyC', 1),
        (8, 'Sensor Interface Board', 1, 'SubassemblyC', 1),
        (9, 'Power Distribution Unit', 1, None, None),
        (10, 'Battery Pack', 1, 'SubassemblyD', 1),
        (11, 'Wheels', 4, None, None),
        (12, 'Nuts and Bolts Set', 1, None, None),
        (13, 'Screws Set', 1, None, None),
        (14, 'User Manual', 1, None, None)
        
    ]
    
    robo2_data = [
        (1, 'Robot Chassis', 1, None, None),
        (2, 'Motor Assembly', 2, 'SubassemblyA', 1),
        (3, 'Motor Driver Board', 1, 'SubassemblyA', 1),
        (4, 'Robot Controller Board', 1, None, None),
        (5, 'Arm Assembly', 1, 'SubassemblyB', 1),
        (6, 'Gripper Mechanism', 1, 'SubassemblyB', 1),
        (7, 'Sensor Array', 1, 'SubassemblyC', 1),
        (8, 'Sensor Interface Board', 1, 'SubassemblyC', 1),
        (9, 'Power Distribution Unit', 1, None, None),
        (10, 'Battery Pack', 1, 'SubassemblyD', 1),
        (11, 'Wheels', 4, None, None),
        (12, 'Nuts and Bolts Set', 1, None, None),
        (13, 'Screws Set', 1, None, None),
        (14, 'User Manual', 1, None, None)
        
    ] 
    robo3_data = [
        (1, 'Robot Chassis', 1, None, None),
        (2, 'Motor Assembly', 2, 'SubassemblyA', 1),
        (3, 'Motor Driver Board', 1, 'SubassemblyA', 1),
        (4, 'Robot Controller Board', 1, None, None),
        (5, 'Arm Assembly', 1, 'SubassemblyB', 1),
        (6, 'Gripper Mechanism', 1, 'SubassemblyB', 1),
        (7, 'Sensor Array', 1, 'SubassemblyC', 1),
        (8, 'Sensor Interface Board', 1, 'SubassemblyC', 1),
        (9, 'Power Distribution Unit', 1, None, None),
        (10, 'Battery Pack', 1, 'SubassemblyD', 1),
        (11, 'Wheels', 4, None, None),
        (12, 'Nuts and Bolts Set', 1, None, None),
        (13, 'Screws Set', 1, None, None),
        (14, 'User Manual', 1, None, None)
        
    ]
    robo4_data = [
        (1, 'Robot Chassis', 1, None, None),
        (2, 'Motor Assembly', 2, 'SubassemblyA', 1),
        (3, 'Motor Driver Board', 1, 'SubassemblyA', 1),
        (4, 'Robot Controller Board', 1, None, None),
        (5, 'Arm Assembly', 1, 'SubassemblyB', 1),
        (6, 'Gripper Mechanism', 1, 'SubassemblyB', 1),
        (7, 'Sensor Array', 1, 'SubassemblyC', 1),
        (8, 'Sensor Interface Board', 1, 'SubassemblyC', 1),
        (9, 'Power Distribution Unit', 1, None, None),
        (10, 'Battery Pack', 1, 'SubassemblyD', 1),
        (11, 'Wheels', 4, None, None),
        (12, 'Nuts and Bolts Set', 1, None, None),
        (13, 'Screws Set', 1, None, None),
        (14, 'User Manual', 1, None, None)
        
    ] 
    robo5_data = [
        (1, 'Robot Chassis', 1, None, None),
        (2, 'Motor Assembly', 2, 'SubassemblyA', 1),
        (3, 'Motor Driver Board', 1, 'SubassemblyA', 1),
        (4, 'Robot Controller Board', 1, None, None),
        (5, 'Arm Assembly', 1, 'SubassemblyB', 1),
        (6, 'Gripper Mechanism', 1, 'SubassemblyB', 1),
        (7, 'Sensor Array', 1, 'SubassemblyC', 1),
        (8, 'Sensor Interface Board', 1, 'SubassemblyC', 1),
        (9, 'Power Distribution Unit', 1, None, None),
        (10, 'Battery Pack', 1, 'SubassemblyD', 1),
        (11, 'Wheels', 4, None, None),
        (12, 'Nuts and Bolts Set', 1, None, None),
        (13, 'Screws Set', 1, None, None),
        (14, 'User Manual', 1, None, None)
        
    ] 
    robo6_data = [
        (1, 'Robot Chassis', 1, None, None),
        (2, 'Motor Assembly', 2, 'SubassemblyA', 1),
        (3, 'Motor Driver Board', 1, 'SubassemblyA', 1),
        (4, 'Robot Controller Board', 1, None, None),
        (5, 'Arm Assembly', 1, 'SubassemblyB', 1),
        (6, 'Gripper Mechanism', 1, 'SubassemblyB', 1),
        (7, 'Sensor Array', 1, 'SubassemblyC', 1),
        (8, 'Sensor Interface Board', 1, 'SubassemblyC', 1),
        (9, 'Power Distribution Unit', 1, None, None),
        (10, 'Battery Pack', 1, 'SubassemblyD', 1),
        (11, 'Wheels', 4, None, None),
        (12, 'Nuts and Bolts Set', 1, None, None),
        (13, 'Screws Set', 1, None, None),
        (14, 'User Manual', 1, None, None)
        
    ] 
    robo7_data = [
        (1, 'Robot Chassis', 1, None, None),
        (2, 'Motor Assembly', 2, 'SubassemblyA', 1),
        (3, 'Motor Driver Board', 1, 'SubassemblyA', 1),
        (4, 'Robot Controller Board', 1, None, None),
        (5, 'Arm Assembly', 1, 'SubassemblyB', 1),
        (6, 'Gripper Mechanism', 1, 'SubassemblyB', 1),
        (7, 'Sensor Array', 1, 'SubassemblyC', 1),
        (8, 'Sensor Interface Board', 1, 'SubassemblyC', 1),
        (9, 'Power Distribution Unit', 1, None, None),
        (10, 'Battery Pack', 1, 'SubassemblyD', 1),
        (11, 'Wheels', 4, None, None),
        (12, 'Nuts and Bolts Set', 1, None, None),
        (13, 'Screws Set', 1, None, None),
        (14, 'User Manual', 1, None, None)
        
    ] 
    robo8_data = [
        (1, 'Robot Chassis', 1, None, None),
        (2, 'Motor Assembly', 2, 'SubassemblyA', 1),
        (3, 'Motor Driver Board', 1, 'SubassemblyA', 1),
        (4, 'Robot Controller Board', 1, None, None),
        (5, 'Arm Assembly', 1, 'SubassemblyB', 1),
        (6, 'Gripper Mechanism', 1, 'SubassemblyB', 1),
        (7, 'Sensor Array', 1, 'SubassemblyC', 1),
        (8, 'Sensor Interface Board', 1, 'SubassemblyC', 1),
        (9, 'Power Distribution Unit', 1, None, None),
        (10, 'Battery Pack', 1, 'SubassemblyD', 1),
        (11, 'Wheels', 4, None, None),
        (12, 'Nuts and Bolts Set', 1, None, None),
        (13, 'Screws Set', 1, None, None),
        (14, 'User Manual', 1, None, None)
        
    ] 
    robo9_data = [
        (1, 'Robot Chassis', 1, None, None),
        (2, 'Motor Assembly', 2, 'SubassemblyA', 1),
        (3, 'Motor Driver Board', 1, 'SubassemblyA', 1),
        (4, 'Robot Controller Board', 1, None, None),
        (5, 'Arm Assembly', 1, 'SubassemblyB', 1),
        (6, 'Gripper Mechanism', 1, 'SubassemblyB', 1),
        (7, 'Sensor Array', 1, 'SubassemblyC', 1),
        (8, 'Sensor Interface Board', 1, 'SubassemblyC', 1),
        (9, 'Power Distribution Unit', 1, None, None),
        (10, 'Battery Pack', 1, 'SubassemblyD', 1),
        (11, 'Wheels', 4, None, None),
        (12, 'Nuts and Bolts Set', 1, None, None),
        (13, 'Screws Set', 1, None, None),
        (14, 'User Manual', 1, None, None)
        
    ] 
    robo10_data = [
        (1, 'Robot Chassis', 1, None, None),
        (2, 'Motor Assembly', 2, 'SubassemblyA', 1),
        (3, 'Motor Driver Board', 1, 'SubassemblyA', 1),
        (4, 'Robot Controller Board', 1, None, None),
        (5, 'Arm Assembly', 1, 'SubassemblyB', 1),
        (6, 'Gripper Mechanism', 1, 'SubassemblyB', 1),
        (7, 'Sensor Array', 1, 'SubassemblyC', 1),
        (8, 'Sensor Interface Board', 1, 'SubassemblyC', 1),
        (9, 'Power Distribution Unit', 1, None, None),
        (10, 'Battery Pack', 1, 'SubassemblyD', 1),
        (11, 'Wheels', 4, None, None),
        (12, 'Nuts and Bolts Set', 1, None, None),
        (13, 'Screws Set', 1, None, None),
        (14, 'User Manual', 1, None, None)
        
    ]

    # Data for the subassembly tables
    subassembly_a_data = [
        ('A1', 'DC Motor', 2),
        ('A2', 'Motor Mount', 2),
        ('A3', 'Motor Connector', 2),
    ]

    subassembly_b_data = [
        ('B1', 'Arm Base', 1),
        ('B2', 'Arm Segment', 2),
        ('B3', 'Arm Joint', 3),
    ]

    subassembly_c_data = [
        ('C1', 'Proximity Sensor', 4),
        ('C2', 'Light Sensor', 2),
        ('C3', 'Infrared Sensor', 2),
    ]

    subassembly_d_data = [
        ('D1', 'Lithium-ion Battery', 4),
        ('D2', 'Battery Holder', 1),
        ('D3', 'Battery Management Circuit', 1),
    ]

    # Data for the Manufactured Components table
    manufactured_components_data = [
        ('1', 'Robot Chassis', 50, 7),
        ('4', 'Robot Controller Board', 50, 14),
        ('9', 'Power Distribution Unit', 50, 10),
        ('11','Wheels', 50, 7),
        ('12','Nuts and Bolts Set', 50, 14),
        ('13','Screws Set', 50, 10),
        ('14','User Manual', 50, 7),
        ('A1','DC Motor', 50, 7),
        ('A2','Motor Mount', 50, 14),
        ('A3','Motor Connector', 50, 7),
        ('B1','Arm Base', 50, 7),
        ('B2','Arm Segment', 50, 14),
        ('B3','Arm Joint', 50, 14),
        ('C1','Proximity Sensor', 50, 7),
        ('C2','Light Sensor', 50, 7),
        ('C3','Infrared Sensor', 50, 14),
        ('D1','Lithium-ion Battery', 50, 7),
        ('D2','Battery Holder', 50, 14),
        ('D3','Battery Management Circuit', 50, 7)
    
    ]

    # Insert data into the respective tables
    insert_data('robo1', robo1_data)
    insert_data('robo2', robo2_data) 
    insert_data('robo3', robo3_data)
    insert_data('robo4', robo4_data)
    insert_data('robo5', robo5_data)
    insert_data('robo6', robo6_data)
    insert_data('robo7', robo7_data)
    insert_data('robo8', robo8_data)
    insert_data('robo9', robo9_data)
    insert_data('robo10', robo10_data)
    insert_data('SubassemblyA', subassembly_a_data)
    insert_data('SubassemblyB', subassembly_b_data)
    insert_data('SubassemblyC', subassembly_c_data)
    insert_data('SubassemblyD', subassembly_d_data)
    insert_data('ManufacturedComponents', manufactured_components_data)

robo_number=0
num_of_robots=0
def update_manufactured_components(robo_number, num_of_robots):
         
         conn = sqlite3.connect('inventoryV2.db')
         cursor = conn.cursor()
        # Retrieve the data from the ManufacturedComponents table
        #  d =  cursor.execute("select * from ManufacturerComponents")
         tables={"robo1":"table data for robo1","robo2":"table data for robo2","robo3":"table data for robo3","robo4":"table data for robo4","robo5":"table data for robo5","robo6":"table data for robo6","robo7":"table data for robo7","robo8":"table data for robo8","robo9":"table data for robo9","robo10":"table data for robo10"}

         robo_number=input("enter the robo number")
         num_of_robots = input("Enter the number of robots")
         
         table_name = f"robo{robo_number}"
         if table_name in tables:
             
            data =  cursor.execute(f"select * from robo{robo_number}").fetchall()
            for row in data:
                #  print(row)
                if row[3] == None :
                    key = row[1]
                    value = row[2]*num_of_robots
                    cursor.execute("select * from ManufacturedComponents where componentDescription=?",(key,))
                    existQuantity = cursor.fetchone()[2]
                    updateQuantity = existQuantity - value
                    print(f"row number is {key}... existing : {existQuantity} .. Required : {value}...Remaining :{updateQuantity}")
                    cursor.execute("UPDATE ManufacturedComponents set Quantity = ? WHERE ComponentDescription = ?",(updateQuantity, key))  
                    conn.commit()
    
                else:
                    subAsmbTbleName = row[3]
                    value = row[2]*row[4]*num_of_robots
                    
                    statement = f'Select * from {subAsmbTbleName}'
                    # print(statement)
                    subAsbdata = cursor.execute(statement).fetchall()
                    for rw in subAsbdata:
                        key = rw[1]
                        innervalue = rw[2]
                        
                        cursor.execute("select * from ManufacturedComponents where componentDescription=?",(key,))
                        existQuantity = cursor.fetchone()[2]
                        updateQuantity = existQuantity-(value*innervalue)
                        # print(f"row number is {key}... existing : {existQuantity} .. Required : {value}...Remaining :{updateQuantity}")
                        cursor.execute("UPDATE ManufacturedComponents set Quantity = ? WHERE ComponentDescription = ?",(updateQuantity, key))  
                        conn.commit()
                    
                
        
            
            
            return
         else:
             print(f"table {table_name}does not exist")
    
    
if __name__ == "__main__":
        main()

update_manufactured_components(robo_number,num_of_robots)
            