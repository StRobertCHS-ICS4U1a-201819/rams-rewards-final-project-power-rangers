<<<<<<< HEAD
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
=======
import kivy
from kivy.properties import ObjectProperty

import Activity

kivy.require('1.9.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.button import Button

# You can create your kv code in the Python file
Builder.load_string("""
<ActivityList>
    box: Box
    orientation: 'vertical'
    AnchorLayout:
        size_hint: 1, 0.1
        AnchorLayout:
            anchor_x: 'left'
            anchor_y: 'top' 
            canvas:
                Color:
                    rgba: 51/255, 153/255, 51/255, 1
                Rectangle:
                    pos: 0, root.height-root.height/10
                    size: root.width, root.height
            AnchorLayout:
                anchor_x: 'left'
                anchor_y: 'top' 
                padding: root.width/50, root.height/75
                Button:
                    size_hint: 0.15, 1
                    background_color: 1,1,1,1
                    Image:
                        width: root.width/10
                        height: root.height/20
                        source: '../../Desktop/three-bars.png'
                        center_x: self.parent.center_x
                        center_y: self.parent.center_y
                        allow_stretch: True
            AnchorLayout:
                anchor_x: 'right'
                anchor_y: 'top' 
                padding: root.width/50, root.height/75
                Button:
                    size_hint: 0.15, 1
                    background_color: 1,1,1,1
                    Image:
                        width: root.width/10
                        height: root.height/20
                        source: '../../Desktop/camera_icon.png'
                        center_x: self.parent.center_x
                        center_y: self.parent.center_y
                        allow_stretch: True
            AnchorLayout:
                anchor_x: 'center'
                anchor_y: 'top' 
                padding: root.width/50, root.height/75
                canvas:
                    Color:
                        rgba: 1, 1, 1, .6
                    Rectangle:
                        pos: root.width/2-root.width/5, root.height-root.height/10
                        size: root.width/2.5, root.height/10
                        source: '../../Desktop/rams.png'  
                Label:
                    font_size: 46
                    size_hint: 0.3, 1
                    color: 1,1,1,1  
                    markup: True
                    text: '[font=FFF_Tusj]RamsRewards®'    
    ScrollView:
        GridLayout:
            row_default_height: '20dp'
            padding: 20, 5
            cols: 1
            rows: 100
            id: Box

""")

class ActivityList(BoxLayout):
    pass


class RamsRewardsApp(App):

    def build(self):
        Window.size = (300, 570)
        Window.clearcolor = (1, 1, 1, .2)
        g = ActivityList()
        for i in range(100):
           g.box.add_widget(Button())
        return g

sample_app = RamsRewardsApp()
sample_app.run()
