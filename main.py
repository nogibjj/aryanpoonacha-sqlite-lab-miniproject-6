"""
ETL-Query script
"""
import argparse
from mylib.extract import extract
from mylib.transform_load import load
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

    args = parser.parse_args()

    if args.extract:
        print("Extracting data...")
        extract()

    if args.transformload:
        print("Transforming and loadings data into SQLite database...")
        load()

    if args.query:
        print("Querying data...")
        query()


if __name__ == "__main__":
    main()
