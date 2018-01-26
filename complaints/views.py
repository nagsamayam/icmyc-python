from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Complaint
from django.urls import reverse_lazy


class ComplaintsListView(ListView):
    model = Complaint
    template_name = 'complaints/index.html'
    context_object_name = 'complaints'


class ComplaintDetailView(DetailView):
    model = Complaint
    template_name = 'complaints/detail.html'
    context_object_name = 'complaint'


class ComplaintCreateView(CreateView):
    model = Complaint
    template_name = 'complaints/new.html'
    fields = '__all__'


class ComplaintUpdateView(UpdateView):
    model = Complaint
    template_name = 'complaints/edit.html'
    fields = ['title', 'body']


class ComplaintDeleteView(DeleteView):
    model = Complaint
    template_name = 'complaints/delete.html'
    success_url = reverse_lazy('complaint-list')

