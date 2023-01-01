from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt

from .forms import *
from .models import *


def index(request):
	return render(request, 'lucid_diary/index.html')

def login(request):
	return render(request, 'lucid_diary/login.html')

def signup(request):
	return render(request, 'lucid_diary/signup.html')

def workspace(request):
	for n in Note.objects.filter(user_id=request.user.pk):
		print(n.time_update)
	return render(request, 'lucid_diary/workspace.html', {'notes': Note.objects.filter(user_id=request.user.pk)})

def edit(request):
	return render(request, 'lucid_diary/edit.html')

@csrf_exempt
def view(request):
	if request.method == 'POST':
		print('====', request.POST.get('safer'), '=====', sep='\n')
		return render(request, 'lucid_diary/view.html', {'note': Note.objects.get(slug=request.POST.get('safer'))})
	else:
		return HttpResponse("000")



def handle404(request, exception):
	return HttpResponse("Page not found...")

def profile(request):
	return render(request, 'lucid_diary/profile.html')

def logout_user(request):
	logout(request)
	return redirect('home')



class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'lucid_diary/signup.html'
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
	form_class = AuthenticationUserForm
	template_name = 'lucid_diary/login.html'

	def get_success_url(self):
		return reverse_lazy('home')