# lazy-squid-proxy-on-aws-manager
A lazy approach to manage my squid proxy

##Requirements

- [boto](https://pypi.python.org/pypi/boto)
- A working AWS ec2 account
- Create a file called settings.py and fill the data like showed in
settings.py.dist

##Use case

- My dynamic ip changed

##CON

- You should only have one instance with that tag name
- Only one IP on port 8888
- Only port 8888
