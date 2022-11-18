from random import randint
import time

import pyautogui as pag
from pynput import keyboard, mouse

GAME_TICK = 0.6

class AutoClicker:
    def __init__(self, interval, delta):
        self.interval = interval
        self.delta = delta
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
        jitter = randint(0, self.delta * 10) / 10
        time.sleep(self.interval + jitter)

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

clicker = AutoClicker(0.001, GAME_TICK*3.5)
clicker.run()
