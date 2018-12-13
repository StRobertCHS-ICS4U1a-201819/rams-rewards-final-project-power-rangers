import kivy
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen

from Activity import *
from Student import *
kivy.require('1.9.0')

from kivy.effects.dampedscroll import DampedScrollEffect
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

# You can create your kv code in the Python file
Builder.load_string("""
<Screens>
    box: Box
    box2: Box2
    activityName: ActivityName
    Screen:
        name: 'menu'
        BoxLayout:
            padding:5
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
                        padding_bottom: 5
                        spacing: 5
                        orientation: "vertical"
                        height: self.minimum_height
                        size_hint_y: None
                        row_default_height: 125
                        cols:1
                        id: Box
                    
    Screen:
        name: 'Screen2'
        BoxLayout:
            orientation: 'vertical'
            AnchorLayout:
                canvas:
                    Color:
                        rgba: 51/255, 153/255, 51/255, 1
                    Rectangle:
                        pos: 0, root.height - root.height/10
                        size: root.width, root.height/10
                size_hint: 1, 0.1
                BoxLayout:
                    id: ActivityName
                    orientation: 'horizontal'
                    padding: 10
                    spacing: 5
            AnchorLayout:  
                size_hint: 1, 0.9
                pos: 0, 10
                ScrollView:
                    GridLayout:
                        padding: 5
                        spacing: 5
                        orientation: "vertical"
                        height: self.minimum_height
                        size_hint_y: None
                        row_default_height: 125
                        cols:2
                        id: Box2
""")

class Screens(ScreenManager):
    pass

class RamsRewardsApp(App):

    def build(self):

        sm = Screens()

        Window.size = (300, 570)
        Window.clearcolor = (1, 1, 1, .2)

        ball = Activity("ball", 10)
        soccer = Activity("soccer", 20)
        choir = Activity("choir", 5)
        defazingYutes = Activity("defazing yutes", 100)
        gurksingHeadTops = Activity("gurksing headtops", 50)
        singingOCanada = Activity("singing o canada", 200)
        ramofthemonth = Activity("ram of the month", 1000)
        helpingAMandem = Activity("helping a mandem", 70)
        lowingAManATump = Activity("Lowed a man a tump", 90)
        bogeyBreak = Activity("took a bogey break", 80)
        activities = [ball, soccer, choir, defazingYutes, gurksingHeadTops, singingOCanada, ramofthemonth, helpingAMandem, lowingAManATump, bogeyBreak]

        student1 = Student("Timofey", "Hartanovich", 1, 12)
        student2 = Student("Jorge", "Sumi", 2, 12)
        student3 = Student("Jermaine", "Cole", 3, 12)
        student4 = Student("Marshal", "Matthers", 4, 12)
        student5 = Student("Killy", "", 5, 12)
        student6 = Student("Post", "Malone", 6, 12)
        student7 = Student("Trey", "Songz", 7, 12)
        student8 = Student("Kanye", "West", 8, 12)
        students = [student1, student2, student3, student4, student5, student6, student7, student8]

        currentActivity = ball

        def callback(instance):
            global currentActivity
            sm.box2.clear_widgets()
            sm.current = 'Screen2'
            text = instance.text
            for i in activities:
                if i.get_activity() == instance.text:
                    text2 = str(i.get_points()) + " points"
                    currentActivity = i
                    break
            label = Label(text=text, font_name='images/FFF_Tusj.ttf', font_size=sm.width/20, size_hint=(0.75,1))
            label2 = Label(text=text2, font_name='images/FFF_Tusj.ttf', font_size=sm.width/30, size_hint= (0.25, 1))
            sm.activityName.add_widget(label)
            sm.activityName.add_widget(label2)
            print(currentActivity.get_activity())

            for i in students:
                text = 'Points: ' + str(i.get_points())
                label = Label(text=text, font_name='images/FFF_Tusj.ttf', font_size=sm.width / 30, size_hint=(0.25, 1),
                              color=(0, 0, 0, 1))
                button = Button()
                button.text = i.get_name()
                button.background_normal = ''
                button.background_color = .15, .7, .2, .7
                button.size_hint = 0.75, 1
                button.bind(on_press=callback2)
                sm.box2.add_widget(button)
                sm.box2.add_widget(label)

        def callback2(instance):
            global currentActivity
            print (currentActivity.get_activity())
            count = 0
            for i in students:
                if i.get_name() == instance.text:
                    students[count].set_points(students[count].get_points()+currentActivity.get_points())
                    print(students[count].get_points())
                    break
                count += 1
            sm.activityName.clear_widgets()
            sm.current = 'menu'

        for i in activities:
            text = i.get_activity()
            button = Button()
            button.text = text
            button.background_normal = ''
            button.background_color = .15, .7, .2, .7
            button.bind(on_press=callback)
            sm.box.add_widget(button)
        return sm

sample_app = RamsRewardsApp()
sample_app.run()
