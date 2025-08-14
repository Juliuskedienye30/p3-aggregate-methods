class Enrollment:
    # Class variable to store all enrollments
    all = []

    def __init__(self, student, course, enrollment_date):
        self.student = student
        self.course = course
        self._enrollment_date = enrollment_date
        Enrollment.all.append(self)

    def get_enrollment_date(self):
        return self._enrollment_date

    @classmethod
    def aggregate_enrollments_per_day(cls):
        """
        Counts how many enrollments happened on each date.
        Returns a dictionary: {date: count_of_enrollments}
        """
        enrollment_count = {}
        for enrollment in cls.all:
            date = enrollment.get_enrollment_date().date()
            # Increment count for this date
            enrollment_count[date] = enrollment_count.get(date, 0) + 1
        return enrollment_count


class Student:
    def __init__(self, name):
        self.name = name
        self._enrollments = []  # List of Enrollment objects
        self._grades = {}       # {Enrollment: grade}

    def enroll(self, course, date):
        """
        Enrolls the student into a course on a given date.
        """
        enrollment = Enrollment(self, course, date)
        self._enrollments.append(enrollment)

    def course_count(self):
        """
        Counts the number of courses the student is enrolled in.
        """
        return len(self._enrollments)

    def aggregate_average_grade(self):
        """
        Calculates the student's average grade across all courses.
        """
        if not self._grades:
            return 0  # No grades yet

        total_grades = sum(self._grades.values())
        num_courses = len(self._grades)
        return total_grades / num_courses


# -------------------------
# Example Usage
# -------------------------
from datetime import datetime

# Create students
s1 = Student("Alice")
s2 = Student("Bob")

# Enroll students in courses on certain dates
s1.enroll("Math", datetime(2025, 8, 14))
s1.enroll("Science", datetime(2025, 8, 14))
s2.enroll("History", datetime(2025, 8, 15))

# Add grades
for enrollment in s1._enrollments:
    s1._grades[enrollment] = 90
for enrollment in s2._enrollments:
    s2._grades[enrollment] = 80

# Aggregate methods in action
print(f"{s1.name} is enrolled in {s1.course_count()} courses")
print("Enrollments per day:", Enrollment.aggregate_enrollments_per_day())
print(f"{s1.name}'s average grade: {s1.aggregate_average_grade()}")
