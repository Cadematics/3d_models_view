# viewer/views.py
from django.shortcuts import render, redirect
from .forms import ModelUploadForm
from .models import Model3D

def index(request):
    if request.method == 'POST':
        form = ModelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the uploaded model
            return redirect('index')  # Redirect to the home page after upload
    else:
        form = ModelUploadForm()
    
    models = Model3D.objects.all()  # Retrieve all uploaded models

    return render(request, 'viewer/index.html', {
        'form': form,
        'models': models  # Pass uploaded models to the template
    })
