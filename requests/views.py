from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RequestForm,RequestEmployeeForm, RequestSuperUserForm
from .models import Request
from django.urls import reverse
from django.http import HttpResponseRedirect


class RequestView(CreateView):
    template_name = 'requests/create-request.html'
    queryset = Request.objects.all()
    form_class=RequestForm

    def get_success_url(self):
        return reverse('home')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.owner = self.request.user
        post.save()
        print("HI")
        
        return HttpResponseRedirect(self.get_success_url())
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['requests'] = Request.objects.filter(owner=self.request.user)
        return context

class EmployeeRequestsView(ListView):
    model = Request
    template_name = 'requests/employee-my-requests.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_superuser == False:
            context['requests'] = Request.objects.filter(employee=self.request.user)
        else:
            context['requests'] = Request.objects.all()
        return context

class RequestSingleView(UpdateView):
    template_name = 'requests/request-single.html'
    queryset = Request.objects.all()
    form_class=RequestEmployeeForm

    def get_success_url(self):
        return reverse('employee-my-requests')


class ManagerSingleView(UpdateView):
    template_name = 'requests/request-single.html'
    queryset = Request.objects.all()
    form_class=RequestSuperUserForm

    def get_success_url(self):
        return reverse('employee-my-requests')