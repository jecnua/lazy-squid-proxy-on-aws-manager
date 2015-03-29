import boto.ec2
import requests

def stop(conn, id):
    #conn.stop_instances(id)
    pass

def get_my_ip():
    session = requests.session()
    r = session.get('http://checkip.amazonaws.com/')
    ip = r.text
    return ip.rstrip()

def add_my_ip(conn, id):
    pass
