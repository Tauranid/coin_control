#!/bin/bash
emuchild=$(pgrep -f /opt/retropie/configs/all/autostart.sh)
emuparent=$((0-$(ps -o ppid= -p $emuchild)))
kill -STOP -- $emuparent
vcgencmd display_power 0
