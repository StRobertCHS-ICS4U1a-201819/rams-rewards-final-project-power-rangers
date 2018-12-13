class Activity(object):
    def __init__(self, activity, points):
        self.activity = activity
        self.points = points

    def get_activity(self):
        return self.activity

    def set_activity(self, activity):
        self.activity = activity

    def get_points(self):
        return self.points

    def set_points(self, points):
        self.points = points
