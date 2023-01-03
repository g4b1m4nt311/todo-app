from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Todo
from .forms import CreateUserForm


# login
class AppLogin(LoginView):
    template_name = 'todo_app/signin.html'
    fields = ['email', 'password1', 'password2']
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('todos')


# register
class SignUp(FormView):
    template_name = 'todo_app/signup.html'
    form_class = CreateUserForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('todos')

    # redirect user once submitted
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(SignUp, self).form_valid(form)

    # restrict unauthenticated users
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('todos')
        return super(SignUp, self).get(*args, **kwargs)


# generate list of todos
class TodoList(LoginRequiredMixin, ListView):
    model = Todo
    context_object_name = 'todos'  # improves readibility

    # restrict users from accessing other users data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todos'] = context['todos'].filter(user=self.request.user)
        return context


# detail view for todo item
class TodoDetail(LoginRequiredMixin, DetailView):
    model = Todo
    context_object_name = 'todo'
    template_name = 'todo_app/todo.html'  # customise todo detail template name


# create new todo
class TodoCreate(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ['name', 'description', 'status']
    success_url = reverse_lazy('todos')

    # only allow user to create their own todos
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TodoCreate, self).form_valid(form)


# update todo
class TodoUpdate(LoginRequiredMixin, UpdateView):
    model = Todo
    fields = ['name', 'description', 'status']
    success_url = reverse_lazy('todos')


# delete todo
class TodoDelete(LoginRequiredMixin, DeleteView):
    model = Todo
    context_object_name = 'todo'
    success_url = reverse_lazy('todos')
