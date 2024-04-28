from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import *


def student_register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_login')
    else:
        form = StudentRegistrationForm()
    return render(request, 'student_register.html', {'form': form})


def teacher_register(request):
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_login')
    else:
        form = TeacherRegistrationForm()
    return render(request, 'teacher_register.html', {'form': form})


def parent_register(request):
    if request.method == 'POST':
        form = ParentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('parent_login')
    else:
        form = ParentRegistrationForm()
    return render(request, 'parent_register.html', {'form': form})


def student_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('student_dashboard')  # Create this URL
    else:
        form = LoginForm()
    return render(request, 'student_login.html', {'form': form})


def teacher_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('teacher_dashboard')  # Create this URL
    else:
        form = LoginForm()
    return render(request, 'teacher_login.html', {'form': form})


def parent_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('parent_dashboard')  # Create this URL
    else:
        form = LoginForm()
    return render(request, 'parent_login.html', {'form': form})


@login_required
def student_dashboard(request):
    # Get the current logged-in student
    student = Student.objects.get(user=request.user)
    # Retrieve subjects for the student
    subjects = student.subjects.all()
    context = {'subjects': subjects}
    return render(request, 'student_dashboard.html', context)


@login_required
def teacher_dashboard(request):
    # Get the current logged-in teacher
    teacher = Teacher.objects.get(user=request.user)
    context = {}  # Add necessary context data
    return render(request, 'teacher_dashboard.html', context)


@login_required
def parent_dashboard(request):
    # Get the current logged-in parent
    parent = Parent.objects.get(user=request.user)
    context = {}  # Add necessary context data
    return render(request, 'parent_dashboard.html', context)


@login_required
def student_subjects(request):
    # Get the current logged-in student
    student = Student.objects.get(user=request.user)
    # Retrieve subjects for the student
    subjects = student.subjects.all()
    context = {'subjects': subjects}
    return render(request, 'student_subjects.html', context)


def student_exams(request):
    # Retrieve all exams for now, you might want to filter based on student's subjects or other criteria
    exams = Exam.objects.all()
    context = {'exams': exams}
    return render(request, 'student_exams.html', context)


def student_assignments(request):
    # Retrieve all assignments for now, you might want to filter based on student's subjects or other criteria
    assignments = Assignment.objects.all()
    context = {'assignments': assignments}
    return render(request, 'student_assignments.html', context)


def upload_materials(request):
    if request.method == 'POST':
        form = MaterialUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect to a success page or back to the upload page
            return redirect('upload_materials')
    else:
        form = MaterialUploadForm()
    return render(request, 'upload_materials.html', {'form': form})

def weekly_plan(request):
    if request.method == 'POST':
        form = WeeklyPlanForm(request.POST)
        if form.is_valid():
            # Save the form data to the database or perform other actions
            form.save()
            return redirect('weekly_plan')  # Redirect to the same page after saving
    else:
        form = WeeklyPlanForm()
    context = {'form': form}
    return render(request, 'weekly_plan.html', context)

def lesson_plan(request):
    if request.method == 'POST':
        form = LessonPlanForm(request.POST)
        if form.is_valid():
            # Save the form data to the database or perform other actions
            form.save()
            return redirect('lesson_plan')  # Redirect to the same page after saving
    else:
        form = LessonPlanForm()
    context = {'form': form}
    return render(request, 'lesson_plan.html', context)

@login_required
def teacher_submissions(request):
    # Retrieve submissions to be marked (e.g., assignments)
    submissions = Assignment.objects.filter(subject__teacher=request.user.teacher)
    context = {'submissions': submissions}
    return render(request, 'teacher_submissions.html', context)

@login_required
def teacher_classes(request):
    # Retrieve classes scheduled by the teacher
    classes = Class.objects.filter(teacher=request.user.teacher)
    context = {'classes': classes}
    return render(request, 'teacher_classes.html', context)

@login_required
def notifications(request):
    # Retrieve notifications or announcements (e.g., from database)
    notifications = Notification.objects.all()  # You may need to filter based on user roles or other criteria
    context = {'notifications': notifications}
    return render(request, 'notifications.html', context)
