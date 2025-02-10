from django.shortcuts import render
from datetime import datetime
# Create your views here.
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.template import loader

def hello(request):
    return HttpResponse("<h2>Hello! Welcome To Django Application</h2>")

def index(request):
    return HttpResponse("<h1>This is Index Page</h1>")


@require_http_methods(["GET"])
def showTime(request):
    now = datetime.now()
    html = "<html> <body>Current Time</body>"
    return HttpResponse(
        f"{html}<body><p>{now}</p></body></html>"
    )  # HttpResponse send HTTP response to client's browser

@require_http_methods(['GET'])
def Employee(request):
   template=loader.get_template('employee.html') #Getting our Template
   return HttpResponse(template.render()) #Renderering the template in Http Response

@require_http_methods(['GET'])
def showStudent(request):
   template=loader.get_template('student.html') #Getting our Template
   student={
       'name' : 'vishal',
       'age':34
   }
   return HttpResponse(template.render(student)) #Renderering the template in Http Response

def ShowImage(request):
   template=loader.get_template('Image.html') #Getting our Template
   return HttpResponse(template.render()) #Renderering the template in Http Response
