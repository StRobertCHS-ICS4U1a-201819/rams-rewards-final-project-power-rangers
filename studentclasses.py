class Student(object):

    def __init__(self, rewards_points, first_name, last_name, homeroom, student_id):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__homeroom = homeroom
        self.__student_id = student_id
        self.__rewards_points = 0

    def set_rewards_points(self, rewards_points):
        self.__rewards_points = rewards_points

    def get_rewards_points(self):
        return self.__rewards_points

    def get_name(self):
        return self.__first_name + self.__last_name

    def set_homeroom(self, homeroom):
        self.__homeroom = homeroom

    def get_homeroom(self):
        return self.__homeroom

    def get_student_id(self):
        return self.__student_id
