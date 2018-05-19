#!/usr/bin/env python
'''Send messages to SQS standard queue
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
sqs = boto3.client('sqs')

#Get Queue URL
response = sqs.get_queue_url(QueueName=qname)
i=1
while 1:
  print "Sending message %d .." %(i)
  sqs.send_message(QueueUrl=response['QueueUrl'],
                   DelaySeconds=0,
                   MessageBody=('This is message %d' %(i))
                  )
  i += 1
  time.sleep(5)
