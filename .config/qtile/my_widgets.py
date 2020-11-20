import os
from libqtile import bar
from libqtile.widget import base, GenPollText

class CustomExit(base._TextBox):
    """
    A button of exiting the running qtile easily. When clicked this button, a countdown
    start. If the button pushed with in the countdown again, the qtile shutdown.
    """
    defaults = [
        ('default_text', ' ', 'A text displayed as a button'),
        ('countdown_format', '{}    ', 'This text is showed when counting down.'),
        ('timer_interval', 1, 'A countdown interval.'),
        ('countdown_start', 5, 'Time to accept the second pushing.'),
    ]

    def __init__(self, widget=bar.CALCULATED, command='systemctl poweroff', **config):
        base._TextBox.__init__(self, '', widget, **config)
        self.add_defaults(CustomExit.defaults)

        self.is_counting = False
        self.text = self.default_text
        self.countdown = self.countdown_start
        self.command = command
        self.__call_later_funcs = []

    def __reset(self):
        self.is_counting = False
        self.countdown = self.countdown_start
        self.text = self.default_text
        for f in self.__call_later_funcs:
            f.cancel()

    def update(self):
        if not self.is_counting:
            return

        self.countdown -= 1
        self.text = self.countdown_format.format(self.countdown)
        func = self.timeout_add(self.timer_interval, self.update)
        self.__call_later_funcs.append(func)
        self.draw()

        if self.countdown == 0:
            self.qtile.cmd_spawn(self.command)
            return

    def button_press(self, x, y, button):

        if not self.is_counting:
            self.is_counting = True
            self.update()
            return
        else:
            self.__reset()
            self.draw()




def updates_count():
    """
    Returns the number of updates as a string
    """
    number_of_updates = int(os.popen('checkupdates | wc -l').read().split('\n')[0])
    return '  %i' % (number_of_updates,)

def open_news(qtile):
    """
    Opens get_arch_news in st
    :param qtile: A qtile object
    """
    qtile.cmd_spawn('st -e get_arch_news &>/dev/null &')


# widget that displays updates and allows to 
# open the arch news feed
update_widget = GenPollText(func=updates_count, mouse_callbacks={'Button1': open_news}, update_interval=60*3)



