class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"Ім'я: {self.name}, Вік: {self.age}")
student = Student('Vasya', 23)
student.info()