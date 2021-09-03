from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserChangeForm
from .models import Request
from django.contrib.auth.mixins import LoginRequiredMixin
from profiles.models import Profile
from django.views import generic

class HomePage(TemplateView):
    http_method_names = ['get']
    template_name = 'feed/homepage.html'
    model = Request

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        requests = Request.objects.all().order_by('-id')[0:30]
        context['requests'] = requests
        return context



class CreateNewRequest(LoginRequiredMixin, CreateView):
    model = Request
    template_name = 'feed/new_request.html'
    fields = ['date_from', 'date_to', 'working_days_off', 'message']
    success_url = "/"

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)





