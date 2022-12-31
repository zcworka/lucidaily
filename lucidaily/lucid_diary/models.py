from django.db import models
from django.contrib.auth.models import User
import hashlib

class Note(models.Model):

	title = models.CharField(max_length=255)
	content = models.TextField(blank=True)
	is_lucid = models.BooleanField(default=False)
	time_create = models.DateTimeField(auto_now_add=True, verbose_name="create date")
	time_update = models.DateTimeField(auto_now=True, verbose_name="update date")
	user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
	slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

	def save(self,  *args, **kwargs):

		self.slug = hashlib.sha256(b"Nobody inspects the spammish repetition").hexdigest()

		return super(Note, self).save(*args, **kwargs)