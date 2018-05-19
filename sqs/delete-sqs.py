#!/usr/bin/env python
'''Basic script to delete SQS standard queue
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
response = sqs.get_queue_url(QueueName=qname)
queue_url = response['QueueUrl']
response = sqs.delete_queue(QueueUrl=queue_url)
print response
