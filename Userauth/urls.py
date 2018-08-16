from django.conf.urls import url
from . import views

from django.views.generic import TemplateView


urlpatterns=[
       url(r'^signup/$',views.signup_user,name='signup.html'),
       url(r'^login/$',views.login_user,name='login.html'),
       
       url(r'^logout/$', TemplateView.as_view(template_name='Userauth/logout.html')),
]
