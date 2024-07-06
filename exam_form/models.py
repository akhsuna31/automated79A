from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ExaminerApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    department_name = models.CharField(max_length=255)
    address = models.TextField()
    contact_details = models.TextField()  # Can include phone, email, fax, website
    profile_attachment = models.FileField(upload_to='attachments/', null=True, blank=True)
    contact_person_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    mobile_phone = models.CharField(max_length=20)
    email = models.EmailField()
    activities_since = models.DateField()

    # Forensic Investigation Types
    computer_forensics = models.BooleanField(default=False)
    network_forensics = models.BooleanField(default=False)
    mobile_devices_forensics = models.BooleanField(default=False)
    digital_video_image_cctv_forensics = models.BooleanField(default=False)
    digital_audio_forensics = models.BooleanField(default=False)
    device_specific_forensics = models.BooleanField(default=False)
    digital_equipment_machines = models.BooleanField(default=False)
    any_other_forensics = models.CharField(max_length=255, null=True, blank=True)

    # Detailed Descriptions
    detailed_description = models.TextField()

    organization_chart = models.FileField(upload_to='attachments/', null=True, blank=True)
    quality_manual = models.FileField(upload_to='attachments/', null=True, blank=True)
    quality_manual_revision_date = models.DateField(null=True, blank=True)
    quality_manual_details = models.TextField(null=True, blank=True)

    # SOPs
    sop_case_acceptance = models.BooleanField(default=False)
    sop_handling_exhibits = models.BooleanField(default=False)
    sop_security_preservation = models.BooleanField(default=False)
    sop_analysis = models.BooleanField(default=False)
    sop_report_format = models.BooleanField(default=False)
    sop_tools_testing = models.BooleanField(default=False)
    sop_training = models.BooleanField(default=False)
    sop_internal_audit = models.BooleanField(default=False)
    sop_other_procedures = models.TextField(null=True, blank=True)

    # Lab Details
    lab_area = models.CharField(max_length=255)
    fire_resistant_cupboards = models.IntegerField()
    work_desks = models.IntegerField()
    power_backup = models.TextField()

    # Expert Opinions
    expert_opinions_last_three_years = models.IntegerField()

    is_verified = models.BooleanField(default=False)
    can_edit = models.BooleanField(default=False)
    is_submitted = models.BooleanField(default=False)

    def __str__(self):
        return self.department_name


class Officer(models.Model):
    name = models.CharField(max_length=100)
    rank = models.CharField(max_length=100)