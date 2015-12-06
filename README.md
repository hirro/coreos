# README.md

# Hardware
I used the following hardware:
* INTEL NUC I5 4250U HASWELL
* 16GB RAM
* 250GB SSD

# Burn Live CD USB on OSX
The CoreOS installation is started after booting from a CentOS7 Live CD. 

 1. Download the Live CD:
          
          > wget http://buildlogs.centos.org/centos/7/isos/x86_64/CentOS-7-livecd-x86_64.iso
 2. Burn it to USB
  1. Convert it to image format

            > hdiutil convert -format UDRW -o centos.img CentOS-7-livecd-x86_64.iso
  2. Find the name of the USB drive
  
          > diskutil list
  3. Unmount USB drive (diskN is the USB drive)

           > diskutil unmountDisk /dev/diskN 
  4. Burn USB
           > sudo dd if=centos.img.dmg of=/dev/rdisk3 bs=1m

# Installation
1. Boot using the USB stick
2. Enable network
3. Remove all partitions on the disk using the "Disks" utility (might need reboot in some cases)
4. Open the terminal
5. Run the commands:
           
           > wget https://github.com/hirro/coreos/archive/master.zip
           > unzip master.zip
           > cd coreos-master/target/$HOST
           > sudo ./install.sh
6. Reboot

# Verify Installation
 1. Check etcd2

           > etcdctl set /message "Hello world"
           Hello world
 2. Check fleet

           > fleetctl list-machines
           MACHINE		IP		METADATA
           14fedb2d...	192.168.1.5	region=se-varmdo
           2b321291...	192.168.1.4	region=se-varmdo
           5db7dbb5...	192.168.1.2	region=se-varmdo
           
           
