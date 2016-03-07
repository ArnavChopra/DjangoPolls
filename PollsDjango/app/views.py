"""
Definition of views.
"""
from django.contrib.auth.models import User
from django.contrib.auth.views import login
from app.models import Choice, Poll
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect,render_to_response
from django.template import RequestContext
from django.utils import timezone
from django.views.generic import ListView, DetailView
from os import path
from django.core.urlresolvers import reverse_lazy
import json
from django.contrib.auth.models import Group
# class PollListView(ListView):
#     """Renders the home page, with a list of all polls."""
#     model = Poll

#     def get_context_data(self, **kwargs):
#         context = super(PollListView, self).get_context_data(**kwargs)
#         context['title'] = 'Polls'
#         context['year'] = datetime.now().year
#         return context

# class PollDetailView(DetailView):
#     """Renders the poll details page."""
#     model = Poll

#     def get_context_data(self, **kwargs):
#         context = super(PollDetailView, self).get_context_data(**kwargs)
#         context['title'] = 'Poll'
#         context['year'] = datetime.now().year
#         return context

# class PollResultsView(DetailView):
#     """Renders the results page."""
#     model = Poll

#     def get_context_data(self, **kwargs):
#         context = super(PollResultsView, self).get_context_data(**kwargs)
#         context['title'] = 'Results'
#         context['year'] = datetime.now().year
#         return context

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title': 'Contact',
            'message': 'Your contact page.',
            'year': datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title': 'About',
            'message': 'Your application description page.',
            'year': datetime.now().year,
        })
    )

def vote(request, poll_id):
    """Handles voting. Validates input and updates the repository."""
    poll = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = poll.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'app/details.html', {
            'title': 'Poll',
            'year': datetime.now().year,
            'poll': poll,
            'error_message': "Please make a selection.",
    })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('app:results', args=(poll.id,)))

@login_required
def seed(request):
    """Seeds the database with sample polls."""
    samples_path = path.join(path.dirname(__file__), 'samples.json')
    with open(samples_path, 'r') as samples_file:
        samples_polls = json.load(samples_file)

    for sample_poll in samples_polls:
        poll = Poll()
        poll.text = sample_poll['text']
        poll.pub_date = timezone.now()
        poll.save()

        for sample_choice in sample_poll['choices']:
            choice = Choice()
            choice.poll = poll
            choice.text = sample_choice
            choice.votes = 0
            choice.save()

    return HttpResponseRedirect(reverse('app:home'))
'''def custom_login(request,**kwargs):
    if request.user.is_authenticated():
        return redirect(reverse_lazy('contact'))
    else:
        return redirect(reverse_lazy('login'))'''

def index(request):
    if request.user.is_authenticated():
        #return render(request, 'app/student.html',{})
        return redirect(reverse_lazy('student'))
    else:
        return redirect(reverse_lazy('login'))
def student(request,**kwargs):
    assert isinstance(request, HttpRequest)
    user_group=request.user.groups.all()
    return render(
        request,
        'app/studentmain.html',
        context_instance = RequestContext(request,
        {
            'title': 'Student',
            'year': datetime.now().year,
            'group_name': Group.objects.all(),
            'user':User.objects.all(),
            'user_group':request.user.groups.all()
        })
        )
def students(request,group_id=1):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/student.html',
        context_instance = RequestContext(request,
        {
            'title': 'Student',
            'year': datetime.now().year,
            'students':Group.objects.get(id=group_id),
            'user':User.objects.all(),
            'group_name': Group.objects.all(),
        })
        )
def prof(request,group_id=1):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/prof.html',
        context_instance = RequestContext(request,
        {
            'title': 'Student',
            'year': datetime.now().year,
            'students':User.objects.filter(groups__id=group_id),
            'user':User.objects.all(),
            'group_name': Group.objects.all(),
            'user_group':request.user.groups.all(),
        })
        )
'''def home(request):
    return render(request, "home.html", {'username':request.user.username})'''