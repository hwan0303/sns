from django.shortcuts import render

# Create your views here.
def showbase(request):
    return render(request, 'main/base.html')

def showmainpage(request):
    return render(request, 'main/mainpage.html')

def showshow(request):
    return render(request, 'main/show.html' )