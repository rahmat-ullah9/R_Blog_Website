from django.contrib import admin
from .models import Category, Blogs
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category_name','created_category','updated_category')
    list_display_links =('category_name','id')
    
class BlogsAdmin(admin.ModelAdmin):
    list_display = ('id','title','category','author','status','is_featured','created_category','updated_category') #admin panel e kon info gulo dekhabe
    list_display_links =('title',)
    prepopulated_fields={'slug': ('title',)}
    search_fields = ('id','title','author__username') #admin panel e search bar e ki ki diye search korte parbe
    list_editable =('is_featured',) #admin panel e checkbox kinba form field hoish
admin.site.register(Category, CategoryAdmin)  
admin.site.register(Blogs, BlogsAdmin)
