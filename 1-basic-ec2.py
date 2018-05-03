import  boto3
from urllib2 import urlopen


ec2 = boto3.client('ec2')
my_ip = urlopen('http://ip.42.pl/raw').read()  #Get your PublicIP
#Create Security Group
sg = ec2.create_security_group(Description='Created using boto3',
                                               GroupName='MySG-1')
ec2.authorize_security_group_ingress(CidrIp="%s/32" %(my_ip),
                                                        FromPort=22, #ssh port
                                                        GroupId=sg['GroupId'],
                                                        IpProtocol='tcp',
                                                        ToPort=22)
#Launch instance
response = ec2.run_instances(ImageId='ami-b46f48db', #Mumbai region
                             InstanceType='t2.micro',
                             KeyName='demo1',
                             SecurityGroupIds=[sg['GroupId']],
                             MaxCount=1,
                             MinCount=1
                             )
print(response)
