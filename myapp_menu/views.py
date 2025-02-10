from django.views.decorators.http import require_http_methods
from django.template import loader
from django.http import HttpResponse

# Create your views here.
# @require_http_methods(["GET"])
def home(request):
    template=loader.get_template('menu.html')
    return HttpResponse(template.render())
def about(request):
    template=loader.get_template('about.html')
    return HttpResponse(template.render())
