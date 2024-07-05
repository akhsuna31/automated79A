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


'''class ExaminerApplicationForm(forms.ModelForm):
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
        widgets = {
            'department_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_details': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'profile_attachment': forms.FileInput(attrs={'class': 'form-control-file'}),
            'contact_person_name': forms.TextInput(attrs={'class': 'form-control'}),
            'designation': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'activities_since': forms.TextInput(attrs={'class': 'form-control'}),
            'computer_forensics': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'network_forensics': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'mobile_devices_forensics': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'digital_video_image_cctv_forensics': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'digital_audio_forensics': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'device_specific_forensics': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'digital_equipment_machines': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'any_other_forensics': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'detailed_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'organization_chart': forms.FileInput(attrs={'class': 'form-control-file'}),
            'quality_manual': forms.FileInput(attrs={'class': 'form-control-file'}),
            'quality_manual_revision_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'quality_manual_details': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'sop_case_acceptance': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'sop_handling_exhibits': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'sop_security_preservation': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'sop_analysis': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'sop_report_format': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'sop_tools_testing': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'sop_training': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'sop_internal_audit': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'sop_other_procedures': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'lab_area': forms.TextInput(attrs={'class': 'form-control'}),
            'fire_resistant_cupboards': forms.TextInput(attrs={'class': 'form-check-input'}),
            'work_desks': forms.TextInput(attrs={'class': 'form-check-input'}),
            'power_backup': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'expert_opinions_last_three_years': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def clean(self):
        cleaned_data = super().clean()
        # Add custom validation logic here
        return cleaned_data
'''