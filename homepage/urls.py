from django.conf.urls import patterns, include, url
from homepage.views import hello, current_datetime, hours_ahead, index, about, blog, specific_blog, projects, contact
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'homepage.views.home', name='home'),
    # url(r'^homepage/', include('homepage.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
	url(r'^$',index),
	url(r'^hello/$',hello),
	url(r'^time/$',current_datetime),
	url(r'^time/plus/(\d{1,2})/$', hours_ahead),
	url(r'^about/$',about),
	url(r'^blog/$',blog),
	url(r'^blog/\d+/$',specific_blog),
	url(r'^projects/$',projects),
	url(r'^contact/$',contact),
)
