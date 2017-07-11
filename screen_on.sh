#!/bin/bash
vcgencmd display_power 1
sleep 3
emuchild=$(pgrep -f /opt/retropie/configs/all/autostart.sh)
emuparent=$((0-$(ps -o ppid= -p $emuchild)))
kill -CONT -- $emuparent
