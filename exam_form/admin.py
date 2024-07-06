from django.contrib import admin
from django.utils.html import format_html
from .models import ExaminerApplication, Officer

class ExaminerApplicationAdmin(admin.ModelAdmin):
    change_list_template = "admin/examinerapplication_changelist.html"
    list_display = ('department_name', 'is_verified', 'is_submitted')  # Adjust as needed for individual listing
    actions = ['mark_as_verified', 'allow_edit']

    def mark_as_verified(self, request, queryset):
        queryset.update(is_verified=True)
        self.message_user(request, "Selected applications have been marked as verified.")

    def allow_edit(self, request, queryset):
        queryset.update(can_edit=True)
        self.message_user(request, "Selected applications can now be edited by the users.")

    mark_as_verified.short_description = "Mark selected applications as verified"
    allow_edit.short_description = "Allow selected applications to be edited by users"

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}

        total_filled_verified = ExaminerApplication.objects.filter(is_verified=True).count() #is_submitted=True
        partial_filled = ExaminerApplication.objects.filter(is_verified=False, is_submitted=False).count()
        filled_not_verified = ExaminerApplication.objects.filter(is_verified=False, is_submitted=True).exclude(detailed_description='').count()

        extra_context['verified_count'] = total_filled_verified
        extra_context['partial_filled_count'] = partial_filled
        extra_context['unverified_count'] = filled_not_verified

        return super().changelist_view(request, extra_context=extra_context)

admin.site.register(ExaminerApplication, ExaminerApplicationAdmin)
admin.site.register(Officer)