from django.contrib import admin
from .models import MovieDetails,Category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}
admin.site.register(Category,CategoryAdmin)

class MovieDetailsAdmin(admin.ModelAdmin):
    list_display=['title','description','release_date','actors','category']
    prepopulated_fields={'slug':('title',)}
admin.site.register(MovieDetails,MovieDetailsAdmin)