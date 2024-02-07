from teacher.models import *
from .models import *


class DashboardService:
    @staticmethod
    def get_attendance_data(student):
        courses = Course.objects.filter(grade=student.grade)
        attendance_data = []
        for course in courses:
            attendance_qs = Attendance.objects.filter(
                course_class=course, present_student=student
            )

            total_classes = Attendance.objects.filter(course_class=course).count()
            total_present = attendance_qs.count()
            if total_classes > 0:
                attendance_percentage = round((total_present / total_classes) * 100, 1)
            else:
                attendance_percentage = 0
            attendance_data.append(
                {
                    "course_name": course.course_name,
                    "total_present": total_present,
                    "total_classes": total_classes,
                    "attendance_percentage": attendance_percentage,
                }
            )
        return attendance_data

    @staticmethod
    def get_assignment_data(student):
        courses = Course.objects.filter(grade=student.grade)
        assignment_data = []
        for course in courses:
            assignments = Assignment.objects.filter(course=course)

            for assignment in assignments:
                submission_exists = Submit.objects.filter(
                    work=assignment, student=student
                ).exists()
                print(submission_exists)

                assignment_data.append(
                    {
                        "course_name": course.course_name,
                        "assignment_name": assignment.name,
                        "start_date": assignment.start,
                        "end_date": assignment.end,
                        "is_past_done": submission_exists,
                    }
                )
        return assignment_data
