import kivy
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen

from Activity import *

kivy.require('1.9.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.button import Button

# You can create your kv code in the Python file
Builder.load_string("""
<Screens>
    box: Box
    Screen:
        name: 'menu'
        BoxLayout:
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
                            pos: 0, root.height - root.height/10
                            size: root.width, root.height/10
                AnchorLayout:
                    padding: 10, 0
                    anchor_x: 'left'
                    anchor_y: 'center' 
                    Button:
                        size_hint: 0.15, 0.8
                        background_color: 1,1,1,1
                        Image:
                            width: root.width/10
                            height: root.height/20
                            source: 'images/three-bars.png'
                            center_x: self.parent.center_x
                            center_y: self.parent.center_y
                            allow_stretch: True
                AnchorLayout:
                    padding: 10, 0
                    anchor_x: 'right'
                    anchor_y: 'center' 
                    Button:
                        size_hint: 0.15, 0.8
                        background_color: 1,1,1,1
                        Image:
                            width: root.width/10
                            height: root.height/20
                            source: 'images/camera_icon.png'
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
                            source: 'images/rams.png'  
                    Label:
                        font_size: root.width/12.5
                        size_hint: 0.3, 1
                        color: 1,1,1,1  
                        markup: True
                        font_name: 'images/FFF_Tusj.ttf'
                        text: 'RamsRewards®'  
            AnchorLayout:  
                size_hint: 1, 0.9
                pos: 0, 10
                ScrollView:
                    GridLayout:
                        padding: 5
                        orientation: "vertical"
                        height: self.minimum_height
                        size_hint_y: None
                        row_default_height: 125
                        cols:1
                        id: Box
                    
    Screen:
        name: 'Screen2'
        
        Button:
            on_press: root.current = 'menu'
        
""")

class Screens(ScreenManager):
    pass

class RamsRewardsApp(App):

    def build(self):

        sm = Screens()

        Window.size = (300, 570)
        Window.clearcolor = (1, 1, 1, .2)

        ball = Activity("ball", 10)
        soccer = Activity("soccer", 10)
        choir = Activity("choir", 10)
        defazingYutes = Activity("defazing yutes", 10)
        gurksingHeadTops = Activity("gurksing headtops", 10)
        singingOCanada = Activity("singing o canada", 10)
        ramofthemonth = Activity("ram of the month", 1000)
        helpingAMandem = Activity("helping a mandem", 10)
        lowingAManATump = Activity("Lowed a man a tump", 10)
        bogeyBreak = Activity("took a bogey break", 10)
        activities = [ball, soccer, choir, defazingYutes, gurksingHeadTops, singingOCanada, ramofthemonth, helpingAMandem, lowingAManATump, bogeyBreak]

        def callback(instance):
            sm.current = 'Screen2'

        for i in activities:
            text = i.get_activity()
            button = Button()
            button.text = text
            button.bind(on_press=callback)
            sm.box.add_widget(button)
        return sm

sample_app = RamsRewardsApp()
sample_app.run()
