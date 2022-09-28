from datetime import timedelta
import datetime
import boto3
import json
import sys
import os

try:
    hour = sys.argv[1]
    if len(sys.argv) != 2:
        print("Insufficient arguments")
        sys.exit()
except IndexError:
    #default time
    hour = os.environ.get('CUSTOM_HOUR', '1000')

access_id= os.environ.get('ACCESS_ID')
access_key= os.environ.get('ACCESS_KEY')

# Create IAM client
iam = boto3.client('iam', aws_access_key_id=access_id, aws_secret_access_key=access_key)
response = iam.list_users()

users = []
for user in response['Users']:
    users.append(user['UserName'])
paginator = iam.get_paginator('list_access_keys')

time = datetime.datetime.now()
today = datetime.datetime(time.year, time.month, time.day, time.hour, time.minute, time.second,tzinfo=datetime.timezone.utc)

users_name = []
access_key = []
create_date = []
hours_left = []
days_left = []
for user in users:
    for response in paginator.paginate(UserName=user):
        for x in response['AccessKeyMetadata']:
            
            day_left = today - x['CreateDate']
            hour_left = day_left.total_seconds()//3600
            day_left = day_left.days
            if hour_left > float(hour):
                users_name.append(x['UserName'])
                access_key.append(x['AccessKeyId'])
                create_date.append(x['CreateDate'])
                hours_left.append(hour_left)
                days_left.append(day_left)

f = open("user_list.csv", "w")
for i in range(len(users)):
    f.write("계정명 , "+users_name[i]+" 액세스키 , "+access_key[i]+" 생성된시간 , "+str(create_date[i])+" 경과한일수 , "+str(days_left[i])+" 경과한시간 ,"+str(hours_left[i])+"\n")
f.close()
