class Task():
    def __init__(self, duration, priority, name, description, done_by):
        self.duration = duration
        self.priority = priority
        self.name = name
        self.description = description
        self.done_by = done_by

        self.completed = False
        self.subtasks = []

    def complete(self):
        self.completed = True

    def move_due_date(self, new_date):
        self.done_by = new_date

    def add_sub_task(self, sub_task):
        self.subtasks.append(sub_task)

    def sort_sub_tasks(self):
        def merge(list1 : list, list2 : list):
            merged = []
            num_elements = len(list1) + len(list2)
            for i in range(num_elements):
                if len(list1) != 0 and len(list1) != 0:
                    if list1[0].priority <= list2[0].priority:
                        merged[i] = list1.pop(0)
                    else:
                        merged[i] = list2.pop(0)
                else:
                    if len(list1) != 0:
                        merged[i:-1] = list1
                        break
                    else:
                        merged[i:-1] = list2
                        break
            return merged

        def split(list : list):
            switch = False
            list1 = [] ; list2 = []
            while(len(list) != 0):
                if switch:
                    list1.append(list.pop(0))
                else:
                    list2.append(list.pop(0))
                
                switch = not switch

            return list1, list2
    
        def merge_sort(list):
            if len(list) == 1:
                return list
            
            list1, list2 = split(list)
            sorted = merge(merge_sort(list1), merge_sort(list2))
            return sorted
        
        self.subtasks = merge_sort(self.subtasks)

    def split_task(self, intervals):
        new_tasks = []
        num_new = (self.duration // intervals) + 1
        dur = self.duration
        time = self.duration // intervals
        if self.subtasks.is_empty():
            for i in range(num_new):
                new = Task(time if dur - time > 0 else dur, 
                           self.priority, self.name + "_" + str(i), 
                           description="Part 1: \n" + self.description,
                           done_by = self.done_by
                           )
                dur -= time
                new_tasks.append(new)
            
            self.subtasks = new_tasks
        else:
            for sub_task in self.subtasks:
                if sub_task.duration > intervals:
                    sub_task.split_task(intervals)



class Studying(Task):
    def __init__(self, duration, priority, subject, course, frequency):
        super(duration, priority)
        self.subject = subject
        self.course = course

        self.frequency = frequency

        self.comprehension = 0.0
    
class Work(Task):
    def __init__(self, duration, priority, attachments, due_date):
        super(duration, priority)
        self.due = due_date 
        self.attachments = attachments

class Exercise(Task):
    def __init__(self, duration, priority, type, description, frequency):
        super().__init__(duration, priority, type, description, None)
        self.type = type
        self.frequency = frequency

class Cleaning(Task):
    def __init__(self, duration, priority, description, done_by, area, frequency):
        super().__init__(duration, priority, "Cleaning " + area, description, done_by)
        self.area = area
        self.frequency = frequency

class Project(Task):
    def __init__(self, duration, priority, name, description, done_by, stage, folder, languages):
        super().__init__(duration, priority, name, description, done_by)
        self.stage = stage
        self.folder = folder
        self.languages = languages

class Leisure(Task):
    def __init__(self, duration, name, description):
        super().__init__(duration, 0, name, description, None)
        
