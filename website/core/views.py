from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from Website.core.models import Document
from Website.core.forms import DocumentForm


def home(request):
    return render(request, "core/home.html")

def upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/upload.html', {
        'form': form
    })

def about(request):
    return render(request, 'core/about.html')

def math(request):
    documents = Document.objects.filter(courses="Math")
    return render(request, 'core/math.html', {'documents': documents})

def english(request):
    documents = Document.objects.filter(courses="English")
    return render(request, 'core/english.html', {'documents': documents})

def science(request):
    documents = Document.objects.filter(courses="Science")
    return render(request, 'core/science.html', {'documents': documents})

def art(request):
    documents = Document.objects.filter(courses="Art")
    return render(request, 'core/art.html', {'documents': documents})

def history(request):
    documents = Document.objects.filter(courses="History")
    return render(request, 'core/history.html', {'documents': documents})