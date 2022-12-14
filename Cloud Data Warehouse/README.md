# DATA WAREHOUSE

## INTRODUCTION

A music streaming startup, Sparkify want to move their processes and data from onpremises to the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

##  TASKS

The task is to build an ETL pipeline that extracts their data from S3, stages them in Redshift, and transforms data into a set of tables for analysis purposes.

## Project template
- Create_table.py: where facts and dimension tables for the schema in Redshift.
- etl.py: where data is loaded from S3 into the staging tables on Redshift and thereafter processed into the analytics tables on Reshift.
- sql_queries.py: where SQL statements, are defined, which are impoted into the two other files.
- README.md: where the processes and the decisions for the ETL pipeline.

## Project Steps

Step 1: Create Table Schemas
- Design of schemas for Fact and Dimension tables.
- Writing SQL 'CREATE' statement for each of the tables in 'sql_queries.py'.
- Writing the logic to connect the created tables to the database in 'create_tables.py'.
- Lauching a redshift cluster and creating an IAM role that has read access to S3 in 'aws_iac.ipyynb'.
- Udating the 'dwh.cfg' file.

Step 2: Build ETL Pipeline
- Implementing logic in 'etl.py' to load data from S3 to staging tables on Redshift.
- Implementing logic in 'etl.py' to load data from staging tables to analytic tables on Redshift.
- Deleting the Redshift cluster when finished in 'aws_iac.ipyynb'.

## Project Datasets

- Song data: 's3://udacity-dend/song_data'
- Log data: 's3://udacity-dend/log_data'

Log data json path: 's3://udacity-dend/log_json_path.json'

## ERD 
see 'Sparkify_2.JPG'

## How to run the Project

- Run the 'aws_iac.ipynb' file to create the cluster on AWS and complete the 'dwh.cfg'.
- Run the 'create_tables.py' file to create the tables in the terminal via 'python create_tables.py'.
- Run the 'etl.py' file to to extract the staging tables from the S3, transform the data, load the data into fact and dimension tables. This is done by executing 'python etl.py' command in the terminal.
