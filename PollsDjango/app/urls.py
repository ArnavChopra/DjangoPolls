"""
Definition of urls for polls viewing and voting.
"""
from datetime import datetime
from django.conf.urls import patterns, url
from app.models import Poll
from app.views import PollListView, PollDetailView, PollResultsView
from app.forms import BootstrapAuthenticationForm

urlpatterns = patterns('',
    url(r'^$', 'app.views.index'),
    url(r'^(?P<user_id>\d+)/$','app.views.student',name='student'),
    url(r'^$',
        PollListView.as_view(
            queryset=Poll.objects.order_by('-pub_date')[:5],
            context_object_name='latest_poll_list',
            template_name='app/index.html',),
        name='ahome'),
    url(r'^(?P<pk>\d+)/$',
        PollDetailView.as_view(
            template_name='app/details.html'),
        name='detail'),
    url(r'^(?P<pk>\d+)/results/$',
        PollResultsView.as_view(
            template_name='app/results.html'),
        name='results'),
    url(r'^(?P<poll_id>\d+)/vote/$', 'app.views.vote', name='vote'),
    url(r'^home/$',
        PollListView.as_view(
            queryset=Poll.objects.order_by('-pub_date')[:5],
            context_object_name='latest_poll_list',
            template_name='app/index.html',),
        name='home'),
)
