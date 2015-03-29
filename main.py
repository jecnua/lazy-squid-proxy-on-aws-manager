import boto.ec2
from settings import *

print ('Connect')
conn = boto.ec2.connect_to_region("eu-west-1",
    profile_name=local_profile_name)
#statuses = conn.get_all_instance_status()
reservations = conn.get_all_reservations()
#print reservations
instances = reservations[0].instances
#print instances
for instance in instances:
    if instance.tags['Name'] == remote_tag_Name:
        print "{} : {} is {}".format(instance.id,instance.tags['Name'], instance.state)
        if instance.state == 'running':
            print ('want me to restart?')
        else:
            print ('want me to stop?')
