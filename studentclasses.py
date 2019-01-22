class Student(object):

    def __init__(self, rewards_points, first_name, last_name, homeroom, student_id, event, second_event, third_event):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__homeroom = homeroom
        self.__student_id = student_id
        self.__rewards_points = rewards_points
        self.__event = event
        self.__second_event = second_event
        self.__third_event = third_event

    def set_rewards_points(self, rewards_points):
        self.__rewards_points = rewards_points

    def get_rewards_points(self):
        return self.__rewards_points

    def get_name(self):
        return self.__first_name + " " + self.__last_name

    def set_homeroom(self, homeroom):
        self.__homeroom = homeroom

    def get_homeroom(self):
        return self.__homeroom

    def get_student_id(self):
        return self.__student_id

    def get_event(self):
        return self.__event

    def get_second_event(self):
        return self.__second_event

    def get_third_event(self):
        return self.__third_event
