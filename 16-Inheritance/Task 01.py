class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"Name:{self.name}, Age: {self.age}"


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def get_student_details(self):
        return f"Name:{self.name}, Age: {self.age}, Student_id:{self.student_id}"


class Teacher(Person):
    def __init__(self, name, age, salary, employee_id):
        super().__init__(name, age)
        self.salary = salary
        self.employee_id = employee_id

    def get_teacher_details(self):
        return f"Name:{self.name}, Age: {self.age}, employee_id:{self.employee_id}, Salary:{self.salary}"


person = Person("Anna Sebastian", 25)
print(person.get_details())

student = Student("Teena Gustafson", 15, " STD1001")
print(student.get_student_details())

teacher = Teacher("Maria Anderson", 51, 45000, "EMP15")
print(teacher.get_teacher_details())
