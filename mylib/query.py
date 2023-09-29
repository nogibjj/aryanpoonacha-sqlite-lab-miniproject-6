"""Query the database"""

import sqlite3

def query():
    """Query the database to get cars with the most horsepower"""
    conn = sqlite3.connect("CarsDB.db")
    cursor = conn.cursor()
    
    # Query to find cars with the most horsepower
    cursor.execute("""
            SELECT car_name, hp
            FROM CarsDB
            ORDER BY hp DESC
            LIMIT 5
    """)
    
    result = cursor.fetchall()
    conn.close()

    # Print the query results
    if result:
        print("Cars with the Most Horsepower:")
        print("{:<20} {:<10}".format("Car Name", "HP"))
        print("-" * 30)
        for row in result:
            car_name, hp = row
            print("{:<20} {:<10}".format(car_name, hp))
    else:
        print("No cars with the most horsepower found.")

if __name__ == "__main__":
    query()
