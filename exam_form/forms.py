from django import forms
from .models import ExaminerApplication


class ContactInformationForm(forms.ModelForm):
    class Meta:
        model = ExaminerApplication
        fields = ['department_name', 'address', 'contact_details', 'profile_attachment', 'contact_person_name', 'designation', 'mobile_phone', 'email', 'activities_since']

class PersonalInformationForm(forms.ModelForm):
    class Meta:
        model = ExaminerApplication
        fields = ['contact_person_name', 'designation', 'mobile_phone', 'email']

class ExpertiseAreasForm(forms.ModelForm):
    class Meta:
        model = ExaminerApplication
        fields = [
            'computer_forensics', 'network_forensics', 'mobile_devices_forensics',
            'digital_video_image_cctv_forensics', 'digital_audio_forensics', 'device_specific_forensics',
            'digital_equipment_machines', 'any_other_forensics'
        ]

class DetailedDescriptionsForm(forms.ModelForm):
    class Meta:
        model = ExaminerApplication
        fields = ['detailed_description', 'organization_chart', 'quality_manual', 'quality_manual_revision_date', 'quality_manual_details']

class SOPsForm(forms.ModelForm):
    class Meta:
        model = ExaminerApplication
        fields = [
            'sop_case_acceptance', 'sop_handling_exhibits', 'sop_security_preservation', 'sop_analysis',
            'sop_report_format', 'sop_tools_testing', 'sop_training', 'sop_internal_audit', 'sop_other_procedures'
        ]

class LabFacilitiesForm(forms.ModelForm):
    class Meta:
        model = ExaminerApplication
        fields = ['lab_area', 'fire_resistant_cupboards', 'work_desks', 'power_backup', 'expert_opinions_last_three_years']

