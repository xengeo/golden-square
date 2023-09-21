class Tasks:

    def __init__(self):
        self._task_list = []

    def add_task(self, task:str):
        if type(task) != str or task == '':
            raise Exception("Input must be a string")
        
        if task in self._task_list:
            return "Task already exists"
        
        self._task_list.append(task)

    def list_tasks(self):
        if len(self._task_list) > 0:
            return self._task_list
        return "Your list is empty"
    
    def mark_complete(self, task):
        
        if type(task) != str or task == '':
            raise Exception("Input is invalid")
        
        if task in self._task_list:
            self._task_list.remove(task)
            return f"{task} completed" 
        
        return "Task is not in the task list"
    