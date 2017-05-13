# Seattle-Parking
*for more detialed information on how to recreate my project please refer to the powerpoint

Area Observed:
![Alt text](areamap.png?raw=true "Title")

#Background:

-Metered Parking
-23 Days of observations
-713,093 transactions
-Daily Revenues:
  -Min: $169.36
  -Max: $137,854.72
-$2.5 million total revenue observed

#Why is pricing important?
1) Study demand so can increase transaction rate to be $0.50 higher 
  -Extra $5.6 million in yearly revenue
2) If decide to charge meters on Sundays
  -Only average ½ of normal sales
  -Extra $3 million in yearly revenue
  
#DAG:
![Alt text](diagram.png?raw=true "Title")
  
  
##Step 1 and 2
I first streamed my transaction data using a python script on an EC2 instance. My data was only updated once a day so I pulled my data daily using cron. I used boto to store my unstructured data into my S3 bucket. 
Files used to recreate: Step2.py, Vagrant_dup, S3 bucket.png, bootstrap copy.sh

![Alt text](S3buck.png?raw=true "Title")

##Step 3
I spun up a cluster using AWS and using spark I created a script that took my data, structured it filtered everything out that I no longer wanted to use and put it into my postgres database in 3NF (Also created using AWS). I have to run this step manually because while doing my twitter project I ran into the problem where I ran out of memory in my database and then my spark job lasted a couple of hours before failing. I do not want that to happen again, especially if it is constantly costing me money. 
Files used to recreate: Ashleigh_Project(2).json, transactions_table.png
 
I got in contact with some of the members who worked with my data in the Seattle government, and they were so nice to give me a CSV file of location information about the parking meters. Because I only had access to one file. I just made a simple python script that took the information from the CSV and put it into my database. 
Files used to recreate: SDOT_Parking…csv, topostgres_singlefile.py, meters_table.png

![Alt text](meters_table.png?raw=true "Title")

##Step 4
Then using SQL I created queries that allowed me to better analyze my data.
Files used to recreate: SQL
 
##Step 5
Then using my S3 bucket I created a static website gave basic information about transactions and revenues for specific areas/districts of Seattle. 
Files used to recreate: forhtml.py, project.html, datafrompostgress.csv
https://s3.amazonaws.com/ashprojectbucket/project.html

![Alt text](website.png?raw=true "Title")

#My Projects 8 Desired properties of a Big Data system:

##Robustness and fault tolerance:

Strength: In the past I have had issues with Spark inserting data into my database, because my database ran out of memory. In order to address this issue I decided to manually run Spark. 

Weakness: My project is reliant on AWS. If AWS goes down, I will not be able to collect data, store data, access my database, or view my static webpage. 

##Low latency reads and updates:

Strength: The type of data that I am using does not require low latency. In fact price changes for metered parking in the City of Seattle have around a months notice. Also price changes are not based on a day, a week, or even a months worth of data. The City of Seattle has been collecting data since 2012 and their price changes are based off of historical information. This is another reason why I decided that it would be best for me to manually run my Spark jobs because I need data ready when I plan on using it. And if I was not going to check on my project weekly or even monthly I did not want to have my database get overloaded. 

Possible Improvements: Currently I am using SQL to obtain statistics and insights about my data. However the size of my data is slightly over 100MB, once the size of my data increases I will need to use Spark SQL to get information about my statistics in a timely manner. 

##Scalability:

Strength: AWS allows me to store as much data as I want for a reasonable cost. I am able to scale up with AWS.

Possible Improvements: Once the size of my data increases I should consider using Spark data frames or Spark SQL for faster results.  

##Generalization:

Strength: My project allows me to successfully stream parking data from the City of Seattle. 

Weakness: Currently my project does not allow me to stream data that is not structured like the data from the City of Seattles Parking Transaction API. 

##Extensibility:

Strength: If necessary it is easy for me to create a new table to store more information, or to add new features to current tables. For example while creating my project, I contacted the City of Seattle and asked them for meter location information. Once they gave me the information I made a new table and a python script to add the additional information. This took less than an hour of my time.
Ad hoc queries:

Strength: Currently it is very easy for me to use SQL on my data. PostgreSQL even has querying functionality. The insights that I mentioned above were all discovered using SQL.

##Minimal maintenance:

Strength: As I mentioned earlier my data does not require low latency. I choose to manually run Spark on my data because I need to be aware of how much data I am inserting into my database at a time so that I do not run out of storage. Also my data collection and storage processes are automated.

Possible Improvement: Ideally I would be able to have a database that never runs out of storage, and therefore not have to manually run Spark. 

##Debuggability:

Strength: Because I am manually running Spark, I am able to detect where my issue is. Is my bug due to having issues with my clusters (constantly terminating), obtaining my data (well be able to tell by the size of my bucket, in the future maybe I could send a weekly email report on the status of how much data that was collected), if my data is formatted in a different way (if there are a minimal amount of rows entered into my database then after a couple of months then I could see the latest date entered and look up a more recent file) etc. 

Possible Improvement: I can always improve on my debugging skills. Also it would be nice to have a weekly email report on the status of how much data I have collected over the past week. 


