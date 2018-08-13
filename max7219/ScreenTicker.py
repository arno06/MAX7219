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

    DIRECTION_POS = 1
    DIRECTION_NEG = -1

    def __init__(self, led_count = 8, matrix_count = 4):
        self.dimension = [led_count*matrix_count, led_count]
        self.matrix = MAX7219(0, 0, led_count, matrix_count)
        self.canvas = []
        self.applied_canvas = []
        self.camera_position = [0, 0]
        self.alignments = [ScreenTicker.ALIGNMENT_CENTER, ScreenTicker.ALIGNMENT_START]
        self.modes = [ScreenTicker.MODE_LOOP, ScreenTicker.MODE_STATIC]
        self.directions = [ScreenTicker.DIRECTION_POS, ScreenTicker.DIRECTION_POS]

    @set_interval(.2)
    def run(self):
        self.update_position()

    def update_canvas(self):
        self.applied_canvas = []
        if self.modes[0] == ScreenTicker.MODE_STATIC:
            self.applied_canvas = self.canvas
            if self.alignments[0] == ScreenTicker.ALIGNMENT_CENTER:
                diff = self.dimension[0] - len(self.canvas)
                half = math.ceil(diff / 2)
                for i in range(int(half)):
                    self.applied_canvas.append([0 for k in range(8)])
                    self.applied_canvas.insert(0, [0 for x in range(8)])
                if len(self.applied_canvas) > self.dimension[0]:
                    self.applied_canvas.pop()
        elif self.modes[0] == ScreenTicker.MODE_LOOP or self.modes[0] == ScreenTicker.MODE_COME_GO:
            i = 0
            while i<self.camera_position[0] and len(self.applied_canvas)<self.dimension[0]:
                self.applied_canvas.append([0 for k in range(8)])
                i = i+1
            k = 0 if self.camera_position[0]>=0 else abs(self.camera_position[0])
            while k<len(self.canvas) and len(self.applied_canvas)<32:
                self.applied_canvas.append(self.canvas[k])
                k = k+1

        while len(self.applied_canvas) < self.dimension[0]:
            self.applied_canvas.append([0 for k in range(8)])
        self.matrix.set_canvas(self.applied_canvas)

    def update_position(self):
        if self.modes[0] == ScreenTicker.MODE_STATIC:
            return
        self.update_canvas()
        self.camera_position[0] += self.directions[0]

        if self.modes[0] == ScreenTicker.MODE_LOOP:
            if self.directions[0] == ScreenTicker.DIRECTION_POS and self.camera_position[0] > self.dimension[0]:
                self.camera_position[0] = -len(self.canvas)
            if self.directions[0] == ScreenTicker.DIRECTION_NEG and self.camera_position[0] < -len(self.canvas):
                self.camera_position[0] = self.dimension[0]
        else:
            if self.directions[0] == ScreenTicker.DIRECTION_POS and self.camera_position[0] >= (self.dimension[0] - len(self.canvas)):
                self.directions[0] = ScreenTicker.DIRECTION_NEG
            elif self.directions[0] == ScreenTicker.DIRECTION_NEG and self.camera_position[0] == 0:
                self.directions[0] = ScreenTicker.DIRECTION_POS

    def set_string(self, string):
        self.canvas = HeightPixelFont.from_string(string)
        self.update_canvas()

    def set_direction(self, direction_x = None, direction_y = None):
        if direction_x is not None:
            self.directions[0] = direction_x
        if direction_y is not None:
            self.directions[1] = direction_y

    def set_mode(self, mode_x = None, mode_y = None):
        if mode_x is not None:
            self.modes[0] = mode_x
        if mode_y is not None:
            self.modes[1] = mode_y

    def set_alignment(self, alignment_x = None, alignment_y = None):
        if alignment_x is not None:
            self.alignments[0] = alignment_x
        if alignment_y is not None:
            self.alignments[1]= alignment_y

    def reset(self):
        self.matrix.close()