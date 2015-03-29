# lazy-squid-proxy-on-aws-manager

A lazy approach to manage my squid proxy. My ip change a lot and every time I
have to login in AWS and add my new ip to the sg (removing the old one). I could
use aws-cli, but I should input and write down ids and stuff.

This script does all once you configure it. Faster and easier.

##Requirements

- [boto](https://pypi.python.org/pypi/boto)
- A working AWS ec2 account
- A running squid proxy server with the right tag and one sg on it
- Create a file called settings.py and fill the data like showed in
settings.py.dist

##Use case

My dynamic ip changed and I need to use my proxy server for **totally legal**
reasons. :D

##PRO

It works!

##TODO

- You need to have only have one instance with that tag identifier
- Only one IP on given port
- Only IPv4
