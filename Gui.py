import kivy
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen

from Activity import *
from Student import *
kivy.require('1.9.0')

from kivy.uix.checkbox import CheckBox
from kivy.app import App
from kivy.lang import Builder

from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView

global sm

# You can create your kv code in the Python file
Builder.load_string("""
<Screens>
    box: Box
    box2: Box2
    activityName: ActivityName
    createActivity: CreateActivity
    studentInformation: StudentInformation
    actNameInput: ActNameInput
    actPointInput: ActPointInput
    Screen:
        name: 'menu'
        BoxLayout:
            padding_top:5
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
                        on_press: root.three_click()
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
                        on_press: root.cam_click()
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
                size_hint: 1, 0.15
                id: CreateActivity
            AnchorLayout:  
                size_hint: 1, 0.75
                pos: 0, 10
                ScrollView:
                    GridLayout:
                        padding: 3
                        spacing: 5
                        orientation: "vertical"
                        height: self.minimum_height
                        size_hint_y: None
                        row_default_height: 125
                        cols:2
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
                        cols:3
                        id: Box2
    Screen:
        name: 'StudentInfo'
        AnchorLayout:
            canvas:
                Color:
                    rgba: 51/255, 153/255, 51/255, 1
                Rectangle:
                    pos: 0, 0
                    size: root.width, root.height
            BoxLayout:
                id: StudentInformation
                orientation: 'vertical'
                padding: 10
                spacing: 5                    
    Screen:
        name: 'Settings'
        
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
                    padding: 15, 0
                    anchor_x: 'right'
                    anchor_y: 'top' 
                    Button:
                        text: '->'
                        size_hint: 0.15, 0.09
                        background_color: 1,1,1,1
                        on_press: 
                            root.back_click()
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
    Screen:
        name: 'camera'
        
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
                    padding: 15, 0
                    anchor_x: 'left'
                    anchor_y: 'top' 
                    Button:
                        text: '<-'
                        size_hint: 0.15, 0.09
                        background_color: 1,1,1,1
                        on_press: 
                            root.back_click2()
    Screen:
        name: 'activityCreate'
        
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
                    padding: 15, 0
                    anchor_x: 'left'
                    anchor_y: 'top' 
                    Button:
                        text: '<-'
                        size_hint: 0.15, 0.09
                        background_color: 1,1,1,1
                        on_press: 
                            root.back_click2()
            Label:
                color: 0,0,0,1
                text: 'Activity Name'
            TextInput:
                id: ActNameInput
            Label:
                color: 0,0,0,1
                text: 'Activity Points'
            TextInput:
                id: ActPointInput
            Button:
                text: 'Create'

<ScrollableLabel>:
    Label:
        size_hint_y: None
        height: self.texture_size[1]
        text_size: self.width, None
        text: root.text
""")


class Screens(ScreenManager):
    def three_click(self):
        sm.transition.direction = 'right'
        sm.current = 'Settings'
    pass

    def back_click(self):
        sm.transition.direction = 'left'
        sm.current = 'menu'
    pass

    def cam_click(self):
        sm.transition.direction = 'left'
        sm.current = 'camera'
    pass

    def back_click2(self):
        sm.transition.direction = 'right'
        sm.current = 'menu'
    pass

    def award_new_activity(self):
        global currentActivity
        tempActivity = Activity(sm.actNameInput.text, int(sm.actPointsInput.text))
        currentActivity = tempActivity
        

class ScrollableLabel(ScrollView):
    text = StringProperty('')

