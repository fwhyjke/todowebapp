from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, Http404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.utils import timezone

from .forms import *
from .models import *


def welcomepage(request: HttpRequest):
    return render(request, 'yotodo/homepage.html', {'title': 'YoToDoWelcome'})


class MainPage(LoginRequiredMixin, CreateView):
    login_url = 'login'
    form_class = AddToDoIt
    template_name = 'yotodo/main.html'
    success_url = reverse_lazy('main')
    context_object_name = 'tasks'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user.id
        return kwargs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'YoToDo'
        context['tasks'] = ToDoIt.objects.filter(user=self.request.user.id, status=False).order_by('lvl')
        context['lentasks'] = len(context['tasks'])
        return context


class TasksHistoryView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    form_class = AddToDoIt
    success_url = reverse_lazy('main')
    context_object_name = 'tasks'
    template_name = 'yotodo/history.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user.id
        return kwargs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'YoToDo'
        context['tasks'] = ToDoIt.objects.filter(user=self.request.user.id, status=True).order_by('end_at')
        context['lentasks'] = len(context['tasks'])
        return context


class Registration(CreateView):
    template_name = 'yotodo/registration.html'
    success_url = reverse_lazy('main')
    form_class = Register

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main')


class Login(LoginView):
    template_name = 'yotodo/login.html'
    form_class = Loginer

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вход'
        return context

    def get_success_url(self):
        return reverse_lazy('main')


def logout_user(request):
    logout(request)
    return redirect('login')


class CompleteTaskView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = ToDoIt
    fields = ['status', 'end_at']
    success_url = reverse_lazy('main')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.status = True
        self.object.end_at = timezone.now()
        self.object.save()
        return redirect(self.success_url)


class FixedTaskView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = ToDoIt
    fields = ['isfixed']
    success_url = reverse_lazy('main')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.isfixed = True
        self.object.save()
        return redirect(self.success_url)


class UnFixedTaskView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = ToDoIt
    fields = ['isfixed']
    success_url = reverse_lazy('main')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.isfixed = False
        self.object.save()
        return redirect(self.success_url)


class BackTaskView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = ToDoIt
    fields = ['status']
    success_url = reverse_lazy('history')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.status = False
        self.object.save()
        return redirect(self.success_url)


class DeleteTaskView(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = ToDoIt
    success_url = reverse_lazy('history')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)