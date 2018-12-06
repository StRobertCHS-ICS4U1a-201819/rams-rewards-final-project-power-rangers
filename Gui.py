import kivy

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.app import runTouchApp
from kivy.uix.popup import Popup


class Rams_Rewards(App):


    def build(self):
        activities = GridLayout(cols=1, rows=5)
        activities.add_widget(Button(text="hi"))
        activities.add_widget(Button(text="hi"))
        activities.add_widget(Button(text="hi"))
        activities.add_widget(Button(text="hi"))
        activities.add_widget(Button(text="hi"))
        Window.size = (400, 600)
        Window.clearcolor = (200,200,200,1)
        return activities

rams_rewards = Rams_Rewards()
rams_rewards.run()