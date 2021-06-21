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

# multihead
HDMI1_status=$(xrandr -q | awk '/^HDMI1/{print $2}')

if [[ $HDMI1_status = 'connected' ]]; then
	xrandr --output eDP1 --auto --output HDMI1 --auto --right-of eDP1 
	~/.fehbg
else
	xrandr --output eDP1 --auto  --output HDMI1 --off
fi
