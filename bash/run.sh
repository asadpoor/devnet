#!/bin/bash

# Set term type if needed (vt100 for Nexus)
#export TERM=vt00

# Rotate logs
timestamp=`date +%Y%m%d%H%M`
 
# Archive last config log
logfile=config.log
newlogfile=$logfile.$timestamp
cp $logfile $newlogfile

# Get SSH and enable passwords
 echo -n "Enter your SSH username "
 read -s -e username
 echo -ne '\n'
 echo -n "Enter your SSH password "
 read -s -e password
 echo -ne '\n'
 echo -n "Enter your enable password "
 read -s -e enable
 echo -ne '\n'

# Pull in device list and passwords
for device in `cat devices.txt`; do
 ./config.exp $device $username $password $enable ;
 done
