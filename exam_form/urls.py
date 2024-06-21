from django.urls import path
from .views import login_view, signup_view, logout_view, dashboard_view, examiner_application_view, form_submitted_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('examiner-application/', examiner_application_view, name='examiner_application'),
    path('submitted/', form_submitted_view, name='form_submitted'),
]
