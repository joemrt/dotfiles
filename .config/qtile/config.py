# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os

from importlib import reload
import my_widgets
reload(my_widgets)
from my_widgets import CustomExit, update_widget


# shell scripts
os.system('/home/martin/.config/qtile/autostart.sh')

mod = "mod4"
terminal = guess_terminal()




def window_to_other_screen(qtile):
    current_screen = qtile.screens.index(qtile.current_screen)
    other_screen = (current_screen + 1) % 2 
    group_on_other_screen = qtile.screens[other_screen].group.name
    qtile.current_window.togroup(group_on_other_screen)

def focus_to_other_screen(qtile):
    current_screen = qtile.screens.index(qtile.current_screen)
    other_screen = (current_screen + 1) % 2 
    qtile.cmd_to_screen(other_screen)

def custom_dmenu(qtile):
    current_screen = qtile.screens.index(qtile.current_screen)
    qtile.cmd_spawn('dmenu_run -m ' + str(current_screen))


def grow_window(qtile, amount=1, vimdir='h'):
    qtile.current_layout.grow_amount = amount
    if vimdir == 'h':
        qtile.current_layout.cmd_grow_left()
    if vimdir == 'l':
        qtile.current_layout.cmd_grow_right()
    if vimdir == 'j':
        qtile.current_layout.cmd_grow_down()
    if vimdir == 'k':
        qtile.current_layout.cmd_grow_up()


keys = [
    # Switch between windows in current stack pane
    Key([mod], "j", lazy.layout.down(),
        desc="Move focus down in stack pane"),
    Key([mod], "k", lazy.layout.up(),
        desc="Move focus up in stack pane"),
    Key([mod], "h", lazy.layout.left(),
        desc="Move focus up in stack pane"),
    Key([mod], "l", lazy.layout.right(),
        desc="Move focus up in stack pane"),

    # Move windows up or down in current stack
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(),
        desc="Move window down in current stack "),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
    desc="Move window up in current stack "),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
    desc="Move window left in current stack "),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
    desc="Move window right in current stack"),

# Switch window focus to other pane(s) of stack
Key([mod], "c", lazy.layout.next(),
    desc="Switch window focus to other pane(s) of stack"),

# Toggle Floating
Key([mod], "s", lazy.window.toggle_floating(),
    desc="Toggle Floating"),


# Swap panes of split stack
Key([mod, "shift"], "r", lazy.layout.rotate(),
    desc="Swap panes of split stack"),

# Toggle between split and unsplit sides of stack.
# Split = all windows displayed
# Unsplit = 1 window displayed, like Max layout, but still with
# multiple stack panes
Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
    desc="Toggle between split and unsplit sides of stack"),
Key([mod], "Return", lazy.spawn('st -e tmux'), desc="Launch terminal"),

# Toggle between different layouts as defined below
Key([mod], "m", lazy.next_layout(), desc="Toggle between layouts"),
# Toggle fullscreen
Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
Key([mod, 'shift'], "w", lazy.window.kill(), desc="Kill focused window"),

Key([mod, "mod1"], "r", lazy.restart(), desc="Restart qtile"),
Key([mod, "mod1"], "q", lazy.shutdown(), desc="Shutdown qtile"),
Key([mod], "r", lazy.spawncmd(),
    desc="Spawn a command using a prompt widget"),
# custom applications
Key([mod], "d", lazy.function(custom_dmenu)),
Key([mod, "shift"], "n", lazy.spawn('networkmanager_dmenu'),
    desc="launch networmanager_dmenu"),

# Multimedia
Key([], "XF86AudioRaiseVolume", lazy.spawn("/home/martin/bin/increase_volume")),
Key([], "XF86AudioLowerVolume", lazy.spawn("/home/martin/bin/decrease_volume")),
Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute 0 toggle") ),
Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5")),
Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5")),

# Screen Toggling
Key([mod, "mod1"], "period", lazy.function(focus_to_other_screen), desc='Next monitor'),
Key([mod, "mod1"], "comma", lazy.function(window_to_other_screen), desc='Next monitor'),

