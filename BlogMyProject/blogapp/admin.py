from django.contrib import admin
from blogapp.models import Post,Comments,Login
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish','created','updated','status']

    list_filter=('status','author')
    Search_Fields=('title','body')
    row_id_fields=('author')
    ordering=('created',)
    prepopulated_fields={'slug':('title',)}

admin.site.register(Post,PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display=['id','name','email','post','body','created','updated','active']
    list_filter=['active','created','updated']
    Search_Fields=['name','email','body']

admin.site.register(Comments,CommentAdmin)

class LoginAdmin(admin.ModelAdmin):
    list_display=['id','Username','CreatePassword','RetypePassword']

admin.site.register(Login,LoginAdmin)
