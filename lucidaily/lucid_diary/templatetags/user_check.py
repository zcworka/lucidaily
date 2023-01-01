from django import template
from lucid_diary.models import *

register = template.Library()

@register.simple_tag(name='user_check', takes_context=True)
def check_user(context):

	user_id = context['request'].user.pk
	note_slug = context['note'].slug
	
	if User.objects.filter(id=user_id).exists():
		user = User.objects.filter(id=user_id)[0]
		if Note.objects.filter(slug=note_slug).exists():
			return True
	else:
		return False

	return False
	

	