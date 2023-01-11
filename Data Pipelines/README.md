
# Data Pipelines with Airflow
![aws_emr](https://user-images.githubusercontent.com/104716831/211688568-598c0d67-3ec5-45e8-9506-785f2c3aa588.JPG)

## Summary
A music streaming company, Sparkify intends to use Apache Airflow to automate and monitor their data warehouse ETL pipelines. They want a data engineer to create a high grade data pipelines that are dynamic and built from reusable tasks which can be monitored and allow easy backfills. The source data resides in s3 and needs to be processed in Sparkify's data warehouse in Amazon Redshift.

## Needed tools
Python, 
AWS, 
Apache Airflow

## Data sources:
- Log data: s3://udacity-dend/log_data
- Song data: s3://udacity-dend/song_data

## Destinations
- Staging Tables: 
 staging_events,
 staging_songs

- Fact Table:
 songplays

- Dimension Table:
 users,
 songs,
 artists,
 time

## How to run
- Make the neccessary connections between the AWS and Redshift (prerequisite).
- Run the 'create_tables_dag.py' in the Airflow UI.
- Run the 'udac_example_dag.py' in the Airflow UI.
