from django.conf.urls import url
from . import views

urlpatterns = [
		url(r'^(?P<pk>[0-9]+)/$', views.catalog, name="catalog"),
		url(r'^setting/$', views.add_book, name="setting"),
		url(r'^add-category/$', views.add_category, name="add-category"),
		url(r'^settings/$',views.settings,name="settings")
       		]




