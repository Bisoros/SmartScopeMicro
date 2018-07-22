from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from scripts.smartscope import main as smartscope_micro
from multiprocessing import Process
import os
import sys
import asyncio

class SmartScope(App):
    micro = Button(text = 'Launch SmartScope Micro', pos_hint={'x': 0, 'center_y': .1}, size_hint=(.1, .1))
    micro.bind(on_press = smartscope_micro)
    macro = Button(text = 'Macro', pos_hint={'x': .1, 'center_y': .1}, size_hint=(.1, .1))

    layout = FloatLayout()

    layout.add_widget(micro)
    layout.add_widget(macro)
    def build(self):
        return self.layout

SmartScope().run()
