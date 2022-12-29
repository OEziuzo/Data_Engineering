## DATA LAKE

### INTRODUCTION
A music streaming startup, Sparkify want to move their data warehouse to a data lake. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

### TASKS
The task is to buld an ETL pipeline that extracts data from S3, processes the data using Spark, and loads back the processed data into S3 as a set of dimensional tabbles in other to allow the analytics team to continue finding insights in what songs their users are listening to.

### FILES
- etl.py: this script reads data from S3, processes the data using spark, and writes them back to S3.
- dl.cfg: this file contains my AWS credentials.
- README.md: the description and discussion on the processes and steps are recorded in this file.
- test.ipynb: a jupyter notebook environment were the codes were tested.

### DATASETS
The datasets available for this projects are all in JSON format and the reside in S3. They are:

- Song data: 's3://udacity-dend/song_data'
- Log data: 's3://udacity-dend/log_data'

### STEPS INVOLVED IN THIS PROJECT
- step1: create an IAM user in the AWS and update 'dl.cfg' with my credentials.
- step2: create a bucket named 'nazo-bucket' in the AWS.
- step3: write the entire ETL process in the 'etl.py' script.
- step4: test the lines of code in the 'etl.py' script in the 'test.ipynb'
- step5: create an EMR cluster to run the entire process.

### HOW TO RUN THE PROJECT
- If you are using windows, use putty to make connection with the created emr cluster.
- creat a file in the new environment and name it etl.py and click 'i'.
- copy the code in the 'etl.py' script from the workspace, paste it in the new file created, click 'Esc' button type ':wq enter'.
- type 'spark-submit etl.py' and click 'Enter'.

### ERD
![Sparkify_datalake](https://user-images.githubusercontent.com/104716831/210006099-2e2485f9-3a93-45b7-bef1-edf257b95d0b.JPG)
