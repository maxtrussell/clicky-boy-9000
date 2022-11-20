from random import randint
import time

import numpy as np
import pyautogui as pag
from pynput import keyboard, mouse

GAME_TICK = 0.6

class AutoClicker:
    def __init__(self, mean, std):
        self.mean = mean
        self.std = std
        self.suspend = False

    def run(self):
        self.begin()

        print('Running, press space to pause/unpause')
        kb = keyboard.Listener(on_press=self.on_kb)
        kb.start()

        while True:
            self.sleep()
            if not self.suspend:
                pag.click()

    def sleep(self):
        samples = np.random.normal(self.mean, self.std, 1)
        time.sleep(samples[0])

    def on_kb(self, key):
        if key == keyboard.Key.space:
            self.suspend = not self.suspend
            print(f'{self.suspend=}')

    def begin(self):
        print('Please click to begin')
        with mouse.Events() as events:
            for event in events:
                if isinstance(event, mouse.Events.Click):
                    break

clicker = AutoClicker(0.6, 0.1)
clicker.run()
