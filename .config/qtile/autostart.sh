#!/bin/bash
xrandr --output eDP1 --auto --output HDMI1 --auto --right-of eDP1 
# automount devices
udiskie --no-notify &
picom -b
bgdice
dunst &
# start DE own services
systemctl --user start check-battery.timer
# turn of DPMS
xset s off -dpms

# polkit agent for authentification
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &>/dev/null &
