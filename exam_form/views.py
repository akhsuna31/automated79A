from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
#from .forms import ExaminerApplicationForm
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .models import ExaminerApplication
from .utils import export_to_google_sheets
from django.urls import reverse
from formtools.wizard.views import SessionWizardView
import logging
from .forms import (
    ContactInformationForm, PersonalInformationForm, ExpertiseAreasForm,
    DetailedDescriptionsForm, SOPsForm, LabFacilitiesForm
)

logger = logging.getLogger(__name__)


class ExaminerApplicationWizard(SessionWizardView):
    form_list = [
        ('contact_information', ContactInformationForm),
        ('personal_information', PersonalInformationForm),
        ('expertise_areas', ExpertiseAreasForm),
        ('detailed_descriptions', DetailedDescriptionsForm),
        ('sops', SOPsForm),
        ('lab_facilities', LabFacilitiesForm),
    ]
    templates = {
        'contact_information': 'exam_form/contact_information.html',
        'personal_information': 'exam_form/personal_information.html',
        'expertise_areas': 'exam_form/expertise_areas.html',
        'detailed_descriptions': 'exam_form/detailed_descriptions.html',
        'sops': 'exam_form/sops.html',
        'lab_facilities': 'exam_form/lab_facilities.html',
    }
    file_storage = FileSystemStorage(location=settings.MEDIA_ROOT)

    def get_template_names(self):
        return [self.templates[self.steps.current]]

    def done(self, form_list, **kwargs):
        # Save all form data to a new ExaminerApplication instance
        user = self.request.user
        data = {}
        for form in form_list:
            data.update(form.cleaned_data)

        application = ExaminerApplication.objects.create(user=user, **data)
        messages.success(self.request, "Application submitted successfully.")
        return redirect('dashboard')


@csrf_exempt
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid login credentials")
    return render(request, "exam_form/login.html")

@csrf_exempt
def signup_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
        else:
            user = User.objects.create_user(username, email, password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('dashboard')
    return render(request, "exam_form/signup.html")

@csrf_exempt
def logout_view(request):
    auth_logout(request)
    return redirect('login')

@login_required(login_url="/login/")
def dashboard_view(request):
    try:
        application = ExaminerApplication.objects.get(user=request.user)
    except ExaminerApplication.DoesNotExist:
        application = None

    return render(request, "exam_form/dashboard.html", {'application': application, 'user': request.user})


'''@login_required(login_url="/login/")
def examiner_application_view(request):
    try:
        application = ExaminerApplication.objects.get(user=request.user)
    except ExaminerApplication.DoesNotExist:
        application = None

    if application and not application.can_edit:
        messages.error(request, "You cannot edit the application at this time.")
        return redirect('dashboard')

    if request.method == 'POST':
        form = ExaminerApplicationForm(request.POST, request.FILES, instance=application)
        if form.is_valid():
            app = form.save(commit=False)
            app.user = request.user
            app.save()
            messages.success(request, "Application submitted successfully.")
            return redirect('dashboard')
    else:
        form = ExaminerApplicationForm(instance=application)

    return render(request, 'exam_form/examiner_application.html', {'form': form})
'''

@login_required(login_url="/login/")
def form_submitted_view(request):
    return render(request, 'exam_form/form_submitted.html')
