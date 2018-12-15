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

<HomeScreen>:
   name: "HomeScreen"
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
            Button:
               on_release: app.root.current = "ProfileScreen"
               text: 'Profile'
               color: 1, 1, 1, 1
               size_hint: 0.15, 0.075
               background_color: 1,1,1,1
               Image:
                  width: root.width/10
                  height: root.height/20
                  source: '../../Desktop/three-bars.png'
                  center_x: self.parent.center_x
                  center_y: self.parent.center_y
                  allow_stretch: True
            Label:
               text: 'Rams Rewards App' 
               pos: 20, 20
               size: 15, 15
               color: 1, 0, 0, 1
         AnchorLayout:
            anchor_x: 'right'
            anchor_y: 'top'
            padding: root.width/50, root.height/75
            Button:
               size_hint: 0.15, 0.075
               background_color: 1,1,1,1
               Image:
                  width: root.width/10
                  height: root.height/20
                  source: '../../Desktop/camera_icon.png'
                  center_x: self.parent.center_x
                  center_y: self.parent.center_y
                  allow_stretch: True
                  
<ProfileScreen>:
   name: "ProfileScreen"
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
               text: 'Name: ' 
               pos: 0, 20
               size: 15, 15
               color: 1, 0, 0, 1
            
                  
""")

class HomeScreen(Screen):
   pass

class Label(Label):
   pass

class ProfileScreen(Screen):
   pass


sm = ScreenManager()
sm.add_widget(HomeScreen(name='HomeScreen'))
sm.add_widget(ProfileScreen(name='ProfileScreen'))

class RamsRewardsApp(App):

   def build(self):
       Window.size = (300, 570)
       Window.clearcolor = (200, 200, 200, 1)
       return sm

if __name__ == "__main__":
   RamsRewardsApp().run()

