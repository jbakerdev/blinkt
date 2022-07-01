#!/usr/bin/env python
import time
import signal
from sys import exit

try:
    import psutil
except ImportError:
    exit('This script requires the psutil module\nInstall with: sudo apt install python3-psutil')

import blinkt

blinkt.set_clear_on_exit()

def show_graph(v):
    v *= blinkt.NUM_PIXELS

    spectrum = [
        [128,   0, 128],
        [48,   0,  192],
        [0,     0, 255],
        [0,   128, 128],
        [0,   255,   0],
        [255, 192,   0],
        [255,  48,   0],
        [255,   0,   0],
    ]

    for x in range(blinkt.NUM_PIXELS):
        if v < 0:
            r, g, b = 0, 0, 0
        else:
            r, g, b = [int(min(v, 1.0) * c) for c in spectrum[x]]
        pixel = blinkt.NUM_PIXELS - 1 - x
        blinkt.set_pixel(pixel, r, g, b)
        v -= 1

    blinkt.show()


blinkt.set_brightness(0.1)

def clear_leds(signum, frame):
        blinkt.clear()
        blinkt.show()
        exit(0)

signal.signal(signal.SIGTERM, clear_leds)

try:
    while True:
        v = psutil.cpu_percent() / 100.0
        show_graph(v)
        time.sleep(0.01)
except KeyboardInterrupt:
    pass

