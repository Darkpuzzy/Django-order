from django.contrib import admin
from django.urls import path, include
from apiord.urls import doc_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apiord.urls')),
    path('docs/', include(doc_url))
]
