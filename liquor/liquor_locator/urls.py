from django.conf.urls import patterns, url
from liquor_locator import views

urlpatterns = patterns('',
        # ^ indicates home. you enter through .../liquor_locator/
        # ^about/ indicates you enter through .../liquor_locator/about/
        url(r'^$', views.index, name='index'),
        url(r'^register/$', views.register, name='register'), 
        url(r'^session/$', views.user_session, name='session'),
        url(r'^restricted/', views.restricted, name='restricted'),
        url(r'^store/(?P<store_id>[a-z0-9 _]+)/$', views.store, name='store'),
        url(r'^delete/(?P<comment_id>[a-z0-9 _]+)/(?P<store_id>[a-z0-9 _]+)/$', views.deleteComment, name='deletecomment'),
        url(r'^edit/(?P<comment_id>[a-z0-9 _]+)/(?P<store_id>[a-z0-9 _]+)/$', views.editComment, name='editcomment'),
        url(r'^favorites/$', views.favorites, name='favorites'),
        url(r'^addToFavorites/(?P<store_id>[a-z0-9 _]+)/$', views.addToFavorites, name='addToFavorites'),
        url(r'^deleteFromFavorites/(?P<store_id>[a-z0-9 _]+)/$', views.deleteFromFavorites, name='deleteFromFavorites'),
        )