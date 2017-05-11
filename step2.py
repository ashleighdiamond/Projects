#! /usr/bin/python3
import os
import sys
import boto
import yaml
import urllib
from datetime import date, timedelta, datetime

"""DataId,MeterCode,TransactionId,TransactionDateTime,Amount,UserNumber,PaymentMean
,PaidDuration,ElementKey,TransactionYear,TransactionMonth,Vendor"""

"This file is how I made my requests and stored the unstructured data in my S3 bucket, it was orig called please.py"

def putS3(filename, content_str):
    conn = boto.connect_s3()
    bucket = conn.get_bucket('ashprojectbucket')
    file = bucket.new_key(filename)
    file.set_contents_from_string(content_str)

if __name__ == '__main__':
    fromdt = (date.today()-timedelta(5)).strftime('%m%d%Y')
    todt = (date.today()-timedelta(3)).strftime('%m%d%Y')
    filedt = datetime.now().strftime('%m%d%Y%H%M')
    url = "http://web6.seattle.gov/SDOT/wapiParkingStudy/api/ParkingTransaction?from=" + fromdt + "&to=" + todt
    response = (urllib.request.urlopen(url)).read()
    print(filedt)
    #putS3(filedt, response)
