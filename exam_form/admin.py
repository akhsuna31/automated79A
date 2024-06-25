from django.contrib import admin

# Register your models here.
from .models import ExaminerApplication

@admin.register(ExaminerApplication)
class ExaminerApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'department_name', 'is_verified', 'can_edit')
    actions = ['mark_as_verified', 'allow_edit']

    def mark_as_verified(self, request, queryset):
        queryset.update(is_verified=True)
        self.message_user(request, "Selected applications have been marked as verified.")

    def allow_edit(self, request, queryset):
        queryset.update(can_edit=True)
        self.message_user(request, "Selected applications can now be edited by the users.")

    mark_as_verified.short_description = "Mark selected applications as verified"
    allow_edit.short_description = "Allow selected applications to be edited by users"
