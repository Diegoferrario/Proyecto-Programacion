from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render, HttpResponse
# Create your views here.
# pages/views.py
class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView): # new
    template_name = 'about.html'

    
def contact(request):
    return render(request, 'contact/contact.html', )