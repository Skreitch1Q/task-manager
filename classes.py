"""Классы предметной области для приложения "Менеджер задач"."""

import json


class Task:
    """Описывает отдельную задачу.

    Атрибуты:
        title (str): название задачи.
        description (str): описание задачи.
        due_date (str): срок выполнения в формате ГГГГ-ММ-ДД.
    """

    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date

    def __str__(self):
        return f"{self.title} (до {self.due_date})"


class TaskManager:
    """Управляет списком задач и файловыми операциями.

    Методы: add_task(), delete_task(), save_to_file(), load_from_file().
    """

    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_from_file()

    def add_task(self, task):
        """Добавляет задачу в список и сохраняет изменения в файл."""
        self.tasks.append(task)
        self.save_to_file()

    def delete_task(self, index):
        """Удаляет задачу по индексу и сохраняет изменения в файл."""
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_to_file()

    def save_to_file(self):
        """Сериализует список задач в JSON-файл."""
        data = [
            {
                "title": task.title,
                "description": task.description,
                "due_date": task.due_date,
            }
            for task in self.tasks
        ]
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def load_from_file(self):
        """Загружает задачи из JSON-файла при запуске приложения."""
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.tasks = [
                    Task(item["title"], item["description"], item["due_date"])
                    for item in data
                ]
        except FileNotFoundError:
            self.tasks = []