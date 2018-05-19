#!/usr/bin/env python
'''Basic script to create SQS standard queue
Parameters:
1. Queue Name
'''
import sys
import  boto3

__author__ = "AWS Training Center"
__copyright__ = "Copyright 2018, AWS Training Center"

if len (sys.argv) != 2:
  print "Usage: %s <Queue Name>" %(sys.argv[0])
  exit(1)

qname = sys.argv[1]
sqs = boto3.client('sqs')
response = sqs.create_queue(QueueName=qname)
print response
