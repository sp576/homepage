from django.contrib import admin
from blog.models import Posts, Category, Comment

class BlogAdmin(admin.ModelAdmin):
	exclude = ['date']
	prepopulated_fields = {'slug':('title',)}

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('title',)}
	
class CommentAdmin(admin.ModelAdmin):
	exclude = ['date']
	#prepopulated_fields = {'slug':('title',)}

admin.site.register(Posts, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)