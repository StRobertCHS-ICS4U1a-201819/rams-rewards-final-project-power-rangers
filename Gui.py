# It is common practice to create your own custom
# widgets so base widgets aren't effected

import kivy

kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.widget import Widget


class CustomWidget(Widget):
    pass


class GuiApp(App):
    def build(self):
        return CustomWidget()


customWidget = GuiApp()

customWidget.run()a`