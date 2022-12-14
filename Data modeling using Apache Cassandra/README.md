# Data_Engineering with Apache Cassandra

## Overview
A startup called Sparkify wants to analyze the data they have been collecting on songs and user activity on their new music streaming app.

## Task
They aim of this project is 
- to create an Apache Cassandra database which can create queries on song play data to answer analytic questions.
- to create an ETL pipeline that transfers data from a set of CSV files within a directory to create a streamlined CSV file to model and insert data into Apache Cassandra  using Python.

## Datasets
The datasets for this project is event_data.

## Project Steps

Step 1: Modeling NoSQL database or Apache Cassandra daatabase
- Writing 'CREATE KEYSPACE', 'SET KEYSPACE' statements.
- Writing 'CREATE' statements for the tables.
- Using 'INSERT' statementto load the tables created.

Step 2: Build ETL Pipeline
- Writing ETL logic fo iterate through each event file in 'event_data' to process and create a new CSV file in Python.
