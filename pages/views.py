from django.contrib.auth import get_user_model # new
from rest_framework import generics
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy

from django.views.generic import TemplateView

from .serializers import UserSerializer 


class HomePageView(TemplateView):
    template_name = 'home.html'

class UserList(generics.ListCreateAPIView): # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView): # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class UserListView(ListView):
    model = get_user_model()
    template_name = 'users.html'
    context_object_name = 'object_list'

class UserListUpdate(UpdateView):
    model = get_user_model()
    fields = ('username', 'email',)
    template_name = 'user_edit.html'
    success_url = reverse_lazy('users')

class UserListDelete(DeleteView):
    model = get_user_model()
    template_name = 'user_delete.html'
    success_url = reverse_lazy('users')