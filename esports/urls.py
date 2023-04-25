from django.contrib import admin
from django.urls import path,include
admin.site.site_header="13 Hopes"
admin.site.site_title ="Admin 13 Hopes"
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('commerce.urls')),
    path('',include('userapp.urls')),
]
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)