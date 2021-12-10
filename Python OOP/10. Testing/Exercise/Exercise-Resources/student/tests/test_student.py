import unittest
from project.student import Student


class TestStudent(unittest.TestCase):

    def test_student__initialization(self):
        student = Student('name', {'course1': [], 'course2': []})
        student2 = Student('name2')

        self.assertEqual('name', student.name)
        self.assertEqual({'course1': [], 'course2': []}, student.courses)

        self.assertEqual('name2', student2.name)
        self.assertEqual({}, student2.courses)

    def test_enroll__when_course_in_courses__return_course_added_and_extend_notes(self):
        student = Student('name', {'course1': [], 'course2': []})
        result = student.enroll('course1', 'note1')

        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual([x for x in 'note1'], student.courses['course1'])

    def test_enroll__when_course_not_in_courses__return_course_and_notes_added(self):
        student = Student('name', {'course1': [], 'course2': []})

        for idx, command in enumerate(['', 'Y']):
            result = student.enroll(f'course3{idx}', 'n1 n2', command)

            self.assertEqual("Course and course notes have been added.", result)
            self.assertTrue(f'course3{idx}' in student.courses)
            self.assertEqual('n1 n2', student.courses[f'course3{idx}'])

    def test_enroll__without_add_course_notes__should_add_course_without_notes(self):
        student = Student('name', {'course1': [], 'course2': []})

        result = student.enroll('course3', 'n1 n2', "N")

        self.assertEqual(result, "Course has been added.")
        self.assertTrue('course3' in student.courses.keys())
        self.assertEqual([], student.courses['course3'])

    def test_add_notes_to_course__when_course_in_courses(self):
        student = Student('name', {'course1': [], 'course2': []})

        result = student.add_notes('course1', 'new notes')
        expected_result = "Notes have been updated"

        self.assertEqual(expected_result, result)
        self.assertEqual(['new notes'], student.courses['course1'])

    def test_add_notes__when_course_not_found__raise_error(self):
        student = Student('name', {'course1': [], 'course2': []})

        with self.assertRaises(Exception) as context:
            student.add_notes('course3', 'some notes')

        self.assertEqual("Cannot add notes. Course not found.", str(context.exception))
        self.assertTrue('course3' not in student.courses.keys())

    def test_leave_course__when_course_in_courses_return_course_removed(self):
        student = Student('name', {'course1': [], 'course2': []})

        result = student.leave_course('course1')
        self.assertEqual("Course has been removed", result)

    def test_leave_course__when_course_not_in_courses_raise_error(self):
        student = Student('name', {'course1': [], 'course2': []})
        with self.assertRaises(Exception) as context:
            student.leave_course('course4')
        self.assertEqual("Cannot remove course. Course not found.", str(context.exception))


if __name__ == '__main__':
    unittest.main()
