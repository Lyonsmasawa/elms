from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class StudentRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class TeacherRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class ParentRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class MaterialUploadForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['subject', 'file']
        
        
class WeeklyPlanForm(forms.ModelForm):
    class Meta:
        model = WeeklyPlan
        fields = ['week', 'topics']

class LessonPlanForm(forms.ModelForm):
    class Meta:
        model = LessonPlan
        fields = ['date', 'topic', 'objectives', 'activities']