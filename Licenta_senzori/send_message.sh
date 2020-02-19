#!/bin/sh

#gsmsendsms -d /dev/ttyACM0 -b 9600  0746247689 "test send sms cu gsmsendsms"
gsmsendsms -d /dev/ttyACM0 -b 9600  $1 "$2"
sleep 1