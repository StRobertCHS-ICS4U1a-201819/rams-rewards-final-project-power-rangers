# https://kivy.org/doc/stable/guide/lang.html
import kivy

from Student import *

kivy.require('1.9.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.widget import Widget

# You can create your kv code in the Python file
pres = Builder.load_string("""

<ScreenManage>:
   profileScreen: ProfileScreen
   homeScreen: HomeScreen

   Screen: 
      name: "HomeScreen"
      id: HomeScreen
      orientation: 'vertical'
      AnchorLayout:
         AnchorLayout:
            anchor_x: 'left'
            anchor_y: 'top'
            canvas:
               Color:
                  rgba: 51/255, 153/255, 51/255, 1
               Rectangle:
                  pos: 0, root.height-root.height/10
                  size: root.width, root.height/10 
            AnchorLayout:
               anchor_x: 'left'
               anchor_y: 'top'
               padding: root.width/50, root.height/75
               Label:
                  font_size: root.width/12.5
                  size_hint: 1, 1
                  color: 1,1,1,1  
                  text: 'RamsRewards®'
            AnchorLayout:
               anchor_x: 'right'
               anchor_y: 'top'
               Button:
                  on_release:
                     app.root.transition.direction = 'left'
                     app.root.current = 'ProfileScreen'
                  text: 'Profile'
                  color: 1, 1, 1, 1
                  size_hint: 0.15, 0.075
                  background_color: 1,0,0,1  
   Screen:
      name: "ProfileScreen"
      id: ProfileScreen
      orientation: 'vertical'
      AnchorLayout:
         AnchorLayout:
            anchor_x: 'left'
            anchor_y: 'top'
            canvas:
               Color:
                  rgba: 51/255, 153/255, 51/255, 1
               Rectangle:
                  pos: 0, root.height-root.height/10
                  size: root.width, root.height/10 
            AnchorLayout:
               anchor_x: 'left'
               anchor_y: 'top'
               Button:
                  text: 'Back'
                  on_release:
                     app.root.transition.direction = 'right'
                     app.root.current = 'HomeScreen'
                  color: 1, 0, 0, 1
                  size_hint: 0.15, 0.075
                  background_color: 1, 1, 1, 1
            AnchorLayout:
               anchor_x: 'right'
               anchor_y: 'top'
               Button:
                  text: 'Events'
                  on_release:
                     app.root.transition.direction = 'left'
                     app.root.current = 'EventsScreen'
                  color: 1, 0, 0, 1
                  size_hint: 0.15, 0.075
                  background_color: 1,1,1,1
            BoxLayout:
               orientation: "vertical"
               size: root.size
               spacing: 20
               Label: 
                  text: "Barcode"
               Button:
                  text: "Barcode"
                  on_release:
                     app.root.transition.direction = 'up'
                     app.root.current = 'BarcodeScreen'
                  color: 1, 0, 0, 1
                  size_hint: 1, 0.5
                  background_color: 1, 1, 1, 1

   Screen:
      name: "EventsScreen"
      id: EventsScreen
      orientation: 'vertical' 
      AnchorLayout:
         AnchorLayout:
            anchor_x: 'left'
            anchor_y: 'top'
            canvas:
               Color:
                  rgba: 51/255, 153/255, 51/255, 1
               Rectangle:
                  pos: 0, root.height-root.height/10
                  size: root.width, root.height/10 
            AnchorLayout:
               anchor_x: 'left'
               anchor_y: 'top'
               Button:
                  on_release:
                     app.root.transition.direction = 'right'
                     app.root.current = 'ProfileScreen'
                  text: 'Back'
                  color: 1, 0, 0, 1
                  size_hint: 0.15, 0.075
                  background_color: 1, 1, 1, 1
   Screen:
      name: "BarcodeScreen"
      id: BarcodeScreen
      orientation: 'vertical' 
      AnchorLayout:
         AnchorLayout:
            anchor_x: 'left'
            anchor_y: 'top'
            canvas:
               Color:
                  rgba: 51/255, 153/255, 51/255, 1
               Rectangle:
                  pos: 0, root.height-root.height/10
                  size: root.width, root.height/10 
            AnchorLayout:
               anchor_x: 'left'
               anchor_y: 'top'
               Button:
                  on_release:
                     app.root.transition.direction = 'down'
                     app.root.current = 'ProfileScreen'
                  text: 'Back'
                  color: 1, 0, 0, 1
                  size_hint: 0.5, 0.075
                  background_color: 1, 1, 1, 1

""")


class ScreenManage(ScreenManager):
    pass

class HomeScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

class BarcodeScreen(Screen):
    pass


class Screen(Screen):
    pass


class Label(Label):
    pass


sm = ScreenManage()

student1 = Student(500, 'Bob', 'Smith', 'PSU500', '50081756')


class RamsRewardsApp(App):

    def build(self):
        Window.size = (300, 570)
        Window.clearcolor = (200, 200, 200, 1)


        label_app = Label()
        label_app.text = 'Rams Rewards App'
        label_app.size_hint = 1, 1
        label_app.color = 1, 0, 0, 1
        label_app.font_name = 'arial'
        label_app.font_size = 32
        sm.homeScreen.add_widget(label_app)

        label_0 = Label()
        label_0.text = 'Welcome ' + student1.get_name()
        label_0.size_hint = 1, 1.5
        label_0.color = 1, 0, 0, 1
        label_app.font_size = 32
        sm.homeScreen.add_widget(label_0)

        # Student Name
        label_1 = Label()
        label_1.text = 'Name: ' + student1.get_name()
        label_1.size_hint = 1, 1.5
        label_1.color = 1, 0, 0, 1
        sm.profileScreen.add_widget(label_1)

        # Student ID Label
        label_2 = Label()
        label_2.text = 'Student ID: ' + student1.get_student_id()
        label_2.size_hint = 1, 1.3
        label_2.color = 1, 0, 0, 1
        sm.profileScreen.add_widget(label_2)

        # Homeroom Label
        label_3 = Label()
        label_3.text = 'Homeroom: ' + student1.get_homeroom()
        label_3.size_hint = 1, 1.1
        label_3.color = 1, 0, 0, 1
        sm.profileScreen.add_widget(label_3)

        # Points Label
        label_4 = Label()
        label_4.text = 'Rewards Points: ' + str(student1.get_rewards_points())
        label_4.size_hint = 1, 0.9
        label_4.color = 1, 0, 0, 1
        sm.profileScreen.add_widget(label_4)

        return sm


if __name__ == "__main__":
    RamsRewardsApp().run()

