from django.urls import path
from . import views
from .views import CompanyListAPIView, CompanyDetailView, CustomTokenObtainPairView, LoginView

urlpatterns = [
    #     path('companies/', views.company_list, name='company_list'),
    # path('companies/<int:company_id>/', views.company_detail, name='company_detail'),
    path('company/<int:company_id>/', views.company_weight_cards, name='company_weight_cards'),
    path('companies/', CompanyListAPIView.as_view(), name='company-list'),  # عرض أو إضافة الشركات
    path('companies/<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),  # تفاصيل الشركة أو تعديلها أو حذفها
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),

    
]