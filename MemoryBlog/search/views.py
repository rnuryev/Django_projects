from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Article
# Create your views here.

def search(request):
    question = request.GET.get('q')
    if question is not None:
        search_articles = Article.objects.filter(content__search=question)
        last_question = '?q=%s' % question

    paginator = Paginator(search_articles, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'search/search_result.html', {'page': page, 'posts': posts, 'last_question': last_question, 'question': question})