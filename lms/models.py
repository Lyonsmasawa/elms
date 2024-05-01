from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    # Add related_name arguments to resolve the clash
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='custom_user_groups'  # Example related_name
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_permissions'  # Example related_name
    )
    
    def __str__(self):
        return self.is_approved


class Class(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    weekly_plan = models.TextField(blank=True, null=True)
    lesson_plan = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name


class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    classes_taught = models.ManyToManyField(Class)
    subjects_taught = models.ManyToManyField(Subject)
    
    def __str__(self):
        return self.user


class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    class_enrolled = models.ForeignKey(Class, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user


class Announcement(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.teacher


class Schedule(models.Model):
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    
    def __str__(self):
        return self.subject


class Notification(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.message


class Assignment(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    deadline = models.DateField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='assignments/', blank=True, null=True)
    grade = models.CharField(max_length=10, blank=True, null=True)
    teacher_comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.subject.name


class Exam(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date = models.DateField()
    
    def __str__(self):
        return self.title


class ExamSubmission(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    file = models.FileField(upload_to='exam_submissions/')
    submitted_at = models.DateTimeField(auto_now_add=True)
    grade = models.CharField(max_length=10, blank=True, null=True)
    teacher_comment = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.exam.title


class Material(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    file = models.FileField(upload_to='materials/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
