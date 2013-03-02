from django.conf.urls import patterns, url
from sheetapp import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cutimesheet.views.home', name='home'),
    # url(r'^cutimesheet/', include('cutimesheet.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.index, name='index'),

    #url(r'^cutimesheet/', views.index, name='index'),

    url(r'^(?P<sheet_id>\d+)/edit/$', views.edit, name='edit'),
    url(r'^(?P<sheet_id>\d+)/create/$', views.create, name='create'),
    url(r'^(?P<sheet_id>\d+)/submit/$', views.submit, name='submit'),
    url(r'^(?P<sheet_id>\d+)/review/$', views.review, name='review'),
    url(r'^(?P<sheet_id>\d+)/approve/$', views.approve, name='approve'),
    url(r'^(?P<sheet_id>\d+)/decline/$', views.decline, name='decline'),
    url(r'^(?P<user_id>\d+)/list/$', views.list, name='list'),

    url(r'^login/$', 'django.contrib.auth.views.login',name="my_login"),
)
