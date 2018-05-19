#!/usr/bin/env python
'''Basic script to list EC2 running instances.
'''
import sys
import  boto3

__author__ = "AWS Training Center"
__copyright__ = "Copyright 2018, AWS Training Center"

#Add your region list here
regions = ['us-west-2']
count=0
#Iterating over all regions 
for regname in regions:
  # Establishing connection
  ec2 = boto3.client("ec2", region_name=regname)
  #Fetching all running instances
  #all_instances = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
  all_instances = ec2.describe_instances()
  #print all_instances
  for res in all_instances["Reservations"] :
    for instance in res["Instances"]:
      count = count+1
      print "%2d. %s %s %s %s\n" %(count, regname, instance["InstanceType"], instance["InstanceId"], instance["State"]["Name"])
