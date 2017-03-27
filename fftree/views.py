from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Brother

# Create your views here.
def index(request):
	return HttpResponse("Hello World")
	#brother_list = Brother.objects.order_by('-init_year')
	#context = {'brother_list': brother_list,}
	#return render(request, 'fftree/index.html', context)

def pledgeClass(request, init_year):
	return HttpResponse("You're looking at brothers in the %s pledge class." % init_year)

def brother(request, brother_id):
	#return HttpResponse("You're looking at brother %s." % brother_id)
	#try:
	#	brother = Brother.objects.get(pk=brother_id)
	#except Brother.DoesNotExist:
	#	raise Http404("Brother does not exist")
	#return render(request, 'fftree/brother.html', {'brother': brother})
	brother = get_object_or_404(Brother, pk=brother_id)
	return render(request, 'fftree/brother.html', {'brother': brother})

def comment(request, brother_id):
	return HttpResponse("You're commenting on brother %s." % brother_id)