class Task:
    def __init__(self, task_id, title, done=False):
        self.id = task_id
        self.title = title
        self.done = done

    def to_dict(self):
        return {"id": self.id, "title": self.title, "done": self.done}


class TaskStore:
    def __init__(self):
        self._tasks = {}
        self._next_id = 1

    def add(self, title):
        task = Task(self._next_id, title)
        self._tasks[task.id] = task
        self._next_id += 1
        return task

    def get(self, task_id):
        return self._tasks.get(task_id)

    def all(self):
        return list(self._tasks.values())

    def delete(self, task_id):
        return self._tasks.pop(task_id, None) is not None