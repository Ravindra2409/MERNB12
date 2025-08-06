import boto3

ec2 = boto3.resource('ec2')
client = boto3.client('ec2')
elb = boto3.client('elbv2')

# Constants — customize these:
VPC_ID = 'VPCRavindraB12 ID'  
SG_ID = 'SGRavindraB12'    #  
TG_ARN = 'arn:aws:elasticloadbalancing:...:targetgroup/TGRavindraB12/...'
LB_ARN = 'arn:aws:elasticloadbalancing:...:loadbalancer/app/LBRavindraB12/...'
AMI_ID = 'ami123'  
KEY_NAME = 'B12RavindraKeyEC2.pem'

# Launch EC2 instances (2 backend, 2 frontend)
def launch_instances(role_tag):
    instances = ec2.create_instances(
        ImageId=AMI_ID,
        MinCount=2,
        MaxCount=2,
        InstanceType='t2.micro',
        KeyName=KEY_NAME,
        SecurityGroupIds=[SG_ID],
        SubnetId='subnet-xxxxxxxx',  
        UserData=f'''#!/bin/bash
        apt-get update -y
        apt-get install -y nodejs npm git
        git clone https://github.com/your-org/{role_tag}-app.git /opt/{role_tag}
        cd /opt/{role_tag}
        npm install
        npm start &''',
        TagSpecifications=[{
            'ResourceType': 'instance',
            'Tags': [{'Key': 'Name', 'Value': f'{role_tag}-server'}]
        }]
    )
    return [i.id for i in instances]

# Register instances to Target Group
def attach_to_target_group(instance_ids):
    for instance_id in instance_ids:
        elb.register_targets(
            TargetGroupArn=TG_ARN,
            Targets=[{'Id': instance_id, 'Port': 3000}]
        )

# Setup Flow
backend_ids = launch_instances('backend')
frontend_ids = launch_instances('frontend')

attach_to_target_group(backend_ids)

print("✅ EC2 instances launched and backend targets registered to LBRavindraB12")