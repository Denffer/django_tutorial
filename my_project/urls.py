from django.conf.urls import include, url
from django.contrib import admin
from mycontacts import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.show),
    url(r'^add/', views.add),
]