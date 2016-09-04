from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.utils.decorators import method_decorator

from django.views.generic import FormView, View, CreateView
from django.views.generic.base import TemplateView
from .forms import *


class Login(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def get_form_kwargs(self, **kwargs):
        kwargs = super(Login, self).get_form_kwargs(**kwargs)
        kwargs['request'] = self.request
        return kwargs

    def get_success_url(self):
        if self.request.user.is_superuser:
            return reverse_lazy('admin')
        else:
            return reverse_lazy('home')

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect(reverse_lazy('home'))

class Home(TemplateView):
    template_name = 'home.html'

class Admin(TemplateView):
    template_name = 'admin/admin.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Admin, self).dispatch(*args, **kwargs)


class RegistroMarcacion(CreateView):
    template_name = 'usuario/registroMarcacion.html'
    form_class = RegistroMarcacionForm
    success_url = reverse_lazy('home')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(RegistroMarcacion, self).dispatch(*args, **kwargs)

    def get_initial(self):
        return {
            'usuario':self.request.user
        }

    def get_form_kwargs(self, **kwargs):
        kwargs = super(RegistroMarcacion, self).get_form_kwargs(**kwargs)
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        messages.success(self.request, 'Gracias por Registrar su Despertar')
        messages.success(self.request, 'Que tenga Buen Dia ...')
        return super(RegistroMarcacion, self).form_valid(form)

