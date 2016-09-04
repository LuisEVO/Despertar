from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^logout/$', Logout.as_view(), name='logout'),
    url(r'^admin/$', Admin.as_view(), name='admin'),
    url(r'^marcacion/$', RegistroMarcacion.as_view(), name='registro_marcacion'),
 ]