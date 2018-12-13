class Activity(object):
    def __init__(self, activity, points, color: (int, int, int, int)):
        self.activity = activity
        self.points = points
        self.color = color

    def get_activity(self):
        return self.activity

    def set_activity(self, activity):
        self.activity = activity

    def get_points(self):
        return self.points

    def set_points(self, points):
        self.points = points

    def get_color(self):
        return self.color
