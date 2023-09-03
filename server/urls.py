"""django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from .views.media import delete_all_medias
from .views.media import delete_media
from .views.media import download_original
from .views.media import download_converted
from .views.media import upload_and_convert
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from . import views


from rest_framework.routers import DefaultRouter
from .views.media import MediaViewSet
router = DefaultRouter()
router.register(r'media', MediaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('api/hello-world', views.hello_world),
    # OAuth2
    # re_path(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # Medias
    path('api/', include(router.urls)),
    path('api/upload_and_convert/', upload_and_convert, name='upload_and_convert'),
    path('api/download_original/', download_original, name='download_original'),
    path('api/download_converted/', download_converted, name='download_converted'),
    path('api/delete_media/<int:media_id>', delete_media, name='delete_media'),
    path('api/delete_all_medias/', delete_all_medias, name='delete_all_medias'),

]

handler400 = 'server.views.error.handler400'
handler403 = 'server.views.error.handler403'
handler404 = 'server.views.error.handler404'
handler500 = 'server.views.error.handler500'

admin.site.site_header = 'Administration du projet'
admin.site.site_title = 'Projet Administration'
