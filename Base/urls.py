from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
import views

urlpatterns = [
    url(r'^(?P<filename>(robots.txt)|(humans.txt))$', 
        views.home_files, name="home_files"),
]

urlpatterns += i18n_patterns(
        url(r'^admin/', include(admin.site.urls)),
        url(r'^$', views.home, name='home'),
)
