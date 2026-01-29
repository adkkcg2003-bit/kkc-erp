from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import F  # Add this import
from hr.models import Task
from workflows.models import Document
from hostel.models import Room

@login_required
def dashboard(request):
    pending_tasks = Task.objects.filter(status='Pending').count()
    pending_documents = Document.objects.filter(status='Pending').count()
    rooms_with_space = Room.objects.filter(occupied__lt=F('capacity')).count()
    
    context = {
        'pending_tasks': pending_tasks,
        'pending_documents': pending_documents,
        'rooms_with_space': rooms_with_space,
        'user': request.user,  # Added - useful in template
    }
    return render(request, 'dashboard.html', context)

from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout(request):
    logout(request)
    return redirect('dashboard')  # Redirect to home/dashboard after logout