class RamsRewardsApp(App):

    def build(self):
        global sm
        sm = Screens()

        Window.size = (300, 570)
        Window.clearcolor = (1, 1, 1, .2)

        ball = Activity("ball", 10)
        soccer = Activity("soccer", 20)
        choir = Activity("choir", 5)
        lead_prayer = Activity("lead prayer", 100)
        help_prepare = Activity("help with assembly", 50)
        singing_o_canada = Activity("singing o canada", 200)
        ram_of_the_month = Activity("ram of the month", 1000)
        assisting_others = Activity("helping a student", 70)
        helpful_student = Activity("giving a student a pencil", 90)
        character_award = Activity("character award", 80)
        activities = [ball, soccer, choir, lead_prayer, help_prepare, singing_o_canada, ram_of_the_month,
                      assisting_others, helpful_student, character_award]

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
        currentStudent = student1

        def refreshCallBack(text1):
            global currentActivity
            global currentStudent
            global lastScreen
            sm.activityName.clear_widgets()
            sm.box2.clear_widgets()
            sm.transition.direction = 'left'
            sm.current = 'Screen2'
            text = text1
            for i in students:
                currentStudent = i
                currentStudent.select(False)
            for i in activities:
                if i.get_activity() == text:
                    text2 = str(i.get_points()) + " points"
                    currentActivity = i
                    break

            label = Label(text=text, font_name='images/FFF_Tusj.ttf', font_size=sm.width / 20, size_hint=(0.7, 1))
            label2 = Label(text=text2, font_name='images/FFF_Tusj.ttf', font_size=sm.width / 30, size_hint=(0.2, 1))
            add_points_button = Button(text="+", font_name='images/FFF_Tusj.ttf', font_size=sm.width / 30, size_hint=(0.05, 1))
            add_points_button.bind(on_press=on_click)
            back_button = Button(text="<-", font_name='images/FFF_Tusj.ttf', font_size=sm.width / 25,
                                       size_hint=(0.05, 1))
            add_points_button.bind(on_press=on_click)
            back_button.bind(on_press=backButtonCallBack)
            sm.activityName.add_widget(back_button)
            sm.activityName.add_widget(label)
            sm.activityName.add_widget(label2)
            sm.activityName.add_widget(add_points_button)

            for i in students:
                currentStudent = i
                text = 'Points: ' + str(i.get_points())
                label = Label(text=text, font_name='images/FFF_Tusj.ttf', font_size=sm.width / 30, size_hint=(0.2, 1),
                              color=(0, 0, 0, 1))
                checkbox = CheckBox(size_hint=(0.1, 1))
                checkbox.text = i.get_name()
                checkbox.bind(active=on_checkbox_active)
                student_button = Button()
                student_button.text = i.get_name()
                student_button.background_normal = ''
                student_button.background_color = .15, .7, .2, .7
                student_button.size_hint = 0.7, 1
                student_button.bind(on_press=callback2)
                sm.box2.add_widget(student_button)
                sm.box2.add_widget(label)
                sm.box2.add_widget(checkbox)

        def callback(instance):
            refreshCallBack(instance.text)

        def backButtonCallBack(instance):
            sm.activityName.clear_widgets()
            sm.transition.direction = 'right'
            sm.current = 'menu'

        def newActivityCallBack(instance):
            sm.transition.direction = 'left'
            sm.current = 'activityCreate'

        def backStudentButtonCallBack(instance):
            global currentActivity
            text = currentActivity.get_activity()
            sm.activityName.clear_widgets()
            refreshCallBack(text)
            sm.transition.direction = 'right'
            sm.current = 'Screen2'

        def on_checkbox_active(checkbox, value):
            global currentStudent
            select = False
            for i in students:
                if i.get_name() == checkbox.text:
                    currentStudent = i
            if value:
                select = True
            currentStudent.select(select)

        def on_click(instance):
            global currentStudent
            global currentActivity
            for i in students:
                if i.isSelected():
                    currentStudent = i
                    currentStudent.set_points(i.get_points()+currentActivity.get_points())
                    currentStudent.log_event(currentActivity.get_activity())
            refreshCallBack(currentActivity.get_activity())


        def callback2(instance):
            global currentActivity
            global currentStudent
            global lastScreen
            sm.current = 'StudentInfo'
            sm.studentInformation.clear_widgets()
            for i in students:
                if i.get_name() == instance.text:
                    currentStudent = i
                    break
            nameLabel = Label(text="Name: " + currentStudent.get_name())
            idLabel = Label(text="Student ID: " + str(currentStudent.get_id()))
            gradeLabel = Label(text="Grade: " + str(currentStudent.get_grade()))
            pointsLabel = Label(text="Points: " + str(currentStudent.get_points()))
            activitiesLabel = ScrollableLabel(text="    Activities:\n" + str(currentStudent.get_history()))
            button = Button(text="Back")
            button.bind(on_press=backStudentButtonCallBack)
            sm.studentInformation.add_widget(button)
            sm.studentInformation.add_widget(nameLabel)
            sm.studentInformation.add_widget(idLabel)
            sm.studentInformation.add_widget(gradeLabel)
            sm.studentInformation.add_widget(pointsLabel)
            sm.studentInformation.add_widget(activitiesLabel)

        newActivityButton = Button()
        newActivityButton.text= "Custom Activity"
        newActivityButton.bind(on_press=newActivityCallBack)
        sm.createActivity.add_widget(newActivityButton)
        for i in activities:
            text = i.get_activity()
            text1 = str(i.get_points())
            button = Button()
            button.text = text
            label = Label()
            label.text = "Points: " + text1
            label.color = 0, 0, 0, 1
            label.size_hint = 0.3, 1
            button.background_normal = ''
            button.background_color = .15, .7, .2, .7
            button.size_hint = 0.7, 1
            button.bind(on_press=callback)
            sm.box.add_widget(button)
            sm.box.add_widget(label)

        return sm


sample_app = RamsRewardsApp()
sample_app.run()