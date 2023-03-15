from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from week6_app.models import Student

def index(request):
    # default to Stranger if no user_name provided
    name = request.GET.get("user_name", " there")
    message = f"<html><h1> Hi! {name}!</h1></html>"
    return render(request, 'index.html', {'name': name})

def students(request):
    all_students = Student.objects.all()
    return render(request, 'allstudents.html', {'all_students': all_students})

def detail(request, id):
    if request.method == 'GET':
        try:
            students_detail = Student.objects.get(id=id)
        except Student.DoesNotExist:
            raise Http404('Student does not exist')
        return render(request, 'detail.html', {'students_detail': students_detail})
