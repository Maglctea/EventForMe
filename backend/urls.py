"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg.openapi import Info, Contact, License
from rest_framework.permissions import AllowAny
from jet import urls as jet_urls
from django.views.static import serve
import os

schema_view = get_schema_view(
    Info(
        title='Eventforme',
        default_version='1.0',
        description='full documentation api',
        contact=Contact(email='pentegov_92@mail.ru'),
        license=License(name='MIT')
    ),
    public=True,
    permission_classes=(AllowAny,)
)

urlpatterns = [
    path('jet/', include(jet_urls, 'jet')),  # Django JET URLS
    path('admin/', admin.site.urls),
    re_path('^api/v(?P<version>(1|1))/', include('authapp.urls', namespace='authapp')),
    re_path('^api/v(?P<version>(1|1))/catalog/', include('catalogapp.urls', namespace='catalog')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('swagger/', schema_view.with_ui()),
    path('api-auth/', include('rest_framework.urls')),
    path('fp/', include('django_drf_filepond.urls')),
    re_path(r'^demo/(?P<path>.*)$', serve, {'document_root': os.path.join(settings.BASE_DIR, 'static')}),
    path('auth/', include('authapp.urls')),
    path('accounts/', include('allauth.urls')),
    path('auth/', include('rest_framework_social_oauth2.urls'))
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
