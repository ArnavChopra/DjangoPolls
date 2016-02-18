"""
Definition of urls for $safeprojectname$.
"""
from django.contrib.auth.views import login
from app.views import PollListView
from datetime import datetime
from django.conf.urls import patterns, include, url
from django.contrib import admin
from app.forms import BootstrapAuthenticationForm
from app.models import Poll
from django.core.urlresolvers import reverse_lazy
admin.autodiscover()
from django.contrib.auth.decorators import user_passes_test
urlpatterns = patterns('',
	url(r'^', include('app.urls', namespace="app")),
	url(r'^contact$', 'app.views.contact', name='contact'),
    url(r'^student$', 'app.views.student',
        {
            'template_name': 'app/student.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
                'redirect_if_logged_in': 'home/',
                'next_page': 'home/',
            }
        },
        name='student'),
	url(r'^about', 'app.views.about', name='about'),
	url(r'^seed', 'app.views.seed', name='seed'),
	url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
                'redirect_if_logged_in': 'home/',
                'next_page': 'home/',
            }
        },
        name='login'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': 'home/',
        },
        name='logout'),
    url(r'^admin/', include(admin.site.urls)),
)
