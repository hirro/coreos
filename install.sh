#!/bin/bash 

usage() { echo "Usage: $0 [-h <4host>]" 1>&2; exit 1; }

confirm () {
    # call with a prompt string or use a default
    read -r -p "${1:-Are you sure? [y/N]} " response
    case $response in
        [yY][eE][sS]|[yY]) 
            true
            ;;
        *)
            false
            ;;
    esac
}

declare -A machines

machines["c0:3f:d5:6b:d0:f5"]="epyon"
machines["c0:3f:d5:62:b9:6c"]="unicorn"
machines["c0:3f:d5:6b:dc:79"]="zero"

# Only works for the Centos 7 Live CD
echo "Retrieving MAC address"
mac=`cat /sys/class/net/eno1/address`
echo "MAC address is: $mac"
host=${machines["$mac"]}
file="machines.d/${host}.yaml"
echo "Using cloud-config $file"

if [ -f "$file" ]; then
    wget -q https://raw.github.com/coreos/init/master/bin/coreos-install
    chmod +x coreos-install
    echo "sudo ./coreos-install -d /dev/sda -C stable -c $file"
    confirm && sudo ./coreos-install -d /dev/sda -C stable -c $file
else
    echo "Machine not configured $file"
fi
