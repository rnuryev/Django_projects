from django.shortcuts import render, get_object_or_404, redirect
from .models import Section, Article, Subsection, ArticleStatistic, Comment
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from .forms import CommentForm
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response
from django.template import RequestContext


# Create your views here.

def post_list(request, subsec_slug=None, sec_slug=None, author=None):
    all_posts = Article.objects.all().filter(status='опубликован').order_by('-date')
    if sec_slug and subsec_slug:
        sec = get_object_or_404(Section, sec_slug=sec_slug)
        subsec = get_object_or_404(Subsection, subsec_slug=subsec_slug)
        all_posts = all_posts.filter(section__in=[sec]).filter(subsection__in=[subsec]).filter(status='опубликован').order_by('-date')
    else:
        if subsec_slug:
            subsec = get_object_or_404(Subsection, subsec_slug=subsec_slug)
            all_posts = all_posts.filter(subsection__in=[subsec]).filter(status='опубликован').order_by('-date')
        if sec_slug:
            sec = get_object_or_404(Section, sec_slug=sec_slug)
            all_posts = all_posts.filter(section__in=[sec]).filter(status='опубликован').order_by('-date')
        if author:
            auth_post = get_object_or_404(User, username=author)
            all_posts = all_posts.filter(author__in=[auth_post]).filter(status='опубликован').order_by('-date')
    paginator = Paginator(all_posts, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post_list.html', {'page': page, 'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Article, slug=slug)

    obj, created = ArticleStatistic.objects.get_or_create(
        defaults={
            "article": post,
            "date": timezone.now()
        },
        # При этом определяем, забор объекта статистики или его создание
        # по двум полям: дата и внешний ключ на статью
        date=timezone.now(), article=post
    )
    obj.views += 1  # инкрементируем счётчик просмотров и обновляем поле в базе данных
    obj.save(update_fields=['views'])

    comments = post.comment_set.all().order_by('path')
    next = post.get_absolute_url()

    user = auth.get_user(request)
    if user.is_authenticated:
        form = CommentForm
        return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'next': next, 'form': form})
    else:
        return render(request, 'blog/post_detail.html',
                      {'post': post, 'comments': comments, 'next': next})


@login_required
@require_http_methods(["POST"])
def add_comment(request, article_id):
    form = CommentForm(request.POST)
    article = get_object_or_404(Article, id=article_id)

    if form.is_valid():
        comment = Comment()
        comment.path = []
        comment.article_id = article
        comment.author_id = auth.get_user(request)
        comment.content = form.cleaned_data['comment_area']
        comment.save()

        # Django не позволяет увидеть ID комментария по мы не сохраним его,
        # хотя PostgreSQL имеет такие средства в своём арсенале, но пока не будем
        # работать с сырыми SQL запросами, поэтому сформируем path после первого сохранения
        # и пересохраним комментарий
        try:
            comment.path.extend(Comment.objects.get(id=form.cleaned_data['parent_comment']).path)
            comment.path.append(comment.id)
        except ObjectDoesNotExist:
            comment.path.append(comment.id)

        comment.save()

    return redirect(article.get_absolute_url())

def handler404(request, exception, template_name='404.html'):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response