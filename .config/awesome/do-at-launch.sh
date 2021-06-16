#!/bin/bash
# notifications
dunst &
# transparency
picom -b



# turn of DPMS
xset s off -dpms




# automount devices
udiskie --no-notify &

# start DE own services
systemctl --user start check-battery.timer

# polkit agent for authentification
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &>/dev/null &

