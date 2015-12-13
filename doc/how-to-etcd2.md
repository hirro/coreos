#  ETCD2 TROUBLESHOOTING

## Github samples/deployment


## Debugging using Toolbox

There are almost no tools available, install the Toolbox using 
> /usr/bin/toolbox

To install packages run (for example)
> yum install tcpdump
> yum install telnet

To exit the container, press press ctrl-c three times within 1 second.



## Start/Stop/Restart
* sudo systemctl start etcd2.service
* sudo systemctl stop etcd2.service
* sudo systemctl restart etcd2.service

## Interesting files
* /etc/coreos/update.conf
* /run/systemd/system/etcd2.service.d/20-cloudinit.conf

## Logs
* sudo journalctl -xe
* sudo journalctl -f
* sudo journalctl -u etcd2
* sudo journalctl -u etcd2 -f


## Change cluster token on running instances (as root)
* sudo bash
* systemctl stop etcd2
* Update token
      vi /run/systemd/system/etcd2.service.d/20-cloudinit.conf
      [Service]
      Environment="ETCD_ADVERTISE_CLIENT_URLS=http://192.168.1.3:2379"
      Environment="ETCD_DISCOVERY=https://discovery.etcd.io/6d3fb97343f00c68c3af7d5b97b7b429"
      Environment="ETCD_INITIAL_ADVERTISE_PEER_URLS=http://192.168.1.3:2380"
      Environment="ETCD_LISTEN_CLIENT_URLS=http://0.0.0.0:2379,http://0.0.0.0:4001"
      Environment="ETCD_LISTEN_PEER_URLS=http://192.168.1.3:2380,http://192.168.1.3:7001"
      Environment="ETCD_INITIAL_CLUSTER=unicorn=http://192.168.1.3:2380,epyon=http://192.168.1.4:2380,zero=http://192.168.1.5:2380"
      Environment="ETCD_INITIAL_CLUSTER_STATE=new"

*  rm -r /var/lib/etcd2/*
* systemctl daemon-reload
* systemctl start etcd2
* journalctl -u etcd2 -f

## Manual update of CoreOS
> update_engine_client -update
