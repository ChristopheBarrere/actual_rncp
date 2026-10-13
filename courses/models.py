from django.db import models
from django.conf import settings

class Course(models.Model):

    title = models.CharField(max_length=120)
    description = models.TextField()
    coach = models.CharField(max_length=120)
    start_at = models.DateTimeField()
    duration_minutes = models.PositiveSmallIntegerField(default=60)
    capacity = models.PositiveSmallIntegerField()
    is_cancelled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def confirmed_reservations_count(self):

        return self.reservations.filter(
            status=Reservations.Status.CONFIRMED
        ).count()

    @property
    def places_available(self):

        return max(
            self.capacity - self.confirmed_reservations_count,
            0
        )

    @property
    def is_full(self):

        return self.places_available == 0


class Reservations(models.Model):

    class Status(models.TextChoices):
        CONFIRMED = 'confirmed', 'Confirmée'
        CANCELLED = 'cancelled', 'Annulée'

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reservations'
    )
        
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='reservations'
    )

    status = models.CharField(
        max_length=12,
        choices=Status.choices,
        default=Status.CONFIRMED
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        constraints = [
            models.UniqueConstraint(
                fields=['user', 'course'],
                name='unique_user_course'
            )
        ]

    def __str__(self):

        return (
            f'{self.user.username} - '
            f'{self.course.title}'
        )
