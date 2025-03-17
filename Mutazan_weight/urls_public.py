"""
URL configuration for Mutazan_weight project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from companies_manager.admin import tenant_admin_site
from companies_manager.views import *
from django.conf.urls.i18n import set_language
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from companies_manager.views import CustomTokenObtainPairView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_tenants/', tenant_admin_site.urls),
    # path('', include('admin_adminlte.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('system_companies.urls')),
    path('set_language/', set_language, name='set_language'),
    path('api/', include('companies_manager.urls')),  # تأكد من أن المسارات الخاصة بالـ API موجودة في ملف `urls.py` الخاص بالشركات
     # الحصول على التوكن
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
     # تجديد التوكن
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # تسجيل الدخول والحصول على التوكن
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # تجديد التوكن عند انتهاء صلاحيته
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


