from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.


class Home(TemplateView):
    template_name = 'home.html'

class About(TemplateView):
    template_name = 'about.html'

class Stack:
    def __init__(self, name):
        self.name = name

stacks = [
    Stack("Frontend"),
    Stack("Backend")
]

class ListStacks(TemplateView):
    template_name = 'list_stacks.html'
    # kwargs allow you to pass keyword arguments to a function
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stacks'] = stacks
        return context