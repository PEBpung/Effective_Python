from collections import defaultdict

class Student:
    def __init__(self):
        self.data = defaultdict(set)
    def add(self, name, obj):
        self.data[name].add(obj)

student = Student()

names = ['진수', '영희', '영희', '영희', '지우', '지우']
objs  = ['수학', '과학', '수학', '영어', '영어', '수학']

for i, (name, obj) in enumerate(zip(names, objs)):
    student.add(name, obj)

print(student.data)

