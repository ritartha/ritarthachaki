from django.shortcuts import render

# Create your views here.
def my_custom_page_not_found_view(request,exception):
    return render(request,'404.html',status=404)  

def homepage(request):
    return render(request,'homepage.html')    