#!/bin/bash
emuchild=$(pgrep -f /opt/retropie/configs/all/autostart.sh)
emuparent=$(ps -o ppid= -p $emuchild)
kill -CONT -- -$emuparent
#vcgencmd display_power 1
