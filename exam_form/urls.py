from django.urls import path
from .views import examiner_application_view, form_submitted_view

urlpatterns = [
    path('', examiner_application_view, name='examiner_application'),
    path('submitted/', form_submitted_view, name='form_submitted'),
]
