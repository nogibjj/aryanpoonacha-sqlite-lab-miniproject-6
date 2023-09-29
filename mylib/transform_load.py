"""
Transforms and Loads data into the local SQLite3 database
Example:
,general name,count_products,ingred_FPro,avg_FPro_products,avg_distance_root,ingred_normalization_term,semantic_tree_name,semantic_tree_node
"""
import sqlite3
import csv
import os

#load the csv file and insert into a new sqlite3 database
def load(dataset="tables/cars.csv"):
    """"Transforms and Loads data into the local SQLite3 database"""

    #prints the full working directory and path
    print(os.getcwd())
    payload = csv.reader(open(dataset, newline=''), delimiter=',')
    next(payload)  # Skip the header row
    
    conn = sqlite3.connect('CarsDB.db')
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS CarsDB")
    c.execute("""
    CREATE TABLE CarsDB (
        car_name TEXT PRIMARY KEY,
        mpg REAL,
        cyl INTEGER,
        disp REAL,
        hp INTEGER,
        drat REAL,
        wt REAL,
        qsec REAL,
        vs INTEGER,
        am INTEGER,
        gear INTEGER,
        carb INTEGER
    )
""")
    #insert
    c.executemany("""
    INSERT INTO CarsDB (car_name, mpg, cyl, disp, hp, drat, wt, qsec, vs, am, gear, carb)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", payload)
    
    conn.commit()
    conn.close()
    return "CarsDB.db"

