class Student:
    print('Hi!')
    def __init__(self, height = 150):
        self.height = height
oleg = Student() #об'єкт, екземпляр класу
print(oleg.height)
masha = Student(height = 200)
print(masha.height)