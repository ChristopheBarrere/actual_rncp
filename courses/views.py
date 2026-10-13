from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Course, Reservations

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

    reservation = None

    has_confirmed_reservation = False

    if request.user.is_authenticated:

        reservation = Reservations.objects.filter(
            user=request.user,
            course=course
        ).first()

        has_confirmed_reservation = (
            reservation is not None
            and reservation.status
            == Reservations.Status.CONFIRMED
        )

    return render(
        request,
        'courses/course_detail.html',
        {
            'course': course,
            'reservation': reservation,
            'has_confirmed_reservation': (
                has_confirmed_reservation
            ),
        }
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

@login_required
@require_POST
def reserve_course(request, course_id):

    course = get_object_or_404(
        Course,
        id=course_id
    )

    if course.is_cancelled:

        messages.error(
            request,
            'Ce cours est annulé.'
        )

        return redirect(
            'course_detail',
            course_id=course.id
        )

    reservation = Reservations.objects.filter(
        user=request.user,
        course=course
    ).first()

    if (
        reservation
        and reservation.status == Reservations.Status.CONFIRMED
    ):

        messages.info(
            request,
            'Vous avez déjà réservé ce cours.'
        )

        return redirect(
            'course_detail',
            course_id=course.id
        )

    if course.is_full:

        messages.error(
            request,
            'Ce cours est complet.'
        )

        return redirect(
            'course_detail',
            course_id=course.id
        )

    if reservation:

        reservation.status = Reservations.Status.CONFIRMED

        reservation.save(
            update_fields=['status', 'updated_at']
        )

    else:

        Reservations.objects.create(
            user=request.user,
            course=course
        )

    messages.success(
        request,
        'Votre réservation est confirmée.'
    )

    return redirect(
        'course_detail',
        course_id=course.id
    )

@login_required
@require_POST
def cancel_reservation(request, course_id):

    reservation = get_object_or_404(
        Reservations,
        user=request.user,
        course_id=course_id,
        status=Reservations.Status.CONFIRMED
    )

    reservation.status = Reservations.Status.CANCELLED

    reservation.save(
        update_fields=['status', 'updated_at']
    )

    messages.success(
        request,
        'Votre réservation est annulée.'
    )

    return redirect(
        'course_detail',
        course_id=course_id
    )