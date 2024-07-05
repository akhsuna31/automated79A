from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import login_view, signup_view, logout_view, dashboard_view, ExaminerApplicationWizard, form_submitted_view
from django.contrib import admin

urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('examiner-application/', ExaminerApplicationWizard.as_view(), name='examiner_application'),
    path('submitted/', form_submitted_view, name='form_submitted'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)