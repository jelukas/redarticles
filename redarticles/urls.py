from django.conf.urls import patterns, include, url
#Para los ficheros estaticos
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^', include('blog.urls')),
    url(r'^inplaceeditform/', include('inplaceeditform.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns =+ static(settings.STATIC_URL = '', document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()