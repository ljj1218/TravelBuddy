from __future__ import unicode_literals
from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def registerVal(self, postData):
        results = {
            'status': True,
            'errors': [],
            'user': None
        }
        if len(postData['name']) < 3:
            results['status'] = False
            results['errors'].append('Name must be at least 3 chars.')
        if len(postData['username']) < 3:
            results['status'] = False
            results['errors'].append('Username must be at least 3 chars.')
        if len(postData['password']) < 8 or postData['password'] != postData['c_password']:
            results['status'] = False
            results['errors'].append('Please enter a valid password.')
        if results['status'] == True:
            user = User.objects.filter(username = postData['username'])
            if len(user) != 0:
                results['status'] = False
                results['errors'].append('Username already exsit.')
        return results
    def createUser(self, postData):
        user = User.objects.create(name=postData['name'], username=postData['username'], password=postData['password'])
        return user
    def loginVal(self, postData):
        results = {
            'status': True,
            'errors': [],
            'user': None
        }
        results['user'] = User.objects.filter(username = postData['username'])
        if len(results['user']) < 1:
            results['status'] = False
            results['errors'].append('Username does not exist in the system.')
        else:
            if postData['password'] != results['user'][0].password:
                results['status'] = False
                results['errors'].append('The password does not match the username.')
        return results

class User(models.Model):
    name = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    objects = UserManager()

