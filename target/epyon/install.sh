#!/bin/bash 
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

wget -q https://raw.github.com/coreos/init/master/bin/coreos-install
chmod +x coreos-install
echo "sudo ./coreos-install -d /dev/sda -C stable -c cloud-config.yaml"
confirm && sudo ./coreos-install -d /dev/sda -C stable -c cloud-config.yaml
