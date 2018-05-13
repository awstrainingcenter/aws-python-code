# aws-python-code
This repository contains the python startup scripts for AWS. Different the AWS service related code is kept under corresponding directories e.g ec2, s3, sqs.
You can use these scripts as starting point to develop on this further as per your requirement. Do contribute to the repo if you happen to write generic scripts using Python and Boto3 for new or existing AWS services.

>Boto3 Documentation: http://boto3.readthedocs.io/en/latest/index.html

## Prerequites
- Install Python 2.7 and Boto3
- Configure AWS credentials
- Test

### Installing Python
Linux RHEL:
```
sudo yum install python27
sudo yum install epel-release
sudo yum install python27-pip
sudo pip install boto3
sudo pip install awscli
```
Linux (Debian):
```
sudo apt-get install python
sudo apt-get install python-setuptools python-dev build-essential
sudo easy_install pip
sudo pip install boto3
sudo pip install awscli
```
Windows:
- Download and install Python Installer [Windows x86_64](https://www.python.org/ftp/python/2.7.15/python-2.7.15.amd64.msi)
- Downalod and install AWSCLI [AWS CLI](https://s3.amazonaws.com/aws-cli/AWSCLI64.msi) 
### Test your setup
From Unix command line or Windows cmd
```
$aws --version
Output:
chetan@chetan-vm:~$ aws --version
aws-cli/1.14.36 Python/2.7.12 Linux/4.13.0-32-generic botocore/1.8.40
(Note: Versions may differ for you)
```
### Configure your AWS credentials
1. Get you AWS programming access/secret keys
Loging to AWS Console -> IAM -> User -> Security Credentials -> Create Access key -> Download CSV
2. Configure credentials
Easiest way to configure your AWS credentials is to setup AWS CLI:
```
$aws configure
AWS Access Key ID [None]: <-- Provide your Access key -->
AWS Secret Access Key [None]: <-- Provide your secret access key -->
Default region name [None]: <--AWS region name e.g ap-south-1 -->
Default output format [None]: json
```
Boto requires your AWS credentials to talk to AWS. Boto looks for  your credentials in some pre-defined locations as below:
- In ~/.aws/credentails or ~/.aws/config file. This is configured automatically if you configure AWS CLI as shown above.
- Environment variables: AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY
For more options, refer this: [Boto credentials configurations](http://boto3.readthedocs.io/en/latest/guide/configuration.html)
