from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Course

def course_list(request):
    courses = Course.objects.all()

    return render(
        request,
        'courses/course_list.html',
        {'courses': courses}
    )

def course_detail(request, course_id):

    course = get_object_or_404(
        Course,
        id=course_id
    )

    return render(
        request,
        'courses/course_detail.html',
        {'course': course}
    )

def register(request):

    if request.user.is_authenticated:
        return redirect('course_list')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('course_list')

    else:
        form = UserCreationForm()

    return render(
        request,
        'registration/register.html',
        {'form': form}
    )

def register(request):

    if request.user.is_authenticated:
        return redirect('course_list')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('course_list')

    else:

        form = UserCreationForm()

    return render(
        request,
        'registration/register.html',
        {'form': form}
    )