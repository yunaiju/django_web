from django.shortcuts import render
#from django.http import HttpResponse
from .models import MainContent

# Create your views here.
def index(request):
    #return HttpResponse("Hello world")

    content_list = MainContent.objects.order_by('-pub_date') # - : 역순 # 최신순
    context = {'content_list': content_list}
    return render(request, 'mysite/content_list.html', context)