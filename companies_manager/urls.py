from django.urls import path
from . import views

urlpatterns = [
    #     path('companies/', views.company_list, name='company_list'),
    # path('companies/<int:company_id>/', views.company_detail, name='company_detail'),
    path('company/<int:company_id>/', views.company_weight_cards, name='company_weight_cards'),
]