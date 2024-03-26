from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student = Student("Test1")
        self.student_with_courses = Student("Test2", {"math": ["x + y = z"]})

    def test_init(self):
        self.assertEqual("Test1", self.student.name)
        self.assertEqual("Test2", self.student_with_courses.name)

        self.assertEqual({}, self.student.courses)
        self.assertEqual({"math": ["x + y = z"]}, self.student_with_courses.courses)

    def test_enroll_in_the_same_course_appends_new_notes(self):
        result = self.student_with_courses.enroll(
            "math", ["1 + 2 = 3", "3 + 4 = 7"])

        self.assertEqual("Course already added. Notes have been updated.", result)

        self.assertEqual(
            ["x + y = z", "1 + 2 = 3", "3 + 4 = 7"],
            self.student_with_courses.courses["math"])

    def


if __name__ == '__main__':
    main()
