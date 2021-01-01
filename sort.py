arr = "This is a test string from Andrew".split()

sort_01 = sorted(arr, key=str.lower)

print(sort_01)


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))

    def weighted_grade(self):
        return 'CBA'.index(self.grade) / float(self.age)

student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'C', 12),
    Student('dave', 'B', 10),
]
sort02 = sorted(
    student_objects,
    key=lambda student: student.age,
    reverse=False,
)

sort03 = sorted(student_objects,
       key=lambda student: student.grade)

print(sort03)
