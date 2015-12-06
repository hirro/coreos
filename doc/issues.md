Issues

# Why does only epyon listen on port 2379/2380?
> etcdctl -C http://192.168.1.2:2379,http://192.168.1.4:2379,http://192.168.1.5:2379 member list

# Why is only unicorn having the file /var/lib/etcd2/proxy/cluster?
unicorn:
/var/lib/etcd2/
/var/lib/etcd2/member
/var/lib/etcd2/proxy
/var/lib/etcd2/proxy/cluster
   {"PeerURLs":["http://192.168.1.4:2380","http://192.168.1.5:2380"]}

epyon:
/var/lib/etcd2/
/var/lib/etcd2/member
/var/lib/etcd2/member/snap
/var/lib/etcd2/member/wal
/var/lib/etcd2/member/wal/0000000000000000-0000000000000000.wal

zero:
/var/lib/etcd2/
/var/lib/etcd2/member

