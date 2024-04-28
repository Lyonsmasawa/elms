from django.urls import path
from . import views

urlpatterns = [
    path('student/register/', views.student_register, name='student_register'),
    path('student/login/', views.student_login, name='student_login'),
    path('teacher/register/', views.teacher_register, name='teacher_register'),
    path('teacher/login/', views.teacher_login, name='teacher_login'),
    path('parent/register/', views.parent_register, name='parent_register'),
    path('parent/login/', views.parent_login, name='parent_login'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('teacher/dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('parent/dashboard/', views.parent_dashboard, name='parent_dashboard'),
    path('student/subjects/', views.student_subjects, name='student_subjects'),
    path('student/exams/', views.student_exams, name='student_exams'),
    path('student/assignments/', views.student_assignments,
         name='student_assignments'),
    path('teacher/upload_materials/',
         views.upload_materials, name='upload_materials'),
    path('teacher/weekly_plan/', views.weekly_plan, name='weekly_plan'),
    path('teacher/lesson_plan/', views.lesson_plan, name='lesson_plan'),
    path('teacher/submissions/', views.teacher_submissions,
         name='teacher_submissions'),
    path('teacher/classes/', views.teacher_classes, name='teacher_classes'),
]
