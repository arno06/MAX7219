from max7219 import MAX7219
from max7219 import HeightPixelFont
import time

str="20:23"

canvas = HeightPixelFont.from_string(str)

matrix = MAX7219()
matrix.set_canvas(canvas)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    matrix.close()