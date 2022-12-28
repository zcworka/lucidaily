from django.db import models
from django.db.models import *


class User(models.Model):

	nick_name = TextField()
	email = EmailField()
	password = TextField()

	def __str():
		return self.nick_name
 