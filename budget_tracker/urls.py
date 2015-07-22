from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.users.views import LoginView

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('apps.frontend.urls', namespace='frontend')),
    url(r'^', include('apps.tracking.urls', namespace='tracking')),
    url(r'^login/$', LoginView.as_view(), name='login'),

)
