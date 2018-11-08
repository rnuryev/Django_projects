from django import template
from django.db.models import Sum
from django.utils import timezone

from blog.models import ArticleStatistic, Subsection, Article, Section

register = template.Library()

@register.simple_tag
def get_popular_articles_for_week():

    popular = ArticleStatistic.objects.filter(
        # отфильтровываем записи за последние 7 дней
        date__range=[timezone.now() - timezone.timedelta(7), timezone.now()]
    ).values(
        # Забираем интересующие нас поля, а именно id и заголовок
        # К сожалению забрать объект по внешнему ключу в данном случае не получится
        # Только конкретные поля из объекта
        'article__slug', 'article__article_title', 'article__date', 'views', 'article__id',
    ).annotate(
        # Суммируем записи по просмотрам
        sum_views=Sum('views')
    ).order_by(
        # отсортируем записи по убыванию
        '-sum_views')[:4]    # Заберём последние пять записей

    return popular

@register.simple_tag
def get_all_subsection():
    all_subsections = Subsection.objects.all()
    sec_list = []
    for sec in all_subsections:
        sec_list.append((sec, Article.objects.filter(subsection=sec.id).count()))
    return sec_list

@register.simple_tag
def get_all_subsection_in_section(section):
    all_subsections = Subsection.objects.filter(section=section)
    sec_list = []
    for sec in all_subsections:
        sec_list.append(sec)
    return sec_list


@register.simple_tag
def get_all_section():
    all_sections = Section.objects.all()
    section_list = []
    for sec in all_sections:
        section_list.append(sec)
    return section_list

@register.simple_tag
def get_comments_count(post_id):
    post = Article.objects.get(id=post_id)
    return post.comment_set.count()
