# هذا الملف يحتوي على Serializer لتحويل بيانات الشركة إلى JSON عند استخدام API

from rest_framework import serializers
from companies_manager.models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'  # تحديد الحقول التي سيتم تضمينها في الـ API

