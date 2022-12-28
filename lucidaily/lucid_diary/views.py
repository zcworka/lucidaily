from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return render(request, 'lucid_diary/index.html')



def handle404(request, exception):
	return HttpResponse("Page not found...")