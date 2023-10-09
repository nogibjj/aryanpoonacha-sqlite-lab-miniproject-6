"""
ETL-Query script
"""

import argparse
from mylib.extract import extract
from mylib.transform_load import load, load2
from mylib.query import query


def main():
    parser = argparse.ArgumentParser(description="ETL-Query script")
    parser.add_argument("--extract", action="store_true", help="Extract data")
    parser.add_argument(
        "--transformload",
        action="store_true",
        help="Transform and load data into SQLite db",
    )
    parser.add_argument("--query", action="store_true", help="Query data")
    parser.add_argument(
        "--url", type=str, help="URL for data extraction"
    )  # Add this line

    args = parser.parse_args()

    if args.extract:
        print("Extracting data...")
        # extract cars.csv
        extract()
        # extract cars2.csv
        extract(
            url="https://raw.githubusercontent.com/sassoftware/sas-viya-programming/master/data/cars.csv",
            file_path="tables/cars2.csv",
        )

    if args.transformload:
        print("Transforming and loading data into SQLite database...")
        # load cars
        load()
        # load cars2
        load2()

    if args.query:
        print("Querying data...")
        query()


if __name__ == "__main__":
    main()
