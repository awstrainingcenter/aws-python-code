## ec2
This directory contains code for EC2 and related services.
> All the scripts will by default use the AWS Region which you have configured while configuring AWS CLI. In order to run scripts for different AWS region you need to provide extra argument to ec2 connection function call e.g ec2 = boto3.client('ec2', 'ap-south-1')
> The execption handling is not included intentially so as to keep the scripts short and readable. For actual consumption, you should handle exceptions using boto exception class botocore.exceptions
### 1. launch-instance.py
This script launches ec2 instance. Also creates security group and allows ingress access on port 22 (SSH) from your Public IP.
Parameters:
1. AMI ID -> EC2 instance AMI ID in given region
2. SSH key pair -> SSH key pair name which should already exist in your region
```
python launch-instance.py ami-b46f48db demo
```
### 2. terminate-instance.py
This script terminates the ec2 instance.
Parameters:
1. Instance ID -> EC2 instance id that you want to terminate
```
python terminate-instance.py i-09b1dd4fcb497a223
```
### 3. start-stop-instance.py
Starts or Stop given EC2 instance.
Parameters:
1. Action: START or STOP
2. Instance ID
```
python start-stop-instance.py start i-09b1dd4fcb497a223
python start-stop-instance.py stop i-09b1dd4fcb497a223
```
### 4. list-instances.py
List all the instances in us-west-2 region.
> If you want to list instances from all regions, set regions = [] variable with region codes. E.g regions = ['ap-south-1', 'us-east-1', 'us-east-2'] likewise
```
python list-instances.py
```
Output:
```
 1. us-west-2 t2.micro i-0673a858db8363930 running
```
### 5. list-instances-by-state.py
List all the instances in us-west-2 region by instance state (running or stopped)
> If you want to list instances from all regions, set regions = [] variable with region codes. E.g regions = ['ap-south-1', 'us-east-1', 'us-east-2'] likewise
```
python list-instances-by-state.py running
python list-instances-by-state.py stopped
```
Output:
```
 1. us-west-2 t2.micro i-0673a858db8363930 running
```
### 6. list-instances-by-tags.py
List all the instances in us-west-2 region by instance tags.
> If you want to list instances from all regions, set regions = [] variable with region codes. E.g regions = ['ap-south-1', 'us-east-1', 'us-east-2'] likewise
```
python list-instances-by-tags.py Customer=XYZ,Environment=Production
```
Output:
```
 1. us-west-2 t2.micro i-0673a858db8363930 running 
```
