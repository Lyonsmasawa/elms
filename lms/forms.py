from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class NotificationForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)


class TeacherRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['message']


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['class_name', 'subject', 'date', 'time']


class WeeklyPlanForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['weekly_plan']

class LessonPlanForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['lesson_plan']
        
        
class StudentRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
        
        
class AssignmentCreationForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'description', 'deadline', 'file']
        

class AssignmentSubmissionForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['file']
