from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.


class Home(TemplateView):
    template_name = 'home.html'

    # def get(self, request):
    #     return HttpResponse('All great stories begin in two ways..')

class About(TemplateView):
    template_name = 'about.html'