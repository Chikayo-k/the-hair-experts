from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import News
from news.forms import NewsForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def news(request):
    """
    Display news
    """
    news = News.objects.all()               

    return render(request, 'news/news.html',{'news': news})


@login_required    
def news_add(request):
    """
    Add News 
    """
    if not request.user.is_superuser:
        messages.error(request, 'limited to store owners')
        return redirect(reverse('home'))

    if request.method =='POST':
        form = NewsForm(request.POST,request.FILES)
        if form.is_valid():
            news = form.save()
            messages.success(request, 'News was added successfully!')
            return redirect(reverse('news'))
        else:
            messages.error(request, 'Failed. Please try again!')
    else:
        form = NewsForm()
    template ='news/news_add.html'
    context ={
        'form':form,
    }

    return render(request,template,context)


@login_required 
def news_edit(request,news_id):
    """
    Edit news
    """
    if not request.user.is_superuser:
        messages.error(request, 'limited to store owners')
        return redirect(reverse('home'))

    news = get_object_or_404(News, pk=news_id)
    if request.method == 'POST':
        form= NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            messages.success(request,'Updated news successfully!')
            return redirect(reverse('news'))
        else:
            messages.error(request,'Failed to update news. Please try again.')
            
    else:
        form = NewsForm(instance=news)
        messages.info(request, f'You are editing {news.title}')

    template ='news/news_edit.html'
    context ={
        'form':form,
        'news':news,
    }

    return render(request,template,context)


@login_required 
def news_delete(request, news_id):
    """
    Delete news 
    """
    if not request.user.is_superuser:
        messages.error(request, 'limited to store owners')
        return redirect(reverse('home'))

    news = get_object_or_404(News, pk=news_id)
    news.delete()
    messages.success(request, f'News: {news.title} has been deleted!')
    return redirect(reverse('news'))




