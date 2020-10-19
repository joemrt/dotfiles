#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
# PS1='[\u@\h \W]\$ '
PS1="\[\033[0;35m\][\u \W]\$ \[\033[0m\]"

source /usr/share/fzf/key-bindings.bash

# compressing pdfs
function laura_compress()
{
	gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook -dNOPAUSE -dQUIET -dBATCH -sOutputFile=${1%\.pdf}-small.pdf $1
}

# manual mounting with access rights to martin
function mmount()
{
	sudo mount -o gid=martin,fmask=113,dmask=002 $1 $2
}

function reflclean()
{
	sudo reflector -c Germany -a 6 --sort rate --save /etc/pacman.d/mirrorlist
}

function multiheadright()
{
	xrandr --output eDP1 --auto --output HDMI1 --auto --right-of eDP1 && bgdice
}

function multiheadleft()
{
	xrandr --output eDP1 --auto --output HDMI1 --auto --left-of eDP1 && bgdice
}

function multiheadoff()
{
	# put them together
	xrandr --output eDP1 --auto --output HDMI1 --auto 
	# delete second output
	xrandr --output eDP1 --auto 
}

alias gitdot='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'

set -o vi
bind '"jk":vi-movement-mode'

alias vim=nvim
export VISUAL=nvim
export EDITOR=nvim
export LESS='--mouse --wheel-lines=3 -R'

archey3
