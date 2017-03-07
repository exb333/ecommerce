from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from shopping import views
from .views import (
        home,
        contact,
)

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^contact/$', contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
