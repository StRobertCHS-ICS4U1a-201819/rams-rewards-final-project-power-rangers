import kivy
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
                    size_hint: 0.15, 0.075
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
                    size_hint: 0.15, 0.075
                    background_color: 1,1,1,1
                    Image:
                        width: root.width/10
                        height: root.height/20
                        source: '../../Desktop/camera_icon.png'
                        center_x: self.parent.center_x
                        center_y: self.parent.center_y
                        allow_stretch: True
""")

class ActivityList(BoxLayout):
    pass


class RamsRewardsApp(App):

    def build(self):
        Window.size = (300, 570)
        Window.clearcolor = (200, 200, 200, 1)
        return ActivityList()

sample_app = RamsRewardsApp()
sample_app.run()