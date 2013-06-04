from blog.models import Posts, Category, Comment, CommentForm
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.forms.models import inlineformset_factory

def blog(request):
	all_posts = Posts.objects.all().order_by('-date')[:5]
	num_comment_list = list()
	for post in all_posts:
		num_post = Comment.objects.filter(parent=post).count()
		num_comment_list.append(num_post)		
	return render_to_response('blog.html',{'categories' : Category.objects.all(), 'posts':all_posts,'num_posts':Posts.objects.count(), 'num_comments':num_comment_list})

def view_post(request, slug):
	post = get_object_or_404(Posts,slug=slug)
	ParentInlineFormSet = inlineformset_factory(Posts,Comment,extra=1,form=CommentForm)
	if request.method == 'POST':
		form = ParentInlineFormSet(request.POST, request.FILES, instance=post)
		if form.is_valid():
	#		name = form.clean_data['name']
	#		password = form.clean_data['password']
	#		email = form.clean_data['email']
	#		content = form.clean_data['content']
	#		Comment.objects.create(name=name, password=password, email=email,content=content,parent=post)
			form.save()
			return HttpResponseRedirect(post.get_absolute_url())
	else:
		form = ParentInlineFormSet(instance=post)
		#form = CommentForm()
	comments = Comment.objects.filter(parent=post)
	return render_to_response('view_post.html',{'categories':Category.objects.all(),'post':post,'comments':comments,'form':form}, context_instance=RequestContext(request))

def view_category(request, slug):
	c = get_object_or_404(Category, slug=slug)
	return render_to_response('view_category.html',{'category':c,'posts':Posts.objects.filter(category=c).order_by('-date')})