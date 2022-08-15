import sqlite3
# print("Imported successfully!")

#Connect to a database
conn = sqlite3.connect('sales_db')
# print("Connected successfully!")

#Create a cursor object
curs = conn.cursor()
# print("Cursor connected successfully!")

#Creating a new table
curs.execute("""CREATE TABLE inventory_data(
            item_ID INTEGER PRIMARY KEY,
            name TEXT,
            cost_price REAL,
            quantity_in_stock INTEGER
            )
""")
print("Table created successfully!")

#Inserting several values to the table
Stationeries_list = [('01', 'Note Book', '70.0', '1'),
                    ('02', 'Biro', '20.0', '10'),
                    ('03', 'Ruler', '25.0', '2'),
                    ('04', 'Stapler', '100.0', '20'),
                    ('05', 'pencil', '10.0', '1'),
                    ('06', 'sticky notes', '50.0', '2'),
                    ('07', 'Eraser', '15.0', '12'),
                    ('08', 'Crayons', '25.0', '0'),
                    ('09', 'Mathset', '76.8', '1'),
                    ('10', 'Ball Pen', '55.5', '0')
                    ]
# print("Stationeries_list created successfully!")

curs.executemany("INSERT INTO inventory_data VALUES (?, ?, ?, ?)", Stationeries_list)

#querying the database
curs.execute("SELECT * FROM inventory_data")
# print("Query executed successfully!")

#format output to display in a tabular form
items = curs.fetchall()
# print("item_ID"+ "\t\tname"+ "\t\t\tcost_price"+ "\t\t\tquantity_in_stock" "\n" f"{'.' * 80}") 

#looping through the items
for item in items:
    item_ID, name, cost_price, quantity_in_stock = item
    # print(f"{item_ID}\t\t{name}\t\t{cost_price}\t\t\t{quantity_in_stock}")
    # print(item)

curs.execute("""SELECT * FROM inventory_data
            WHERE quantity_in_stock < 20
            ORDER BY cost_price DESC;
            """
            )
item = curs.fetchall()
print(item)


#commit the database and table
conn.commit()

#close the connection to the database
conn.close()

