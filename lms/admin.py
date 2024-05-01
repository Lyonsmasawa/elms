from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Class)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Announcement)
admin.site.register(Schedule)
admin.site.register(Notification)
admin.site.register(Assignment)
admin.site.register(Exam)
admin.site.register(ExamSubmission)
admin.site.register(Material)