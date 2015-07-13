from django.conf.urls import patterns, url
from liquor_locator import views

urlpatterns = patterns('',
        # ^ indicates home. you enter through .../liquor_locator/
        # ^about/ indicates you enter through .../liquor_locator/about/
        url(r'^$', views.index, name='index'),
        url(r'^register/$', views.register, name='register'), 
        url(r'^login/$', views.user_login, name='login'),
        url(r'^restricted/', views.restricted, name='restricted'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^store/(?P<store_id>[a-z0-9 _]+)/$', views.store, name='store'),
        )