from django.utils import timezone
from .models import Assignment, Attendance
from django.core.exceptions import ObjectDoesNotExist


class DashboardService:
    @staticmethod
    def get_assignment_submission_status(teacher):
        assignments = Assignment.objects.filter(teacher=teacher)
        assignment_submission_status = []

        for assignment in assignments:
            total_students = assignment.course.grade.student.count()
            submitted_students = assignment.submission.count()

            assignment_submission_status.append(
                {
                    "assignment_name": assignment.name,
                    "total_students": total_students,
                    "submitted_students": submitted_students,
                    "course_name": assignment.course.course_name,
                    "due_date": assignment.end,
                }
            )
        return assignment_submission_status

    @staticmethod
    def get_total_present_students(teacher):
        courses = teacher.course.all()
        total_present_students = []

        for course in courses:
            try:
                present_students = Attendance.objects.get(
                    course_class=course, date=timezone.now().date()
                ).present_student.count()
            except ObjectDoesNotExist:
                present_students = 0

            total_present_students.append(
                {
                    "course_name": course.course_name,
                    "course_grade": course.grade.level,
                    "total_students": course.grade.student.count(),
                    "present_students": present_students,
                }
            )
        return total_present_students
