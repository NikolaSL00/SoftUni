class Task:

    def __init__(self, name:str, due_date:str):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def change_name(self, new_name):
        if self.name == new_name:
            return "Name cannot be the same."

        self.name = new_name
        return self.name

    def change_due_date(self, new_date:str):
        if self.due_date == new_date:
            return "Date cannot be the same."

        self.due_date = new_date
        return self.due_date

    def check_is_index_is_valid(self, index:int):
        return 0 <= index < len(self.comments)


    def add_comment(self, comment:str):
        self.comments.append(comment)

    def edit_comment(self, comment_number:int, new_comment:str):
        if self.check_is_index_is_valid(comment_number):
            self.comments[comment_number] = new_comment
            return ', '.join(self.comments)

        return "Cannot find comment."

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"



