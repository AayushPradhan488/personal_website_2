# example/views.py
from datetime import datetime

from django.http import HttpResponse
from django.template import loader

def index(request):
    now = datetime.now()
    namepage = loader.get_template('name.html')
    return HttpResponse(namepage.render())