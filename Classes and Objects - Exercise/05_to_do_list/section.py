from task import *

class Section:

    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task} is added to the section"
        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name):

