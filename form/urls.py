from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from form.models import Contactform

urlpatterns = [ url(r'^$', ListView.as_view(queryset=Contactform.objects.all().order_by("-date"), template_name="form/form.html"))]

	

# Create your models here.
