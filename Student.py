class Student(object):

    def __init__(self, first_name, last_name, student_id, grade):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__student_id = student_id
        self.__grade = grade
        self.__points = 0
        self.__history = []
        self.__selected = False

    def get_name(self):
        if self.__first_name == "":
            return self.__last_name
        elif self.__last_name == "":
            return self.__first_name

        return self.__last_name + ", " + self.__first_name

    def get_id(self):
        return self.__student_id

    def get_grade(self):
        return self.__grade

    def get_points(self):
        return self.__points

    def set_points(self, points):
        self.__points = points

    def select(self, select):
        self.__selected = select

    def isSelected(self):
        return self.__selected

    def log_event(self, activity):
        self.__history.append(activity)

    def get_history(self):
        string = ""
        for i in range(len(self.__history)-1, -1, -1):
            string += str(i+1) + ". "
            string += self.__history[i]
            string += '\n'
        return string