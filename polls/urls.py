from django.conf.urls import patterns, url

urlpatterns = patterns('polls.views',

    url(r'^$', 'index'),
    url(r'^(?P<poll_id>\d+)/$', 'detail'),
    url(r'^(?P<poll_id>\d+)/results/$', 'results'),
    url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
    # Uncomment the next line to enable the admin:

)
