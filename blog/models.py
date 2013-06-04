from django.db import models
from django import forms
from django.forms import widgets, Textarea
from django.db.models import permalink
from tinymce.models import HTMLField
from datetime import datetime
from filebrowser.fields import FileBrowseField

#learning it from
#http://www.djangorocks.com/tutorials/how-to-create-a-basic-blog-in-django/defining-your-models.html
class Posts(models.Model):
	title = models.CharField(max_length=100, unique=True)
	content = HTMLField()
	category = models.ForeignKey('blog.Category')
	slug = models.SlugField(max_length=100, unique=True)
	date = models.DateTimeField(default=datetime.now)
	image = FileBrowseField("image",max_length=200,extensions=[".jpg",".png"],blank=True,null=True)
	def __unicode__(self):
		return '%s' % self.title
	@permalink
	def get_absolute_url(self):
		return ('view_blog_post',None,{ 'slug':self.slug})
class Category(models.Model):
	title = models.CharField(max_length=100, db_index=True)
	slug = models.SlugField(max_length=100, db_index=True)
	def __unicode__(self):
		return '%s' % self.title
	@permalink
	def get_absolute_url(self):
		return ('view_blog_category',None,{ 'slug':self.slug})
	
class Comment(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	date = models.DateTimeField(default=datetime.now)
	#password = forms.CharField(max_length=32,widget=forms.PasswordInput)
	content = models.TextField()
	parent = models.ForeignKey('blog.Posts')
	def __unicode__(self):
		return '%s' % self.name
	
# replaced with inlineModelForm	
class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		#exclude = ('parent',)
		fields = ['name','email','content']
		widgets = {
			'content': Textarea(attrs={'cols':200, 'rows':10})
		}