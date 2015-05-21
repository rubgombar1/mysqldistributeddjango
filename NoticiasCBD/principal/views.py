from django.shortcuts import render
from principal.models import Noticia

# Create your views here.
def news(request):
    news = Noticia.objects.all()
    return render(request, 'news.html', {'news' : news})