# README.md

# Burn Centos Live CD USB
  * Download the Live CD
    > wget http://buildlogs.centos.org/centos/7/isos/x86_64/CentOS-7-livecd-x86_64.iso
  * Convert it to image format
    > hdiutil convert -format UDRW -o centos.img CentOS-7-livecd-x86_64.iso
  * Find the name of the USB drive
    > diskutil list
  * Unmount USB drive (diskN is the USB drive)
    > diskutil unmountDisk /dev/diskN 
  * Burn USB
    > sudo dd if=centos.img.dmg of=/dev/rdisk3 bs=1m

# Installation
* Boot using the USB stick
* Enable network
* Remove all partitions on the disk using the "Disks" utility (might need reboot in some cases)
* Open the terminal
* Run the commands:
  > git clone https://github.com/hirro/coreos.git
  > cd coreos
  > sudo ./coreos-install -d /dev/sda -C stable -c machines.d/${host}.yaml

