from django import forms
from .models import ExaminerApplication

class ExaminerApplicationForm(forms.ModelForm):
    class Meta:
        model = ExaminerApplication
        fields = [
            'department_name', 'address', 'contact_details', 'profile_attachment',
            'contact_person_name', 'designation', 'mobile_phone', 'email', 'activities_since',
            'computer_forensics', 'network_forensics', 'mobile_devices_forensics',
            'digital_video_image_cctv_forensics', 'digital_audio_forensics', 'device_specific_forensics',
            'digital_equipment_machines', 'any_other_forensics', 'detailed_description',
            'organization_chart', 'quality_manual', 'quality_manual_revision_date', 'quality_manual_details',
            'sop_case_acceptance', 'sop_handling_exhibits', 'sop_security_preservation', 'sop_analysis',
            'sop_report_format', 'sop_tools_testing', 'sop_training', 'sop_internal_audit', 'sop_other_procedures',
            'lab_area', 'fire_resistant_cupboards', 'work_desks', 'power_backup', 'expert_opinions_last_three_years'
        ]

    def clean(self):
        cleaned_data = super().clean()
        # Add custom validation logic here
        return cleaned_data
