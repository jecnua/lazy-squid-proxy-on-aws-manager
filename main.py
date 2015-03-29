import boto.ec2
import time
import requests
from settings import *


def get_my_ip():
    session = requests.session()
    r = session.get('http://checkip.amazonaws.com/')
    ip = r.text
    return ip.rstrip()


def run(region, squid_port='8888'):
    isNecessaryToAdd = True
    conn = boto.ec2.connect_to_region(region, profile_name=local_profile_name)
    reservations = conn.get_all_reservations()
    for reservation in reservations:
        instances = reservation.instances
        for instance in instances:
            if instance.tags[remote_tag_name] == remote_tag_value:
                print "{} : {} is {}".format(
                    instance.id,
                    instance.tags[remote_tag_name],
                    instance.state)
                if instance.state == 'running':
                    input_var = raw_input(
                        'want me to stop(s)/restart(r)/addip(a)?: ')
                    print ("You choose {}!".format(input_var))
                    if input_var == 'a':
                        sg = instance.groups[0]
                        name = sg.name
                        # FIXME: Maybe there is another way...
                        groups = conn.get_all_security_groups()
                        for group in groups:
                            if group.name == name:
                                print (
                                    'Found the security group: {}!'.format(
                                        group.name))
                                ip = get_my_ip()
                                fullrule = '{}/32'.format(ip)
                                for rule in group.rules:
                                    if rule.from_port == squid_port:
                                        # Dirty but needed
                                        if fullrule.rstrip() == str(
                                                rule.grants[0]):
                                            print 'Rule is already in place'
                                            isNecessaryToAdd = False
                                        else:
                                            print 'I found an old rule for the \
                                             port: {}. Removing.'.format(
                                                rule.grants[0])
                                            group.revoke(
                                                rule.ip_protocol,
                                                rule.from_port,
                                                rule.to_port,
                                                rule.grants[0])
                                if isNecessaryToAdd:
                                    print 'Adding {}'.format(ip)
                                    group.authorize(
                                        'tcp',
                                        squid_port,
                                        squid_port,
                                        '{}/32'.format(ip))
                    else:
                        pass
                else:
                    print ('Instance not running')
    print ('Done')

run(aws_region, remote_squid_port)
