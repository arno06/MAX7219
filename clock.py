#!/usr/bin/env python3

from max7219 import MAX7219
from max7219 import HeightPixelFont
import sys
import logging
import os
import time
import math

from daemons.prefab import run


class ClockDaemon(run.RunDaemon):

    def __init__(self, pidfile):
        super(ClockDaemon, self).__init__(pidfile=pidfile)
        self.matrix = MAX7219()

    def run(self):
        while True:
            self.set_time(":")
            time.sleep(0.5)
            self.set_time(" ")
            time.sleep(0.5)

    def set_time(self, separator):
        t = time.localtime()
        hour = str(t.tm_hour)
        if t.tm_hour < 10:
            hour = "0"+hour
        min = str(t.tm_min)
        if t.tm_min<10:
            min = "0"+min
        time_str = hour+separator+min
        canvas = HeightPixelFont.from_string(time_str)
        diff = 32 - len(canvas)
        half = math.ceil(diff/2)
        for i in range(int(half)):
            canvas.append([0 for k in range(8)])
            canvas.insert(0, [0 for x in range(8)])
        if len(canvas)>32:
            canvas.pop()
        self.matrix.set_canvas(canvas)

    def close(self):
        self.matrix.close()
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
