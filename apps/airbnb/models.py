# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	age = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Rental(models.Model):
	city = models.CharField(max_length=255)
	user = models.ForeignKey(User, related_name="rentals")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Reservation(models.Model):
	rental = models.ForeignKey(Rental, related_name="reservations")
	user = models.ForeignKey(User, related_name="reservations")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

if (request.session["words"]){
	
}else{
	request.session["words"] = []
}
try:
	pass
except Exception as e:
	print e
	raise
else:
	pass
finally:
	pass