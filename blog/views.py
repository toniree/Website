from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
	return render(request, 'blog/home.html')
@csrf_exempt
def contact(request):
	return render(request, 'blog/basic.html', {'content':['Email me','tonilee@berkeley.edu']})


# Create your views here.
