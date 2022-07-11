from django.shortcuts import render

# Create your views here.
def project_home_page(request):
    return render(request,'Projects/projects.html')