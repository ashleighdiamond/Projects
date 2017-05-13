# Seattle-Parking
*for more detialed information on how to recreate my project please refer to the powerpoint

Area Observed:
![Alt text](areamap.png?raw=true "Title")

Background:

-Metered Parking
-23 Days of observations
-713,093 transactions
-Daily Revenues:
  -Min: $169.36
  -Max: $137,854.72
-$2.5 million total revenue observed

Why is pricing important?
1) Study demand so can increase transaction rate to be $0.50 higher 
  -Extra $5.6 million in yearly revenue
2) If decide to charge meters on Sundays
  -Only average ½ of normal sales
  -Extra $3 million in yearly revenue
  
DAG:
![Alt text](diagram.png?raw=true "Title")
  
  
Step 1 and 2
I first streamed my transaction data using a python script on an EC2 instance. My data was only updated once a day so I pulled my data daily using cron. I used boto to store my unstructured data into my S3 bucket. 
Files used to recreate: Step2.py, Vagrant_dup, S3 bucket.png, bootstrap copy.sh

![Alt text](S3bucket.png?raw=true "Title")

Step 3
I spun up a cluster using AWS and using spark I created a script that took my data, structured it filtered everything out that I no longer wanted to use and put it into my postgres database in 3NF (Also created using AWS). I have to run this step manually because while doing my twitter project I ran into the problem where I ran out of memory in my database and then my spark job lasted a couple of hours before failing. I do not want that to happen again, especially if it is constantly costing me money. 
Files used to recreate: Ashleigh_Project(2).json, transactions_table.png
 
I got in contact with some of the members who worked with my data in the Seattle government, and they were so nice to give me a CSV file of location information about the parking meters. Because I only had access to one file. I just made a simple python script that took the information from the CSV and put it into my database. 
Files used to recreate: SDOT_Parking…csv, topostgres_singlefile.py, meters_table.png

![Alt text](meters_table.png?raw=true "Title")

Step 4
Then using SQL I created queries that allowed me to better analyze my data.
Files used to recreate: SQL
 
Step 5
Then using my S3 bucket I created a static website gave basic information about transactions and revenues for specific areas/districts of Seattle. 
Files used to recreate: forhtml.py, project.html, datafrompostgress.csv

![Alt text](website.png?raw=true "Title")



