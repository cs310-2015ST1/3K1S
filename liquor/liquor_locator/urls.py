from django.conf.urls import patterns, url
from liquor_locator import views

urlpatterns = patterns('',
        # ^ indicates home. you enter through .../liquor_locator/
        # ^about/ indicates you enter through .../liquor_locator/about/
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^add_category/$', views.add_category, name='add_category'), # NEW MAPPING!
        url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),)