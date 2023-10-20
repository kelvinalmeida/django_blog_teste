from django.shortcuts import render
from .models import Article
from .forms import ArticleForm

# Create your views here.

def article_list_view(request):

    queryset = Article.objects.all()

    my_ctx = {
        "article_list": queryset,
    }
      
    return render(request, 'article/article_list.html', my_ctx)

def article_detail_view(request, id):

    obj = Article.objects.get(id=id)

    my_ctx = {
        "obj": obj,
    }
      
    return render(request, 'article/article_detail.html', my_ctx)

def article_crate_view(request):

    form = ArticleForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = ArticleForm()

    my_ctx = {
        "form": form,
    }
      
    return render(request, 'article/article_create.html', my_ctx)