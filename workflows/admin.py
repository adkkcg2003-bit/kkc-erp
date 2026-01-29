from django.contrib import admin
from django.utils.html import format_html
from django.core.mail import send_mail
from django.conf import settings
from .models import Document

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_by', 'status_colored', 'approver', 'notes_short', 'submitted_at', 'file_link')
    list_filter = ('status', 'uploaded_by', 'approver')
    search_fields = ('title', 'notes')
    readonly_fields = ('submitted_at',)
    actions = ['approve_selected', 'reject_selected']

    def status_colored(self, obj):
        colors = {
            'Pending': 'orange',
            'Approved': 'green',
            'Rejected': 'red'
        }
        return format_html('<span style="color: {}; font-weight: bold;">{}</span>', colors[obj.status], obj.status)
    status_colored.short_description = 'Status'

    def file_link(self, obj):
        if obj.file:
            url = obj.file.url
            name = obj.file.name.split('/')[-1]
            if obj.file.name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                return format_html('<img src="{}" width="50" height="50" alt="{}" />', url, name)
            return format_html('<a href="{}" target="_blank">{}</a>', url, name)
        return "No file"
    file_link.short_description = 'File Preview'

    def notes_short(self, obj):
        return obj.notes[:50] + '...' if obj.notes else ''
    notes_short.short_description = 'Notes'

    def approve_selected(self, request, queryset):
        for obj in queryset:
            obj.status = 'Approved'
            obj.notes = (obj.notes or '') + '\nApproved by admin'
            obj.save()

            # Email on approval (if Employee has email field)
            if obj.uploaded_by and obj.uploaded_by.email:
                subject = f'Your Leave Request Approved: {obj.title}'
                message = f"""
Your leave request has been approved.

Title: {obj.title}
Type: {obj.leave_type}
From: {obj.from_date}
To: {obj.to_date}
Notes: {obj.notes or 'No notes'}
"""
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [obj.uploaded_by.email])
        self.message_user(request, "Selected documents approved and notified.")
    approve_selected.short_description = "Approve selected documents"

    def reject_selected(self, request, queryset):
        for obj in queryset:
            obj.status = 'Rejected'
            obj.notes = (obj.notes or '') + '\nRejected by admin'
            obj.save()

            # Email on rejection
            if obj.uploaded_by and obj.uploaded_by.email:
                subject = f'Your Leave Request Rejected: {obj.title}'
                message = f"""
Your leave request has been rejected.

Title: {obj.title}
Type: {obj.leave_type}
From: {obj.from_date}
To: {obj.to_date}
Notes: {obj.notes or 'No notes'}
"""
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [obj.uploaded_by.email])
        self.message_user(request, "Selected documents rejected and notified.")
    reject_selected.short_description = "Reject selected documents"