from django.conf.urls import patterns, include, url
from homepage.views import hello, current_datetime, hours_ahead, index, about, specific_blog, projects, contact
from blog.views import blog, view_post, view_category
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
from filebrowser.sites import site
# Don't forget to add admin.autodiscover()!
# If not, you would not have a persmission to edit anything!
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'homepage.views.home', name='home'),
    # url(r'^homepage/', include('homepage.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
		
	url(r'^admin/filebrowser/',include(site.urls)),
  url(r'^admin/', include(admin.site.urls)),
	url(r'^$',index),
	url(r'^hello/$',hello),
	url(r'^time/$',current_datetime),
	url(r'^time/plus/(\d{1,2})/$', hours_ahead),
	url(r'^about/$',about),
	url(r'^blog/$',blog),
	url(r'^blog/category/(?P<slug>[^\.]+)',view_category,name='view_blog_category'),
	(r'^grappelli/', include('grappelli.urls')),
	url(r'^blog/(?P<slug>[^\.]+)',view_post,name='view_blog_post'),
  (r'^tinymce/', include('tinymce.urls')),
	url(r'^projects/$',projects),
	url(r'^contact/$',contact),
	(r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
)
urlpatterns += patterns(”,
 (r’^static/(?P.*)$’, ‘django.views.static.serve’, {‘document_root’: settings.STATIC_ROOT}),
 )