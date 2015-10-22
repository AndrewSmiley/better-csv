from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'better_csv_web.views.index', name='index'),
    url(r'^batch_selection/', 'better_csv_web.views.batch_selection', name='batch_selection'),
    url(r'^run_batch/', 'better_csv_web.views.run_batch', name='run_batch'),
    url(r'^file_upload/', 'better_csv_web.views.file_upload', name='file_upload'),
    url(r'^download_list/', 'better_csv_web.views.download_list', name='download_list'),
    url(r'^download/', 'better_csv_web.views.download', name='download'),
    url(r'^view_data_selection/', 'better_csv_web.views.view_data_selection', name='view_data_selection'),
    url(r'^view_data/', 'better_csv_web.views.view_data', name='view_data'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
