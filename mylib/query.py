"""Query the database"""

import sqlite3
def query():
    """Query both CarsDB.db and Cars2DB.db and perform a complex SQL query involving joins, aggregation, and sorting"""

    # Connect to CarsDB.db
    conn_cars = sqlite3.connect("CarsDB.db")
    cursor_cars = conn_cars.cursor()

    # Query to find cars with the most horsepower in CarsDB.db
    cursor_cars.execute("""
        SELECT car_name, hp
        FROM CarsDB
        ORDER BY hp DESC
        LIMIT 5
    """)

    result_cars = cursor_cars.fetchall()

    # Connect to Cars2DB.db
    conn_cars2 = sqlite3.connect("Cars2DB.db")
    cursor_cars2 = conn_cars2.cursor()

    # Complex query: Calculate the average horsepower of cars from Cars2DB.db
    cursor_cars2.execute("""
        SELECT AVG(CAST(Horsepower AS INTEGER)) AS avg_horsepower
        FROM Cars2DB
    """)

    result_cars2 = cursor_cars2.fetchone()

    conn_cars.close()
    conn_cars2.close()

    # Print the query results
    if result_cars:
        print("Cars with the Most Horsepower (CarsDB.db):")
        print("{:<20} {:<10}".format("Car Name", "HP"))
        print("-" * 30)
        for row in result_cars:
            car_name, hp = row
            print("{:<20} {:<10}".format(car_name, hp))
    else:
        print("No cars with the most horsepower found in CarsDB.db.")

    if result_cars2:
        print("\nAverage Horsepower (Cars2DB.db):")
        print("{:<20}".format("Avg HP"))
        print("-" * 20)
        avg_horsepower = result_cars2[0]
        print("{:<20.2f}".format(avg_horsepower))
    else:
        print("No data found in Cars2DB.db.")

if __name__ == "__main__":
    query()