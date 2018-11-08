from django.contrib import admin
from .models import Company, Animator, SchoolProgram
#
# class StudioInline(admin.TabularInline):
#     model = Studio
#     extra = 0


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'district', 'is_school', 'is_studio')
    list_filter = ('district', )
    fieldsets = (
        ('Данные по компании', {
            'fields': ('name', 'description', 'district', ('is_school', 'is_studio'))
        }),
        ('Контакты компании', {
            'fields': (('adress', 'phone'), ('email', 'site'),)
        }),
        ('Информация о школе', {
            'fields': ('school_desctiption',)
        }),
        ('Информация о студии', {
            'fields': (('studio_aria', 'studio_cost'), 'own_animators', 'studio_condition')
        }),
    )
    # inlines = [StudioInline, SchoolInline]
    readonly_fields = ('school_desctiption', 'studio_aria', 'studio_cost', 'studio_condition', 'own_animators')
    def get_readonly_fields(self, request, obj=None):
        if obj:
            self.readonly_fields = ('school_desctiption', 'studio_aria', 'studio_cost', 'studio_condition', 'own_animators')
            if obj.is_studio == True and obj.is_school == True:
                self.readonly_fields = ()
            else:
                if obj.is_school == True:
                    self.readonly_fields = ('studio_aria', 'studio_cost', 'studio_condition', 'own_animators')
                elif obj.is_studio == True:
                    self.readonly_fields = ('school_desctiption')
        return self.readonly_fields


# admin.site.register(Company)
admin.site.register(Animator)
admin.site.register(SchoolProgram)