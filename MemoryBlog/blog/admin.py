from django.contrib import admin
from .models import Section, Article, Subsection, ArticleStatistic, Comment

# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['article_title']}
    list_display = ('article_title', 'section', 'subsection', 'date', 'status')
    fieldsets = (
        (None, {
           'fields': ('article_title', 'slug', 'article_description', 'section', 'subsection', 'author', 'date', 'head_image', 'content', 'status', 'allow_comments')
        }),
        ('SEO параметры', {
            'fields': ('seo_title', 'seo_desription', 'seo_keywords')
        }),
    )

@admin.register(Subsection)
class SubsectionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'subsec_slug': ['name']}
    list_display = ('name', 'section', 'order_range')

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'sec_slug': ['name']}
    list_display = ('name', 'order_range')

@admin.register(ArticleStatistic)
class ArticleStatisticAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'date', 'views')
    search_fields = ('__str__', )

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article_id', 'author_id', 'pub_date', 'content')
    search_fields = ('author_id', 'content' )
    # list_filter = ('article_id', 'author_id', 'pub_date')

# admin.site.register(Comment)