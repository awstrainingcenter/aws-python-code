#!/usr/bin/env python
'''Receive messages from SQS FIFO queue
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
queue_url = response['QueueUrl']
while 1:
  response = sqs.receive_message(QueueUrl=queue_url,
                   MaxNumberOfMessages=1,
                   VisibilityTimeout=5,
                   WaitTimeSeconds=0
                  )
  #print response
  if response.has_key('Messages'):
    message = response['Messages'][0]
    receipt_handle = message['ReceiptHandle']
    print(message['Body'])
    sqs.delete_message(QueueUrl=queue_url,
                       ReceiptHandle=receipt_handle
                      )
  else:
   	print 'No message in the queue..'
  time.sleep(5)
