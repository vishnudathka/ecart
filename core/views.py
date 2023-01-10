from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    html = """
    <h1>Hello World</h1>
    <p>This is a http response from django.</p>
    """
    return HttpResponse(html)
# Create your views here.
 

