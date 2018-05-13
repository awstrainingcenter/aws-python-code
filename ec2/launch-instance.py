#!/usr/bin/env python
'''Basic script to launch EC2 instance. Also creates security group and allows ingress rule for port 22 (SSH) from your IP address
Parameters:
1. AMI ID for given region
2. SSH key pair name (must exist already)
'''
import sys
import  boto3
from urllib2 import urlopen

__author__ = "AWS Training Center"
__copyright__ = "Copyright 2018, AWS Training Center"
__credits__ = []
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Chetan Agrawal"
__email__ = "awstrainingcenter@gmail.com"
__status__ = "Development"

if len (sys.argv) != 3:
  print "Usage: %s <ami-id> <ssh key pair name>" %(sys.argv[0])
  exit(1)

ami_id = sys.argv[1]
key_pair = sys.argv[2]

ec2 = boto3.client('ec2')
my_ip = urlopen('http://ip.42.pl/raw').read()#Get your PublicIP
#Create Security Group
sg = ec2.create_security_group(Description='Created using boto3',
                               GroupName='MySecurityGroup-1')
ec2.authorize_security_group_ingress(CidrIp="%s/32" %(my_ip),
                                     FromPort=22, #ssh port
                                     GroupId=sg['GroupId'],
                                     IpProtocol='tcp',
                                     ToPort=22)
#Launch instance
response = ec2.run_instances(ImageId=ami_id,
                             InstanceType='t2.micro',
                             KeyName=key_pair,
                             SecurityGroupIds=[sg['GroupId']],
                             MaxCount=1,
                             MinCount=1
                             )
print(response)
