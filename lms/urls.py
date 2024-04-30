from django.urls import path
from . import views
from . import admin_views

urlpatterns = [
    path('admin/manage_classes/', admin_views.manage_classes, name='manage_classes'),
    path('admin/manage_subjects/',
         admin_views.manage_subjects, name='manage_subjects'),
    path('admin/send_notification/',
         admin_views.send_notification, name='send_notification'),

    path('teacher/registration/', views.teacher_registration,
         name='teacher_registration'),
    path('teacher/registration/success/', views.teacher_registration_success,
         name='teacher_registration_success'),

    path('admin/assign_classes/<int:teacher_id>/',
         admin_views.assign_classes, name='assign_classes'),
    path('admin/assign_subjects/<int:teacher_id>/',
         admin_views.assign_subjects, name='assign_subjects'),
    path('admin/approve_teacher/<int:teacher_id>/',
         admin_views.approve_teacher, name='approve_teacher'),


    path('teacher/post_announcement/',
         views.post_announcement, name='post_announcement'),
    path('teacher/schedule_lesson/', views.schedule_lesson, name='schedule_lesson'),
    path('teacher/update_weekly_plan/<int:subject_id>/',
         views.update_weekly_plan, name='update_weekly_plan'),
    path('teacher/update_lesson_plan/<int:subject_id>/',
         views.update_lesson_plan, name='update_lesson_plan'),
    path('teacher/approve_student/<int:student_id>/',
         views.approve_student, name='approve_student'),


    path('student/registration/', views.student_registration,
         name='student_registration'),
    path('student/registration/success/', views.student_registration_success,
         name='student_registration_success'),
    path('student/view_subjects/<int:class_id>/',
         views.view_subjects, name='view_subjects'),
    path('student/view_schedule/<int:class_id>/',
         views.view_schedule, name='view_schedule'),
]
