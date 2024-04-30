from .models import Class, Subject
from .forms import NotificationForm
from django.shortcuts import render, redirect
from .models import *


def manage_classes(request):
    classes = Class.objects.all()
    return render(request, 'manage_classes.html', {'classes': classes})


def manage_subjects(request):
    subjects = Subject.objects.all()
    return render(request, 'manage_subjects.html', {'subjects': subjects})


def send_notification(request):
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            # Send notification to all users
            # Example: Notification.objects.create(message=message)
            # Redirect to the same page after sending
            return redirect('send_notification')
    else:
        form = NotificationForm()
    return render(request, 'send_notification.html', {'form': form})


def assign_classes(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    classes = Class.objects.all()
    if request.method == 'POST':
        selected_classes = request.POST.getlist('classes')
        teacher.classes_taught.clear()
        for class_id in selected_classes:
            class_obj = Class.objects.get(id=class_id)
            teacher.classes_taught.add(class_obj)
        return redirect('manage_teachers')  # Redirect to manage teachers page
    return render(request, 'assign_classes.html', {'teacher': teacher, 'classes': classes})


def assign_subjects(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    subjects = Subject.objects.all()
    if request.method == 'POST':
        selected_subjects = request.POST.getlist('subjects')
        teacher.subjects_taught.clear()
        for subject_id in selected_subjects:
            subject_obj = Subject.objects.get(id=subject_id)
            teacher.subjects_taught.add(subject_obj)
        return redirect('manage_teachers')  # Redirect to manage teachers page
    return render(request, 'assign_subjects.html', {'teacher': teacher, 'subjects': subjects})


def approve_teacher(request, teacher_id):
    teacher = CustomUser.objects.get(id=teacher_id)
    teacher.is_approved_teacher = True
    teacher.save()
    # Redirect to a page indicating successful approval
    return redirect('manage_teachers')
