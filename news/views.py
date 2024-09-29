from django.shortcuts import render, redirect
from .models import News
from news.forms import NewsForm
from django.contrib import messages

# Create your views here.

def news(request):
    """
    Display news
    """
    news = News.objects.all()
    
    # Add news
    if request.method == 'POST':
        
        form = NewsForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'News was added succssfuly')
            return redirect('news')
        else:
            messages.error(request, 'News was not added. Please try again')

    else:
        form = NewsForm()
            

    return render(request, 'news/news.html',{'news': news, 'form':form})

