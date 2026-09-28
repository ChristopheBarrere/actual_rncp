from django.db import models

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