# Resize Bsp windows
Key([mod, 'mod1'], 'h',  lazy.function(lambda qtile: grow_window(qtile, vimdir='h'))),
Key([mod, 'mod1'], 'j',  lazy.function(lambda qtile: grow_window(qtile, vimdir='j'))),
Key([mod, 'mod1'], 'k',  lazy.function(lambda qtile: grow_window(qtile, vimdir='k'))),
Key([mod, 'mod1'], 'l',  lazy.function(lambda qtile: grow_window(qtile, vimdir='l'))),
Key([mod, 'mod1', 'shift'], 'l',  lazy.function(lambda qtile: grow_window(qtile, amount=-1, vimdir='h'))),
Key([mod, 'mod1', 'shift'], 'k',  lazy.function(lambda qtile: grow_window(qtile, amount=-1, vimdir='j'))),
Key([mod, 'mod1', 'shift'], 'j',  lazy.function(lambda qtile: grow_window(qtile, amount=-1, vimdir='k'))),
Key([mod, 'mod1', 'shift'], 'h',  lazy.function(lambda qtile: grow_window(qtile, amount=-1, vimdir='l'))),
]


groups = [Group(i) for i in "123"]

for i in groups:
    keys.extend([
            # mod1 + letter of group = switch to group
            Key([mod], i.name, lazy.group[i.name].toscreen(),
                    desc="Switch to group {}".format(i.name)),

            # mod1 + shift + letter of group = switch to & move focused window to group
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=False),
                desc="Switch to & move focused window to group {}".format(i.name)),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ])

layouts = [
    # layout.Stack(num_stacks=2),
    # Try more layouts by unleashing below layouts.
    layout.Bsp(margin=15),
    # layout.Columns(),
    # layout.Matrix(margin=15),
    layout.Max(margin=15),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(margin=15),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='Cantarell Regular',
    fontsize=18,
    padding=5,
)
extension_defaults = widget_defaults.copy()



screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.TextBox('', mouse_callbacks={'Button1': lambda qtile: qtile.cmd_spawn('/usr/bin/firefox')}),
                widget.TextBox('', mouse_callbacks={'Button1': lambda qtile: qtile.cmd_spawn('/usr/bin/spotify')}),
                widget.TextBox('', mouse_callbacks={'Button1': lambda qtile: qtile.cmd_spawn('/usr/bin/thunar')}),
                # widget.CurrentLayout(),
                # widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(),
                # widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # widget.TextBox("default config", name="default"),
                # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                # put all remaning widgets on the right
                widget.TextBox(width=bar.STRETCH),
                widget.BatteryIcon(),
                widget.Battery(discharge_char='',
                                charge_char='',
                                format='{char} {percent:2.0%}({hour:d}:{min:02d})'),
                widget.Wlan(interface='wlp3s0', 
                            format=' {essid}', 
                            mouse_callbacks={'Button1': lambda qtile: qtile.cmd_spawn('/usr/bin/nm-connection-editor')}),
                # widget.NetGraph(),
                widget.TextBox('', mouse_callbacks={'Button1': lambda qtile: qtile.cmd_spawn('/usr/bin/pavucontrol')}),
                widget.PulseVolume(),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
                update_widget,
                widget.TextBox('', mouse_callbacks={'Button1': lambda qtile: qtile.cmd_spawn('/usr/bin/blueman-manager')}, foreground='#000099'),
                widget.TextBox('', mouse_callbacks={'Button1': lambda qtile: qtile.cmd_spawn('/usr/bin/timeshift-launcher')}, foreground='#005577'),
                widget.TextBox('', mouse_callbacks={'Button1': lambda qtile: qtile.cmd_spawn('/usr/bin/system-config-printer')}, foreground='#007755'),
                CustomExit(command='systemctl reboot', foreground='#007700'),
                CustomExit(command='systemctl hibernate', foreground='#ff5500'),
                CustomExit(command='systemctl poweroff', foreground='#ff0000'),
                widget.Systray(),
            ],
            33,
            background='#222222',
            opacity=1.00
        ),
    ),
    Screen(
        bottom=bar.Bar(
            [
                # widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(),
                # widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # widget.TextBox("default config", name="default"),
                # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                # put all remaning widgets on the right
                widget.TextBox(width=bar.STRETCH),
                widget.BatteryIcon(),
                widget.Battery(discharge_char='',
                                charge_char='',
                                format='{char} {percent:2.0%}({hour:d}:{min:02d})'),
                widget.Wlan(interface='wlp3s0', 
                            format='  {essid} '),
                # widget.NetGraph(),
                widget.PulseVolume(),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
                widget.Systray(),
            ],
            33,
            background='#222222'
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
