from django.contrib import admin
from .models import BlogPost,Category,Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','pub_date','author','status')
    list_filter = ('status',)
    search_fields = ('title','content')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(BlogPost,PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)