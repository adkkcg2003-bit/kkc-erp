from django.db import models
from core.models import Employee

class Document(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='documents/', blank=True, null=True)
    uploaded_by = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='uploaded_documents')
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')],
        default='Pending'
    )
    approver = models.ForeignKey(Employee, related_name='approved_documents', on_delete=models.SET_NULL, null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)
    
    # New fields for leave
    leave_type = models.CharField(
        max_length=50,
        choices=[
            ('Sick', 'Sick Leave'),
            ('Casual', 'Casual Leave'),
            ('Earned', 'Earned Leave'),
            ('Maternity', 'Maternity Leave'),
            ('Other', 'Other'),
        ],
        default='Other',
        blank=True
    )
    from_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title