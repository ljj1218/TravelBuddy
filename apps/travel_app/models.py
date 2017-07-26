from __future__ import unicode_literals
from ..login_app.models import User
from django.db import models
from datetime import date
import datetime

class TravelManager(models.Manager):
    def createTrip(self, postData):
        results  = {
            'status': True, 
            'errors': [], 
        }
        if len(postData['destination']) < 1:
			results['status'] = False
			results['errors'].append('No empty entry')
        if len(postData['plan'])<1:
			results['status'] = False
			results['errors'].append('No empty entry')
        # today does not work
        # if postData['datefrom'] < datetime.date.today():
        #     results['status'] = False
        #     results['errors'].append('Further date')
        if postData['datefrom'] > postData['dateend']:
            results['status'] = False
            results['errors'].append('Check dateto')
        return results

class Travel(models.Model):
    destination = models.CharField(max_length = 50)
    planedby = models.ForeignKey(User, default= None)
    datefrom = models.DateField()
    dateend = models.DateField()
    plan = models.TextField(max_length=500)
    objects = TravelManager()