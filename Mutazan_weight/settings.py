"""
Django settings for a_core project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-rj#-z^kx3j+1ay397otg6j8m_8#v^$^$jys6&41vy^&6le)ezc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '*']

CSRF_TRUSTED_ORIGINS = [ 'https://*' ]


# Application definition

SHARED_APPS = [
    'django_tenants',
    # 'admin_adminlte.apps.AdminAdminlteConfig',
    'jazzmin',
    'companies_manager',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_htmx',
    'allauth',
    'allauth.account',
]

TENANT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'system_companies',
]



# ==================================================================
# ==================================================================

JAZZMIN_SETTINGS = {
    "site_title": "لوحة التحكم",
    # "site_header": "متزان",
    # "site_brand": "متزان",
    # "site_logo": "images/mutazan.svg",  
    # "login_logo": "images/mutazan.svg",
    "custom_css": "css/main.css",
    "custom_js": "common/js/custom.js",
    "welcome_sign": "مرحبًا بك في لوحة التحكم",
   
    
    # "search_model": ["auth.User", "mutazan.YourModel"],
    "topmenu_links": [
        # {"name": "الرئيسية", "url": "admin:index", "permissions": ["auth.view_user"]},
        # {"name": "الدعم الفني", "url": "https://support.example.com", "new_window": True},
        # {"model": "auth.User"},
        # {"app": "mutazan"},
    ],
     
    "show_sidebar": True,  # التأكد من عرض الشريط الجانبي
    "navigation_expanded": True,  # بقاء القائمة الجانبية مفتوحة بشكل افتراضي
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "mutazan.YourModel": "fas fa-box",
    },



    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {"auth.user": "collapsible"},
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,
    "language_chooser": True,  # السماح بتغيير اللغة من داخل اللوحة
    "show_ui_builder": False,  # إخفاء خيار تعديل الواجهة للمستخدمين العاديين
    "user_avatar": "image",  # تحديد حقل الصورة في نموذج المستخدم

    "custom_links": {
        "companies_manager": [  # اسم التطبيق
            {
                "name": "سجل الشركات",
                "url": "/companies/",  # تأكد من أن هذا هو المسار الصحيح للعرض (view) الخاص بك
                "icon": "fas fa-building",
                # "permissions": ["mutazan_companies.view_company"],  # يمكنك تخصيص الصلاحيات
            }
        ]
    },

}

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,  # تعطيل النص الصغير في الهيدر
    "navbar_fixed": True,  # تثبيت الهيدر في أعلى الصفحة
    "sidebar_fixed": True,
    "footer_fixed": True,
    "theme": "darkly",  # يمكنك اختيار سمات مختلفة مثل "default", "darkly", "cosmo", "flatly", إلخ
    "actions_sticky_top": True,  # إبقاء أزرار الإجراءات مثبتة
    "right_sidebar": True,
        "usermenu_links": [
        {"model": "auth.user"},
        {"name": "الإشعارات", "url": "/notifications/", "icon": "fas fa-bell"},
        {"name": "الرسائل", "url": "/messages/", "icon": "fas fa-envelope"},
        {"name": "ملء الشاشة", "url": "#", "icon": "fas fa-expand-arrows-alt"},
    ],
    "extrahead": [
        '<link rel="stylesheet" href="{% static "css/custom_admin.css" %}">',  # ربط CSS المخصص
    ],

}


# ==================================================================
# ==================================================================

INSTALLED_APPS = SHARED_APPS + [
    app for app in TENANT_APPS if app not in SHARED_APPS
]

SITE_ID = 1

MIDDLEWARE = [
    'django_tenants.middleware.main.TenantMainMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django_htmx.middleware.HtmxMiddleware',
]

ROOT_URLCONF = 'Mutazan_weight.urls'
PUBLIC_SCHEMA_URLCONF = 'Mutazan_weight.urls_public'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'templates' ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Mutazan_weight.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': 'tenants_db',  # اسم قاعدة البيانات
        'HOST': 'localhost',
        'PORT': '5432',
        'USER': 'postgres',
        'PASSWORD':'770785807',
    }
}

DATABASE_ROUTERS = (
    'django_tenants.routers.TenantSyncRouter',
)

TENANT_MODEL = "companies_manager.Company"
TENANT_DOMAIN_MODEL = "companies_manager.Domain"
SHOW_PUBLIC_IF_NO_TENANT_FOUND = True


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/
ASE_DIR = Path(__file__).resolve().parent.parent
STATIC_URL = 'static/'
# STATICFILES_DIRS = [ BASE_DIR / 'static' ]
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / "static",  # مجلد static الرئيسي
    BASE_DIR.parent / "books/static",  # مجلد ثانوي للصور إن كان بجانب المشروع
]


MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media' 

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
