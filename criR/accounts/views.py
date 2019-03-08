from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from criRapp.models import Cri
from django.contrib.auth.models import User

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'criRapp/signup.html'

class UserPostListView(generic.ListView):
    model = Cri
    template_name = 'home.html'

    def get_queryset(self):
        return Cri.objects.filter(author__username__exact=self.kwargs['user'])


class UserListView(generic.ListView):
    model = User
    template_name = 'cri_list.html'
