from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_view(request, *args,**kwargs):
    print(request.user)
    # return HttpResponse('<h1>HelloWorld</h1>')
    my_context = {
        'my_text' : "this is about me",
        'my_no': 123
    }
    return render(request, "home.html", my_context)
