from task import Task

class Section:

    def __init__(self, name:str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task :Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name:str):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f"Completed task {task_name}"

        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        count_of_removed_tasks = 0
        tasks_to_remove = []

        for task in self.tasks:
            if task.completed:
                count_of_removed_tasks += 1
                tasks_to_remove.append(task)

        for task in tasks_to_remove:
            self.tasks.remove(task)

        return f"Cleared {count_of_removed_tasks} tasks."

    def view_section(self):
        result = f'Section {self.name}:'

        for task in self.tasks:
            result += f"\n{task.details()}"

        return result


