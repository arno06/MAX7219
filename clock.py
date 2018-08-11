#!/usr/bin/env python3

from max7219 import ScreenTicker
from max7219 import set_interval
import sys
import logging
import os
import time

from daemons.prefab import run


class ClockDaemon(run.RunDaemon):

    def __init__(self, pidfile):
        super(ClockDaemon, self).__init__(pidfile=pidfile)
        self.screen = ScreenTicker()
        self.separator = " "

    def run(self):
        self.screen.run()
        self.update_time()

    @set_interval(.5)
    def update_time(self):
        if self.separator == " ":
            self.separator = ":"
        else:
            self.separator = " "
        t = time.localtime()
        hour = str(t.tm_hour)
        if t.tm_hour < 10:
            hour = "0"+hour
        min = str(t.tm_min)
        if t.tm_min<10:
            min = "0"+min
        time_str = hour+self.separator+min
        self.screen.set_string(time_str)

    def close(self):
        self.screen.reset()
        self.stop()


if __name__ == '__main__':
    action = sys.argv[1]
    logfile = os.path.join(os.getcwd(), "clock.log")
    pidfile = os.path.join(os.getcwd(), "clock.pid")

    logging.basicConfig(filename=logfile, level=logging.DEBUG)
    d = ClockDaemon(pidfile=pidfile)

    if action == "start":
        print("starting "+pidfile)
        d.start()
    elif action == "stop":
        print("stop "+pidfile)
        d.close()
    elif action == "restart":
        d.restart()
