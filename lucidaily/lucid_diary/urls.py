from django.urls import path
from .views import *

urlpatterns = [
	path('', index, name='home'),
	path('signup', RegisterUser.as_view(), name='register'),
	path('login', LoginUser.as_view(), name='login'),
	path('profile', profile, name='profile'),
	path('logout_user', logout_user, name='logout_user'),
	path('workspace', workspace, name='workspace'),
	path('edit', edit, name='edit'),
	path('workspace/view', view, name='view'),
] 
