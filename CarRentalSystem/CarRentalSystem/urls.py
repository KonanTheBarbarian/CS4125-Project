from django.conf import settings

from django.contrib import admin
from django.urls import path, include
if settings.DEBUG:
    import debug_toolbar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('crs/', include('crs.urls', namespace='crs')),
    path('__debug__/', include(debug_toolbar.urls)),

]
