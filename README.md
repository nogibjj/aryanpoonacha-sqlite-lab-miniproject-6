## SQLite Lab
Miniproject 6 for IDS 706, Fall 2023.

Contains the following components in the mylib folder:

Extract.py: Loads a cars dataset from an online URL and saves it locally as cars.csv. We then repeat this process for a second dataset of cars and save it locally into cars2.csv.

Transform_load.py: We then load both csvs into MySQL databases.

query.py: We then compare the average Horsepower of cars in the second database with the top 5 cars with the highest horsepower in the first database with a complex query.

Main.py allows these scripts to be called with command line arguments and runs them automatically in conjunction with testing and CI/CD in the .yaml and Makefiles for automated integration + testing.