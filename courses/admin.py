from django.contrib import admin

from .models import Course, Reservations


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'coach',
        'start_at',
        'capacity',
        'is_cancelled',
    )

    list_filter = (
        'is_cancelled',
        'start_at',
    )

    search_fields = (
        'title',
        'coach',
    )

    ordering = ('start_at',)


@admin.register(Reservations)
class ReservationAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'course',
        'status',
        'created_at',
    )

    list_filter = (
        'status',
        'course',
    )

    search_fields = (
        'user__username',
        'course__title',
    )

    list_select_related = (
        'user',
        'course',
    )