from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from .forms import LeaveForm
from .models import Document

@login_required
def submit_leave(request):
    if request.method == 'POST':
        form = LeaveForm(request.POST, request.FILES)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.uploaded_by = request.user.employee
            leave.status = 'Pending'
            leave.save()

            # Send email to admin/approver on submit
            subject = f'New Leave Request: {leave.title}'
            message = f"""
            New leave request from {leave.uploaded_by}
            Type: {leave.leave_type}
            From: {leave.from_date}
            To: {leave.to_date}
            Reason: {leave.notes}
            Status: Pending
            View in admin: {request.build_absolute_uri('/admin/workflows/document/')}
            """
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, ['adkkcg2003@gmail.com'])  # Change to HR email if needed

            return redirect('dashboard')
    else:
        form = LeaveForm()
    return render(request, 'submit_leave.html', {'form': form})