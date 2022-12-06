			DATA MODELLING WITH PostgreSQL
### Summary:
The project is about creating a progres database with tables to optimize queries on song play  analysis. The main task is to creatae a database schema and ETL pipeline for this analysis.


### Procedures:
i. Create Database: the database created for this project 'sparkifydb'
ii. Create Table: the fact table for this project is 'songplays', whereas the dimension tables are users, artists, songs and time. 
iii. Insert Data into the Tables: the data extracted from the song dataset and the log dataset are inserted into the tables. 
iv. ETL process:  the etl process is carried out by runing the etl.py script in the terminal.
v. Test and Query: the script 'test.ipynb' is responsible for validating proper implementation.


### Files and descriptions:
i. create_tables.py: The python script contain functions to automate the process of creating and dropping the database and table.
ii. sql_queries.py: The file contains sql query that perform dropping, creation, insertion and of data into the table.
iii. etl.py: The python script contain the process of extracting the data, process and insert it into the tables.
iv. etl.ipynb: Interractive environment for testing the etl process.
v. test.ipynb: Interractive environment for testing the create table process.
vi. data: The folder that contains the song data and the log data in json format.

### Data folder
This folder contains the log_data and the songd_data. The extraction is done on etl.ipynb script. Thereafter, the extracted data were loaded into their respective tables. 

### How to run the project 

step 1: Run the create_tables.py script to create the database, tables through at the terminal  via 'python create_tables.py'.

step 2: Run the etl.py script at the terminal window via 'python etl.py' to run the etl process and load data into the database.
