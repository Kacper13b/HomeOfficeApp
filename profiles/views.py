from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views import generic
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserChangeForm
from .models import Profile
from django.contrib.auth.models import User
from django.urls import reverse_lazy



class ProfileDetailView(DetailView):
    http_method_names = ["get"]
    template_name = 'feed/profile.html'
    model = User
    context_object_name = "user"
    slug_field = 'id'
    slug_url_kwarg = 'id'


class ProfileEditView(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'feed/editprofile.html'
    success_url = '/'

    def get_object(self):
        return self.request.user


class ProfileEditPageView(generic.UpdateView):
    model = Profile
    template_name = 'feed/editprofile_page.html'
    #add user field
    fields = ['position', 'image', 'manager']
    success_url = '/'
