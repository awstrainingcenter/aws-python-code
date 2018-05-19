#!/usr/bin/env python
'''Basic script to create SQS FIFO queue
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

sqs = boto3.client('sqs','us-west-2')
response = sqs.create_queue(QueueName=qname, Attributes={'FifoQueue' : 'true' })
print response
