#!/usr/bin/env python
'''Basic script to terminate EC2 instance.
Parameters:
1. Instance id
'''
import sys
import  boto3

__author__ = "AWS Training Center"
__copyright__ = "Copyright 2018, AWS Training Center"

if len (sys.argv) != 2:
  print "Usage: %s <instance id>" %(sys.argv[0])
  exit(1)

instid = sys.argv[1]
ec2 = boto3.client('ec2') #Mumbai region
response = ec2.terminate_instances(InstanceIds=[instid])
print(response)
