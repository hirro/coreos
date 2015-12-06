Howto

# Change cluster token on running instances (as root)
* systemctl stop etcd2
* Update token
vi /run/systemd/system/etcd2.service.d/20-cloudinit.conf
* rm -r /var/lib/etcd2/
* systemctl daemon-reload && systemctl start etcd2

