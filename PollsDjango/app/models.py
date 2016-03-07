"""
Definition of models.
"""
from datetime import datetime 
from django.db import models
from django.db.models import Sum

class Poll(models.Model):
    courseid = models.IntegerField(default=0)
    qrstring = models.CharField(max_length=200, default = ' ')
    is_active = models.IntegerField(default=0)
    created_at = models.DateTimeField(null=True)
    
    '''def total_votes(self):
        """Calculates the total number of votes for this poll."""
        return self.choice_set.aggregate(Sum('votes'))['votes__sum']'''

    def __unicode__(self):
        """Returns a string representation of a poll."""
        return self.text

class Choice(models.Model):
    qr_id = models.IntegerField(default=0)
    studentid = models.IntegerField(default=0)
    is_present = models.IntegerField(default=0)
    created_at = models.DateTimeField(null=True)
    
    '''def votes_percentage(self):
        """Calculates the percentage of votes for this choice."""
        total = self.poll.total_votes()
        return self.votes / float(total) * 100 if total > 0 else 0'''

    def __unicode__(self):
        """Returns a string representation of a choice."""
        return self.text
"""
Definition of models.
"""
from datetime import datetime 
from django.db import models
from django.db.models import Sum

class Qr(models.Model):
    courseid = models.IntegerField(default=0)
    qrstring = models.CharField(max_length=200, default = ' ')
    is_active = models.IntegerField(default=0)
    created_at = models.DateTimeField(null=True)
    
    '''def total_votes(self):
        """Calculates the total number of votes for this poll."""
        return self.choice_set.aggregate(Sum('votes'))['votes__sum']'''

    def __unicode__(self):
        """Returns a string representation of a poll."""
        return self.text

class Attendance(models.Model):
    qr_id = models.IntegerField(default=0)
    studentid = models.IntegerField(default=0)
    is_present = models.IntegerField(default=0)
    created_at = models.DateTimeField(null=True)
    
    '''def votes_percentage(self):
        """Calculates the percentage of votes for this choice."""
        total = self.poll.total_votes()
        return self.votes / float(total) * 100 if total > 0 else 0'''

    def __unicode__(self):
        """Returns a string representation of a choice."""
        return self.text
