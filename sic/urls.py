from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('info.urls')),
    path('lms/', include('lms.urls')),
    path('auth/', include('userauth.urls')),
]

from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
admin.site.site_header = "SIC Admin"
admin.site.index_title = "SIC Index"
admin.site.site_title = "SIC Admin Portal"
