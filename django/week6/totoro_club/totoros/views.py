from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    user_name = request.GET.get('user_name', 'There!')
    if user_name == None:
        return HttpResponse('Hello! You')
    else:
        return render(request, 'base.html', {'name': user_name})
    # return HttpResponse('Welcome!')

def create(request):
    return HttpResponse('create')

def read(request,name):
    return HttpResponse('Hello! '+name)

# def template(request):
#     user_name = request.GET.get('user_name', 'There!')
#     if user_name == None:
#         return HttpResponse('Hello! You')
#     else:
#         return render(request, 'base.html', {'name': user_name})
