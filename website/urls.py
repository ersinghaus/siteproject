from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from Website.core import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^uploads/form/$', views.upload, name='upload'),
    url(r'^about/', views.about, name='about'),
    url(r'^math/', views.math, name= 'math'),
    url(r'^english/', views.english, name= 'english'),
    url(r'^science/', views.science, name= 'science'),
    url(r'^art/', views.art, name= 'art'),
    url(r'^history/', views.history, name= 'history'),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
