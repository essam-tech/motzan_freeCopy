from django.urls import path
from . import views
from .views import CompanyListAPIView, CompanyDetailView

urlpatterns = [
    #     path('companies/', views.company_list, name='company_list'),
    # path('companies/<int:company_id>/', views.company_detail, name='company_detail'),
    path('company/<int:company_id>/', views.company_weight_cards, name='company_weight_cards'),
    path('companies/', CompanyListAPIView.as_view(), name='company-list'),  # عرض أو إضافة الشركات
    path('companies/<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),  # تفاصيل الشركة أو تعديلها أو حذفها
    
]