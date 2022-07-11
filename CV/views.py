from django.shortcuts import render

# Create your views here.
def cv_home_page(request):
    return render(request,'CV/cv.html')
