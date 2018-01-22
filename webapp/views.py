from django.shortcuts import render
#from django.http import HttpResponse

def index(request):
    #return HttpResponse("<h2>HEY!</h2>")
    return render(request, 'webapp/home.html')

def contact(request):
    context = {'aboutus':['if you would like to contact me,','navin.applyjobs@gmail.com']} 
    return render(request, 'webapp/basic.html', context)
# Create your views here.

def login(request):
    #return HttpResponse("<h2>HEY!</h2>")
    return render(request, 'webapp/login.html')
def signin(request):
    #return HttpResponse("<h2>HEY!</h2>")
    return render(request, 'webapp/signin.html')
