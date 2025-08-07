# lib/enrollment.py
from datetime import datetime

class Student:
    def __init__(self, name):
        self.name = name
        self._enrollments = []
        self._grades = {}

    def enroll(self, course, grade=None):
        if isinstance(course, Course):
            enrollment = Enrollment(self, course)
            self._enrollments.append(enrollment)
            course.add_enrollment(enrollment)
            if grade is not None:
                self._grades[enrollment] = grade
        else:
            raise TypeError("course must be an instance of Course")

    def course_count(self):
        return len(self._enrollments)

    def aggregate_average_grade(self):
        total_grades = sum(self._grades.values())
        return total_grades / len(self._grades) if self._grades else 0

class Course:
    def __init__(self, title):
        self.title = title
        self._enrollments = []

    def add_enrollment(self, enrollment):
        self._enrollments.append(enrollment)

class Enrollment:
    all = []

    def __init__(self, student, course):
        self.student = student
        self.course = course
        self._enrollment_date = datetime.now()
        Enrollment.all.append(self)

    def get_enrollment_date(self):
        return self._enrollment_date

    @classmethod
    def aggregate_enrollments_per_day(cls):
        count = {}
        for e in cls.all:
            date = e.get_enrollment_date().date()
            count[date] = count.get(date, 0) + 1
        return count
