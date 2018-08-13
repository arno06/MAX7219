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
        self.screen.set_mode(ScreenTicker.MODE_LOOP)
        self.screen.set_direction(ScreenTicker.DIRECTION_NEG)
        self.screen.set_string("hello world, what's up ? :)")
        self.runner = []

    def run(self):
        self.runner.append(self.screen.run())

    def close(self):
        for t in self.runner:
            t.set()
        self.screen.reset()
        self.stop()


if __name__ == '__main__':
    action = sys.argv[1]
    logfile = os.path.join(os.getcwd(), "test.log")
    pidfile = os.path.join(os.getcwd(), "test.pid")

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
