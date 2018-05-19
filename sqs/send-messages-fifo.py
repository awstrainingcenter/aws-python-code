#!/usr/bin/env python
'''Send messages to SQS FIFO queue
Parameters:
1. Queue Name
'''
import sys
import time
import boto3

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

#Get Queue URL
response = sqs.get_queue_url(QueueName=qname)
i=1
while 1:
  print "Sending message %d .." %(i)
  sqs.send_message(QueueUrl=response['QueueUrl'],
                   DelaySeconds=0,
                   MessageBody=('This is message %d' %(i)),
                   MessageGroupId='FIFOQueue',
                   MessageDeduplicationId=str(i)
                  )
  i += 1
  time.sleep(5)
