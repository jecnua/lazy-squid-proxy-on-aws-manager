import boto.ec2
from settings import *
from operations import *

conn = boto.ec2.connect_to_region('eu-west-1',profile_name=local_profile_name)
#statuses = conn.get_all_instance_status()
reservations = conn.get_all_reservations()
#instances = reservations[0].instances
for reservation in reservations:
    instances = reservation.instances
    for instance in instances:
        if instance.tags['Name'] == remote_tag_Name:
            print "{} : {} is {}".format(instance.id,instance.tags['Name'], instance.state)
            if instance.state == 'running':
                input_var = raw_input('want me to stop(s)/restart(r)/addip(a)?: ')
                print ("You choose {}!".format(input_var))
                if input_var == 'a':
                    pass
                else:
                    pass
            else:
                print ('Instance not running')
print ('Done')
