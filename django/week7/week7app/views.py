from django.shortcuts import render, HttpResponse
from week7app.models import Company
# Create your views here.
def insert(request):
    model = Company()
    model.insert()
    return HttpResponse('Init!')

def retrieveCompanyList(request):
    companies = Company.objects.all().values()
    return render(request, 'companyList.html',{'companyList':companies})

def retrieveCompanyDetail(request,id):
    company = Company.objects.get(id=id)
    return render(request, 'companyDetail.html',{'company':company})