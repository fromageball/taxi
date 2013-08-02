from django.shortcuts import render_to_response
from blog.models import posts, postsImages
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import Context, loader
from django.http import Http404
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.dates import YearArchiveView
from django.views.generic.dates import MonthArchiveView







# Create your views here.
		
def home(request):
	entries = posts.objects.all()[:10]
	paginator = Paginator(entries, 10)
	page = request.GET.get('page')
	try:
		blogs = paginator.page(page)
	except PageNotAnInteger:
		blogs = paginator.page(1)
	except EmptyPage:
		blogs = paginator.page(paginator.num_pages)
	return render(request, 'index.html', {'posts' : entries, 'blogs' : blogs})
	
def index(request):
	entry = posts.objects.filter(published=True)
	return render(request, 'blog/index.html', {'posts':posts})

def single(request, slug):
	entry = posts.objects.filter(slug=slug)
	return render(request, 'blog/single.html', {'posts':entry})

def about(request):
	return render(request, 'blog/about.html')
def archive(request):
	return render(request, 'blog/archive.html')

def search(request):
	return render(request, 'blog/search.html')
	
def contact(request):
	return render(request, 'blog/contact.html')
	
def archive(request):
	return render(request, 'blog/archive.html')

def theindustry(request):
	return render(request, 'blog/theindustry.html')
	
class BlogYearArchiveView(YearArchiveView):
	queryset = posts.objects.all()
	date_field = "timestamp"
	make_object_list = True
	allow_future = True

class BlogMonthArchiveView(MonthArchiveView):
	queryset = posts.objects.all()
	date_field = "timestamp"
	make_object_list = True
	allow_future = True
	
	


	
	
	
	
