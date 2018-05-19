#!/usr/bin/env python
'''Basic script to start or stop EC2 instance.
Parameters:
1. Instance id
'''
import sys
import  boto3
from botocore.exceptions import ClientError

__author__ = "AWS Training Center"
__copyright__ = "Copyright 2018, AWS Training Center"

if len(sys.argv) != 3:
  print "Usage: %s <action: start/stop> <instance id>" %(sys.argv[0])
  exit(1)

instance_id = sys.argv[2]
action = sys.argv[1].upper()

ec2 = boto3.client('ec2')

if action == 'START':
  # Do a dryrun first to verify permissions
  try:
    ec2.start_instances(InstanceIds=[instance_id], DryRun=True)
  except ClientError as e:
    if 'DryRunOperation' not in str(e):
      raise
  # Dry run succeeded, run start_instances without dryrun
  try:
    response = ec2.start_instances(InstanceIds=[instance_id], DryRun=False)
    print(response)
  except ClientError as e:
    print(e)
elif action == 'STOP':
  # Do a dryrun first to verify permissions
  try:
    ec2.stop_instances(InstanceIds=[instance_id], DryRun=True)
  except ClientError as e:
    if 'DryRunOperation' not in str(e):
      raise

  # Dry run succeeded, call stop_instances without dryrun
  try:
    response = ec2.stop_instances(InstanceIds=[instance_id], DryRun=False)
    print(response)
  except ClientError as e:
    print(e)
else:
  print "Wrong action: %s" %(action)
  exit(1)

exit(0)
