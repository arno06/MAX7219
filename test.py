from max7219 import MAX7219
from max7219 import HeightPixelFont
import time

def set_time(matrix, separator):
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
    for i in range(diff):
        canvas.append([0 for k in range(8)])
    matrix.set_canvas(canvas)


matrix = MAX7219()

try:
    while True:
        set_time(matrix, ":")
        time.sleep(1)
        set_time(matrix, " ")
        time.sleep(1)
except KeyboardInterrupt:
    matrix.close()