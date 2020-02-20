#!/bin/sh

#gsmsendsms -d /dev/ttyACM0 -b 9600  0740262875 "test send sms cu gsmsendsms"
gsmsendsms -d /dev/ttyACM0 -b 9600  $1 "$2"
sleep 1
