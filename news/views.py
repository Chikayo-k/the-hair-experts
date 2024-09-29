from django.shortcuts import render, redirect
from .models import News
from news.forms import NewsForm

# Create your views here.

def news(request):
    news = News.objects.all()

    if request.method == 'POST':
        form = NewsForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('news')
    else:
        form = NewsForm()
            

    return render(request, 'news/news.html',{'news': news, 'form':form})