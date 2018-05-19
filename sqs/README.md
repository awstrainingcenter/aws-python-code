## ec2
This directory contains code for SQS operations
> All Standard Queue scripts will by default use the AWS Region which you have configured while configuring AWS CLI. In order to run scripts for different AWS region you need to provide extra argument to sqs connection function call e.g sqs = boto3.client('sqs', 'ap-south-1')
> For FIFO queue, default region is Oregon (us-west-2) as its not supported in Mumbai region.
> The execption handling is not included intentially so as to keep the scripts short and readable. For actual consumption, you should handle exceptions using boto exception class botocore.exceptions
### 1. create-sqs.py
This script create SQS standard queue.
Parameters:
1. Queue Name 
```
python create-sqs.py OrderQueue
```
### 2. send-messages.py
This script continuously sends messages to standard queue every 5 seconds interval
Parameters:
1. Queue Name
```
python send-messages.py OrderQueue
Output:
Sending message 1 ..
Sending message 2 ..
Sending message 3 ..
```
### 3. receive-messages.py
Receives messages from the standard Queue
Parameters:
1. Queue Name
```
python receive-messages.py OrderQueue
Output:
This is message 2
This is message 1
This is message 3
```
### 4. create-sqs-fifo.py
This script create SQS FIFO queue.
Parameters:
1. Queue Name (Ex: OrderQueue.fifo)
```
python create-sqs-fifo.py OrderQueue.fifo
```
### 2. send-messages-fifo.py
This script continuously sends messages to fifo queue every 5 seconds interval
Parameters:
1. Queue Name
```
python send-messages-fifo.py OrderQueue.fifo
Output:
Sending message 1 ..
Sending message 2 ..
Sending message 3 ..
```
### 3. receive-messages-fifo.py
Receives messages from the fifo Queue
Parameters:
1. Queue Name
```
python receive-messages-fifo.py OrderQueue.fifo
Output:
This is message 2
This is message 1
This is message 3
```
