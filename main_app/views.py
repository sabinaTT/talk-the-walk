from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Stack
from .models import Question
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

class Update_Stack(UpdateView):
    model = Stack
    fields = ['name']
    template_name = 'update_stack.html'
    success_url = '/stacks'

class DeleteStack(DeleteView):
    model = Stack
    template_name = 'delete-stack.html'
    success_url = '/questions/'

def list_questions(request):
    questions  = Question.objects.all()
    return render(request, 'list_questions.html', {'questions': questions})

def view_question(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'view_question.html', {'question': question})

class Create_Question(CreateView):
    model = Question
    fields = '__all__'
    template_name = 'create_question.html'
    success_url = '/questions/'

class Update_Question(UpdateView):
    model = Question
    fields = ['the_question', 'answer', 'stack']
    template_name = 'update_question.html'
    success_url = '/questions/'

class Delete_Question(DeleteView):
    model = Question
    template_name = 'confirm_delete_question.html'
    success_url = '/questions/'

