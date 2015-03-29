import boto.ec2
import time
from settings import *
from operations import *

doit = True
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
                    sg = instance.groups[0]
                    name = sg.name
                    ##FIXME: Maybe there is another way...
                    groups = conn.get_all_security_groups()
                    for group in groups:
                        if group.name == name:
                            print ('Found the security group: {}!'.format(group.name))
                            ip = get_my_ip()
                            fullrule = '{}/32'.format(ip)
                            for rule in group.rules:
                                if rule.from_port == '8888':
                                    #Dirty but needed
                                    if fullrule.rstrip() == str(rule.grants[0]):
                                        print 'Rule is already in place'
                                        doit = False
                                    else:
                                        print 'I found an old rule for the port: {}. Removing.'.format(rule.grants[0])
                                        group.revoke(rule.ip_protocol, rule.from_port, rule.to_port, rule.grants[0])
                            if doit:
                                print 'Adding {}'.format(ip)
                                group.authorize('tcp', '8888', '8888', '{}/32'.format(ip))
                else:
                    pass
            else:
                print ('Instance not running')
print ('Done')
