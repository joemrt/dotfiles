#!/bin/bash
# notifications
dunst &
# transparency
picom -b



# turn of DPMS
xset s off -dpms




# automount devices
udiskie --no-notify &

# network manager
nm-applet &

# polkit agent for authentification
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &>/dev/null &

