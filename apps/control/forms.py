import time
from django import forms
from django.contrib.auth import authenticate, login
from django.db.models import Q

from .models import *


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label='Usuario', widget=forms.TextInput(attrs={'class':'user'}))
    password = forms.CharField(max_length=50, label='Contraceña', widget=forms.PasswordInput(attrs={'class':'message'}))

    def __init__(self, **kwargs):
        self.request = kwargs.pop('request', None)
        super(LoginForm, self).__init__(**kwargs)

    def clean(self):
        username = self.cleaned_data.get('username',None)
        password = self.cleaned_data.get('password',None)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
        else:
            self.add_error('username', 'El usuario o contraceña es incorrecto')


class RegistroMarcacionForm(forms.ModelForm):
    class Meta:
        model = Marcacion
        fields = ('__all__')

    def __init__(self, **kwargs):
        self.request = kwargs.pop('request',None)
        super(RegistroMarcacionForm, self).__init__(**kwargs)

    def clean_fecha(self):
        return time.strftime("%Y-%m-%d")

    def clean_hora(self):
        return time.strftime("%X")

    def clean(self):
        fecha = self.cleaned_data.get('fecha',None)
        marcacion = Marcacion.objects.filter(Q(usuario=self.request.user) & Q(fecha=fecha))
        if marcacion:
            self.add_error('fecha','Usted ya registro su despertar el dia de hoy')
