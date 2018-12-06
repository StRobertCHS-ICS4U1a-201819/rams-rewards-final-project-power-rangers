class Student(object):

    def __init__(self, first_name, last_name, student_id, grade):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__student_id = student_id
        self.__grade = grade
        self.__points = 0

    def get_name(self):
        return self.__last_name + ", " + self.__first_name

    def get_student_id(self):
        return self.__student_id

    def get_grade(self):
        return self.__grade

    def get_points(self):
        return self.__points

    def set_points(self, points):
        self.__points = points