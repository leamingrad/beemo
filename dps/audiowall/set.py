'''
Audiowall Set. Made up of AudiowallPages.
============================================
'''

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.button import Button
from kivy.uix.label import Label
from dps.audiowall.page import AudiowallPage

import globals

class AudiowallSet(BoxLayout):

    def __init__(self, **kwargs):
        super(AudiowallSet, self).__init__(**kwargs)
        self.pages = []

        self._container = BoxLayout(orientation='vertical')
        self.add_widget(self._container)

        self._sm = ScreenManager()
        self._sm.transition = SlideTransition()
        self._sm.transition.duration = 0.3
        self._container.add_widget(self._sm)

        self._buttons = BoxLayout(orientation='horizontal', size_hint=(1,0.25))
        self._container.add_widget(self._buttons)

        self.previous = Button(text='<<')
        self.previous.bind(on_press=self.on_previous)
        self._buttons.add_widget(self.previous)

        self.pages_label = Label(text='Page x of y')
        self._buttons.add_widget(self.pages_label)

        self.next = Button(text='>>')
        self.next.bind(on_press=self.on_next)
        self._buttons.add_widget(self.next)

        self.register_event_type('on_add_page')
        for i in range(0,3,1):
            self.title = 'Screen %i' % i
            self.dispatch('on_add_page')

    def on_add_page(self, *largs):
        screen = Screen()
        screen.name = self.title
        page = AudiowallPage()
        screen.add_widget(page)
        self._sm.add_widget(screen)
        self.pages.append(page)

    def on_previous(self, *largs):
        self._sm.transition.direction = 'right'
        self._sm.current = self._sm.previous()

    def on_next(self, *largs):
        self._sm.transition.direction = 'left'
        self._sm.current = self._sm.next()