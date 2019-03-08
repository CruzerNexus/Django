from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Cri

class CrirListView(ListView):
    model = Cri
    template_name = 'criRapp/home.html'

    def get_queryset(self):
        return Cri.objects.order_by('-created')

class CrirDetailView(LoginRequiredMixin,DetailView):
    model = Cri
    template_name = 'criRapp/cri_detail.html'

class CrirCreateView(LoginRequiredMixin,CreateView):
    model = Cri
    template_name = 'criRapp/cri_new.html'
    fields = ['body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CrirUpdateView(LoginRequiredMixin,UpdateView):
    model = Cri
    template_name = 'criRapp/cri_edit.html'
    fields = ['body']

class CrirDeleteView(LoginRequiredMixin,DeleteView):
    model = Cri
    template_name = 'criRapp/cri_delete.html'
    success_url = reverse_lazy('home')