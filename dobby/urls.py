from django.conf.urls import patterns, url

urlpatterns = patterns('dobby.views',

    url(r'^$', 'search_form'),
    url(r'result/', 'index'),

    url(r'^products/$', 'product_list'),
    url(r'^products/(?P<pk>[0-9]+)/$', 'product_detail'),

    # Uncomment the next line to enable the admin:

)
