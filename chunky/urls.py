from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^edit_api$', 'chunky.views.edit_api', name='chunky_edit_api'),
)
