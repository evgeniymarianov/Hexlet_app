from django.urls import path
from hello_django.calc import views

urlpatterns = [
    path('', views.CalcView.as_view()),
    path(
    '<int:a>/<int:b>',
    views.calc_view,
    name='calc',
    ),
    path('history', views.history),
]
