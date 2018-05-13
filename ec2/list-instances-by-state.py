#!/usr/bin/env python
'''Lists EC2 instances by state (running, stopped)
'''
import sys
import  boto3

__author__ = "AWS Training Center"
__copyright__ = "Copyright 2018, AWS Training Center"
__credits__ = []
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Chetan Agrawal"
__email__ = "awstrainingcenter@gmail.com"
__status__ = "Development"


if len(sys.argv) != 2:
  print "Usage: %s <instance state: running or stopped>"
  exit(1)

state = sys.argv[1]
if state not in ['running', 'stopped']:
  print "Error! Invalid state '%s'. Supported state: running, stopped. " %(state)
  exit(1)

#Add your region list here
regions = ['us-west-2']
count=0
#Iterating over all regions 
for regname in regions:
  # Establishing connection
  ec2 = boto3.client("ec2", region_name=regname)
  #Fetching all running instances
  all_instances = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': [state]}])
  #print all_instances
  for res in all_instances["Reservations"] :
    for instance in res["Instances"]:
      count = count+1
      print "%2d. %s %s %s %s\n" %(count, regname, instance["InstanceType"], instance["InstanceId"], instance["State"]["Name"])
