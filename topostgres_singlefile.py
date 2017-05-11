from os.path import expanduser
import psycopg2
import yaml
"""This file is meant to load lines from a CSV file and import them into postgress,
I did not use Spark because this was the only file of its type. It just gives info
about the meter locations"""
credentials = yaml.load(open(expanduser('~/api_cred1.yml')))

conn = psycopg2.connect(**credentials['rds'])  # connect to postgres
cur = conn.cursor()
count = 0# create a cursor

with open ("SDOT_Parking_Pay_Stations.csv", "r") as f:
    data=f.readlines()
    new=[]
    count=0
    for each in data:
        new=each.split(",")
        objectid=None
        try :
            objectid=int(new[0])

        except:
            pass
        if objectid:
            objectid=int(new[0])
            shape=new[1]
            compkey=int(new[2])
            elmntkey=int(new[3])
            segkey=int(new[4])
            unitid=new[5]
            unitdesc=new[6]
            reciept_nbr=new[7]
            pandd_nbr=int(new[8])
            paidarea=new[9]
            subarea=new[10]
            side=new[11]
            cur.execute("INSERT INTO meters (objectid, shape, compkey,elmntkey,segkey, unitid, unitdesc, reciept_nbr, pandd_nbr, paidarea, subarea, side) VALUES (%s, %s, %s,%s,%s, %s, %s,%s,%s, %s, %s, %s)", (objectid, shape, compkey,elmntkey,segkey, unitid, unitdesc, reciept_nbr, pandd_nbr, paidarea, subarea, side))
            count+=1
            if count>100:
                conn.commit()
                count=0
    conn.commit()
    conn.close()
