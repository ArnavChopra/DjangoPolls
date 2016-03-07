from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm

urlpatterns = patterns('',
    url(r'^all/$', 'app.views.student',
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
    url(r'^/get/(?P<group_id>\d+)/$','app.views.students'),
    url(r'^/prof/(?P<group_id>\d+)/$','app.views.prof'),
)
