from django.shortcuts import render, redirect
from .forms import ExaminerApplicationForm


def examiner_application_view(request):
    if request.method == 'POST':
        form = ExaminerApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save()
            # Prepare data for Google Sheets
            data = [
                application.department_name, application.address, application.contact_details,
                application.contact_person_name, application.designation, application.mobile_phone,
                application.email, application.activities_since, application.computer_forensics,
                application.network_forensics, application.mobile_devices_forensics,
                application.digital_video_image_cctv_forensics, application.digital_audio_forensics,
                application.device_specific_forensics, application.digital_equipment_machines,
                application.any_other_forensics, application.detailed_description,
                application.lab_area, application.fire_resistant_cupboards, application.work_desks,
                application.power_backup, application.expert_opinions_last_three_years
            ]
            # Call your Google Sheets export function here (implement export_to_google_sheets(data) in utils.py)
            # export_to_google_sheets(data)
            return redirect('form_submitted')
    else:
        form = ExaminerApplicationForm()

    return render(request, 'exam_form/examiner_application.html', {'form': form})


def form_submitted_view(request):
    return render(request, 'exam_form/form_submitted.html')
