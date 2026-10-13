from django.contrib.auth import views as auth_views
from django.urls import path

from . import views


urlpatterns = [

    path('', views.course_list, name='course_list'),

    path('inscription/', views.register, name='register'),

    path(
        'connexion/',
        auth_views.LoginView.as_view(
            template_name='registration/login.html'
        ),
        name='login'
    ),

    path(
        'deconnexion/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),

    path(
        '<int:course_id>/reserver/',
        views.reserve_course,
        name='reserve_course'
    ),

    path(
        '<int:course_id>/',
        views.course_detail,
        name='course_detail'
    ),

]