from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Stack
from django.views.generic.edit import CreateView
from django.views.generic import DetailView

# Create your views here.


class Home(TemplateView):
    template_name = 'home.html'

class About(TemplateView):
    template_name = 'about.html'

class ListStacks(TemplateView):
    template_name = 'list_stacks.html'
    # kwargs allow you to pass keyword arguments to a function
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stacks'] = Stack.objects.all()
        return context

class Create_Stack(CreateView):
    model = Stack
    fields = ['name']
    template_name = 'create_stack.html'
    success_url = '/stacks/'

class StackDetail(DetailView):
    model = Stack
    template_name = 'stack_detail.html'