from django.conf.urls import url, include

import contacts.views

from django.contrib import admin
from django.contrib.auth import views as auth_views

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^$', contacts.views.ListContactView.as_view(),
        name='contacts-list',),
    url(r'^view$', contacts.views.ListContactView.as_view(),
        name='contacts-list',),
    url(r'^new$', contacts.views.CreateContactView.as_view(),
        name='contacts-new',),
    url(r'^edit/(?P<pk>\d+)/$', contacts.views.UpdateContactView.as_view(),
        name='contacts-edit',),
    url(r'^(?P<pk>\d+)/$', contacts.views.ContactView.as_view(),
        name='contacts-view',),
    url(r'^delete/(?P<pk>\d+)/$', contacts.views.DeleteContactView.as_view(),
        name='contacts-delete',),
    url(r'^admin/', include(admin.site.urls)),
]
