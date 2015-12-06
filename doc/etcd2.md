#  CORE OS TROUBLESHOOTING

## Github samples/deployment


## Debugging using Toolbox

There are almost no tools available, install the Toolbox using 
> /usr/bin/toolbox
To install packages run (for example)
> yum install tcpdump
> yum install telnet
To exit the container, press press ctrl-c three times within 1 second.



## Start/Stop/Restart
sudo systemctl start etcd2.service
sudo systemctl stop etcd2.service
sudo systemctl restart etcd2.service

## Interesting files
* /etc/coreos/update.conf
* /run/systemd/system/etcd2.service.d/20-cloudinit.conf

## Logs
* sudo journalctl -xe
* sudo journalctl -f
* sudo journalctl -u etcd2
* sudo journalctl -u etcd2 -f


