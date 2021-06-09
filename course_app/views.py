from django.shortcuts import render, redirect
from .models import Course
# Create your views here.
def index(request):
    context= {
        'courses': Course.objects.all()
    }
    return render(request, 'index.html', context)

def add(request):
    course = Course.objects.create(
        name= request.POST['name'],
        description= request.POST['description'],
    )
    return redirect('/')

def destroy(request, course_id):
    context= {
        'one_course': Course.objects.get(id=course_id)
    }
    return render(request, 'delete.html', context)

def delete(request, course_id):
    delete_course = Course.objects.get(id=course_id)
    delete_course.delete()
    return redirect('/')