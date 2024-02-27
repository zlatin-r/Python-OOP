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
        try:
            task = next(filter(lambda t: t.name == task_name, self.tasks))
        except StopIteration:
            return f"Could not find task with the name {task_name}"

        task.completed = True

        return f"Completed task {task_name}"

    def clean_section(self):
        count_tasks = 0

        for task in self.tasks:
            if task.completed:
                count_tasks += 1
                self.tasks.remove(task)

        return f"Cleared {count_tasks} tasks."

    def view_section(self):
        tasks_with_details = "\n".join(t.details() for t in self.tasks)
        return f"Section {self.name}:\n{tasks_with_details}"
