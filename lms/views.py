from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import *


@login_required
def notifications(request):
    # Retrieve notifications or announcements (e.g., from database)
    # You may need to filter based on user roles or other criteria
    notifications = Notification.objects.all()
    context = {'notifications': notifications}
    return render(request, 'notifications.html', context)


def teacher_registration(request):
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_teacher = True
            user.save()
            # Redirect to a page indicating successful registration
            return redirect('teacher_registration_success')
    else:
        form = TeacherRegistrationForm()
    return render(request, 'teacher_registration.html', {'form': form})


def teacher_registration_success(request):
    return render(request, 'teacher_registration_success.html')


def post_announcement(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.teacher = request.user.teacher
            announcement.save()
            # Redirect to dashboard or appropriate page
            return redirect('dashboard')
    else:
        form = AnnouncementForm()
    return render(request, 'post_announcement.html', {'form': form})


def schedule_lesson(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.teacher = request.user.teacher
            schedule.save()
            # Redirect to dashboard or appropriate page
            return redirect('dashboard')
    else:
        form = ScheduleForm()
    return render(request, 'schedule_lesson.html', {'form': form})


def update_weekly_plan(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    if request.method == 'POST':
        form = WeeklyPlanForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            # Redirect to subject detail page
            return redirect('subject_detail', subject_id=subject_id)
    else:
        form = WeeklyPlanForm(instance=subject)
    return render(request, 'update_weekly_plan.html', {'form': form})


def update_lesson_plan(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    if request.method == 'POST':
        form = LessonPlanForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            # Redirect to subject detail page
            return redirect('subject_detail', subject_id=subject_id)
    else:
        form = LessonPlanForm(instance=subject)
    return render(request, 'update_lesson_plan.html', {'form': form})


def student_registration(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_student = True
            user.save()
            # Redirect to a page indicating successful registration
            return redirect('student_registration_success')
    else:
        form = StudentRegistrationForm()
    return render(request, 'student_registration.html', {'form': form})


def student_registration_success(request):
    return render(request, 'student_registration_success.html')


def approve_student(request, student_id):
    student = CustomUser.objects.get(id=student_id)
    student.is_approved = True
    student.save()
    # Redirect to a page indicating successful approval
    return redirect('manage_students')


def view_subjects(request, class_id):
    class_obj = Class.objects.get(id=class_id)
    subjects = Subject.objects.filter(class_name=class_obj)
    return render(request, 'view_subjects.html', {'class_obj': class_obj, 'subjects': subjects})


def view_schedule(request, class_id):
    class_obj = Class.objects.get(id=class_id)
    # Implement logic to fetch schedule for the class
    schedule = "Monday 9:00 AM - Math, Tuesday 10:00 AM - Science"  # Example schedule
    return render(request, 'view_schedule.html', {'class_obj': class_obj, 'schedule': schedule})


def create_assignment(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    students = Student.objects.filter(classroom=subject.classroom)
    if request.method == 'POST':
        form = AssignmentCreationForm(request.POST, request.FILES)
        if form.is_valid():
            for student in students:
                assignment = form.save(commit=False)
                assignment.subject = subject
                assignment.save()
            # Redirect to a page indicating successful assignment creation
            return redirect('assignment_created')
    else:
        form = AssignmentCreationForm()
    return render(request, 'create_assignment.html', {'form': form, 'subject': subject})

def submit_assignment(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    students = Student.objects.filter(classroom=subject.classroom)
    if request.method == 'POST':
        form = AssignmentSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            for student in students:
                assignment = form.save(commit=False)
                assignment.subject = subject
                assignment.student = student
                assignment.save()
            # Redirect to a page indicating successful assignment submission
            return redirect('assignment_submitted')
    else:
        form = AssignmentSubmissionForm()
    return render(request, 'submit_assignment.html', {'form': form, 'subject': subject})

def mark_assignment(request, assignment_id, student_id):
    assignment = Assignment.objects.get(id=assignment_id)
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        grade = request.POST.get('grade')
        teacher_comment = request.POST.get('teacher_comment')
        # Update assignment with grade and teacher comment for the specific student
        assignment.grade = grade
        assignment.teacher_comment = teacher_comment
        assignment.save()
        # Redirect to a page indicating successful assignment marking
        return redirect('assignment_marked')
    return render(request, 'mark_assignment.html', {'assignment': assignment, 'student': student})
