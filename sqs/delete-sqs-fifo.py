#!/usr/bin/env python
'''Basic script to delete SQS FIFO queue
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
if not qname.endswith('.fifo'):
  print "Error: FIFO queue name must have suffic .fifo e.g OrderQueue.fifo"
  exit(1)

sqs = boto3.client('sqs', 'us-west-2')
response = sqs.get_queue_url(QueueName=qname)
queue_url = response['QueueUrl']
response = sqs.delete_queue(QueueUrl=queue_url)
print response
