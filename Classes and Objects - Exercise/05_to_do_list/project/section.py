from typing import List
from project.task import Task


class Section:

    def __init__(self, name):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        if task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(task)

        return f"Task {task.details()} is added to the section"

    def complete_task(self, task_name):
        pass
