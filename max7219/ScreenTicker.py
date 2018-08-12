import math
from .MAX7219 import MAX7219
from .font import HeightPixelFont
from .set_interval import set_interval


class ScreenTicker:
    MODE_STATIC = 0
    MODE_LOOP = 1
    MODE_COME_GO = 2

    ALIGNMENT_START = 0
    ALIGNMENT_END = 1
    ALIGNMENT_CENTER = 2

    def __init__(self, led_count = 8, matrix_count = 4):
        self.dimension = [led_count*matrix_count, led_count]
        self.matrix = MAX7219(0, 0, led_count, matrix_count)
        self.canvas = []
        self.camera_position = [0, 0]
        self.alignments = [ScreenTicker.ALIGNMENT_CENTER, ScreenTicker.ALIGNMENT_START]
        self.modes = [ScreenTicker.MODE_STATIC, ScreenTicker.MODE_STATIC]

    @set_interval(.2)
    def run(self):
        self.update()

    def update(self):
        if self.modes[0] == ScreenTicker.MODE_STATIC:
            if self.alignments[0] == ScreenTicker.ALIGNMENT_CENTER:
                diff = self.dimension[0] - len(self.canvas)
                half = math.ceil(diff / 2)
                for i in range(int(half)):
                    self.canvas.append([0 for k in range(8)])
                    self.canvas.insert(0, [0 for x in range(8)])
                if len(self.canvas) > 32:
                    self.canvas.pop()
        self.matrix.set_canvas(self.canvas)

    def set_string(self, string):
        self.canvas = HeightPixelFont.from_string(string)
        self.update()

    def reset(self):
        self.matrix.close()