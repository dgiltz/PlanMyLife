import datetime
class Day():
    def __init__(self, date : datetime.date):
        match(date.isoweekday):
            case 1:
                self.day_of_week = "Monday"
            case 2:
                self.day_of_week = "Tuesday"
            case 3:
                self.day_of_week = "Wednesday"
            case 4:
                self.day_of_week = "Thursday"
            case 5:
                self.day_of_week = "Friday"
            case 6:
                self.day_of_week = "Saturday"
            case 7:
                self.day_of_week  = "Sunday"

        self.date = date

        self.tasks = []
        self.schedule = None
    
    def add_task(self, task):
        self.tasks.append(task)
        if self.schedule != None:
            self.plan()

    def plan(self):
        if len(self.tasks) == 0:
            print("Day already planned!")
        
        for task in self.tasks:
            pass



class Week():
    def __init__(self, date_start : datetime.date, date_end : datetime.date):
        self.date_start = date_start
        self.date_end = date_end
        self.tasks = []

        self.days = [Day()]

    def add_task(self, task):
        self.tasks.append(task)

    def plan(self):
        if len(self.tasks) == 0:
            print("Week already planned") 

