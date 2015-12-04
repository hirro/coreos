# etcd2

# Troubleshooting

## Start/Stop/Restart
sudo systemctl start etcd2.service
sudo systemctl stop etcd2.service
sudo systemctl restart etcd2.service

## Interesting files
* /etc/coreos/update.conf
* /run/systemd/system/etcd2.service.d/20-cloudinit.conf

## Logs
* journalctl -xe
* 