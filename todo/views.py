import sys, codecs, io
#sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding = 'utf-8')
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Todo
from django.urls import reverse_lazy
from .forms import TodoForm

class TodoListView(ListView):
    model = Todo
    template_name = 'todo/list.html'

class TodoDetailView(DetailView):
    model = Todo
    template_name = 'todo/detail.html'
    pk_url_kwarg = 'id'

class TodoCreateView(CreateView):
    model = Todo
    template_name = 'todo/form.html'
    form_class = TodoForm
    success_url = reverse_lazy('todo_list')

class TodoUpdateView(UpdateView):
    model = Todo
    template_name = 'todo/update.html'
    pk_url_kwarg = 'id'
    form_class = TodoForm
    success_url = reverse_lazy('todo_list')

class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'todo/delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('todo_list')

