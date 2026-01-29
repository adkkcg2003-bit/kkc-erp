from django import forms
from .models import Document

class LeaveForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['leave_type', 'title', 'from_date', 'to_date', 'notes', 'file']
        widgets = {
            'leave_type': forms.Select(),
            'title': forms.TextInput(attrs={'placeholder': 'e.g. Sick Leave - Jan 28 to Jan 30'}),
            'from_date': forms.DateInput(attrs={'type': 'date'}),
            'to_date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Reason and any other details...'}),
            'file': forms.FileInput(),
        }