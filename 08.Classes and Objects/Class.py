class Class:
    students = []
    grades = []
    _students_count = 22

    def __init__(self, name):
        self.name = name

    def add_student(self, name: str, grade: float):
        if len(self.students) + 1 < self._students_count:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        return sum(self.grades) / len(self.students)

    def __repr__(self):
        return f"The students in {self.name}: {', '.join(self.students)}.\n"\
               f" Average grade: {a_class.get_average_grade():.2f}"


a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)