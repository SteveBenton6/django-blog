from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def this_blog(request):
    return HttpResponse("Hello Blog!")