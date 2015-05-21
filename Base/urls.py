from django.conf.urls import include, url
from django.core.urlresolvers import reverse
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.contrib.auth import views as auth_views
import views

urlpatterns = [
    url(r'^(?P<filename>(robots.txt)|(humans.txt))$', 
        views.home_files, name="home_files"),
 
    url(r'^accounts/login/$', 
        auth_views.login, {'template_name': 'base/login.html'}),
    
    url(r'^change-password/$', 
        auth_views.password_change, 
        {'template_name': 'base/change-password.html',
         'post_change_redirect': '/'  }),    

    url(r'^accounts/logout/$', 
        auth_views.logout, {'next_page': "/"}), 
    url(r'i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
        url(r'^admin/', include(admin.site.urls)),
        url(r'^$', views.home, name='home'),
)
