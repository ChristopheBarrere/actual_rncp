from datetime import timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Course, Reservations


class CourseTests(TestCase):

    def setUp(self):

        self.user = get_user_model().objects.create_user(
            username='chris',
            password='TestPassword123!'
        )

        self.course = Course.objects.create(
            title='Yoga débutant',
            description='Cours accessible aux débutants.',
            coach='Sophie',
            start_at=timezone.now() + timedelta(days=7),
            duration_minutes=60,
            capacity=10
        )

    def test_course_list_displays_course(self):

        response = self.client.get(
            reverse('course_list')
        )

        self.assertEqual(response.status_code, 200)

        self.assertContains(
            response,
            'Yoga débutant'
        )

    def test_course_detail_displays_course(self):

        response = self.client.get(
            reverse(
                'course_detail',
                args=[self.course.id]
            )
        )

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'Sophie')

    def test_authenticated_user_can_reserve(self):

        self.client.login(
            username='chris',
            password='TestPassword123!'
        )

        response = self.client.post(
            reverse(
                'reserve_course',
                args=[self.course.id]
            )
        )

        self.assertEqual(response.status_code, 302)

        self.assertTrue(
            Reservations.objects.filter(
                user=self.user,
                course=self.course,
                status=Reservations.Status.CONFIRMED
            ).exists()
        )

    def test_user_can_cancel_reservation(self):

        reservation = Reservations.objects.create(
            user=self.user,
            course=self.course
        )

        self.client.login(
            username='chris',
            password='TestPassword123!'
        )

        response = self.client.post(
            reverse(
                'cancel_reservation',
                args=[self.course.id]
            )
        )

        reservation.refresh_from_db()

        self.assertEqual(response.status_code, 302)

        self.assertEqual(
            reservation.status,
            Reservations.Status.CANCELLED
        )
