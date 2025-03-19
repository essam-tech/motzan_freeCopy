from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django_tenants.utils import schema_context
from .models import Company
# companies_manager/views.py
from django.shortcuts import render, get_object_or_404
from companies_manager.models import Company, TransferredWeightCard
# هذا الملف يحتوي على الـ Views الخاصة بالـ API لشركات

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .Serializer import CompanySerializer
from .models import Company
from django.http import Http404
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username  # يمكنك إضافة بيانات إضافية هنا
        return token

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

#----------------------كلاس الapi----------------------
# عرض قائمة الشركات أو إضافة شركة جديدة
class CompanyListAPIView(APIView):
    def get(self, request, format=None):
        companies = Company.objects.all()  # جلب كل الشركات
        serializer = CompanySerializer(companies, many=True)  # تحويل البيانات إلى JSON
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CompanySerializer(data=request.data)  # تحويل البيانات القادمة من المستخدم
        if serializer.is_valid():
            serializer.save()  # حفظ الشركة الجديدة
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# عرض تفاصيل شركة معينة أو تعديلها أو حذفها
class CompanyDetailView(APIView):
    def get_object(self, pk):
        try:
            return Company.objects.get(pk=pk)  # جلب الشركة بناءً على ID
        except Company.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        company = self.get_object(pk)
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        company = self.get_object(pk)
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()  # حفظ التعديلات
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        company = self.get_object(pk)
        company.delete()  # حذف الشركة
        return Response(status=status.HTTP_204_NO_CONTENT)
#---------------------------نهايه كلاس الapi-------------

def company_weight_cards(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    
    # جلب البيانات المنقولة لعرضها
    transferred_cards = TransferredWeightCard.objects.filter(company_name=company.name)
    print(f"تم العثور على {transferred_cards.count()} بطاقة وزن منقولة.")  # للتحقق من البيانات
    
    return render(request, 'companies/company_detail.html', {  # المسار الصحيح للقالب
        'company': company,
        'transferred_cards': transferred_cards,
    })

class CustomLoginView(LoginView):
    template_name = "login.html"  # تحديد قالب صفحة تسجيل الدخول

    def form_valid(self, form):
        """ التحقق من أن المستخدم هو المسؤول الإداري لشركة معينة """
        user = form.get_user()
        try:
            tenant = Company.objects.get(admin_user=user)

            # ✅ تبديل Schema إلى الشركة الخاصة به
            with schema_context(tenant.schema_name):
                return super().form_valid(form)  # تسجيل الدخول باستخدام `LoginView`
        except Company.DoesNotExist:
            form.add_error(None, "ليس لديك صلاحية الدخول.")
            return self.form_invalid(form)  # إرجاع خطأ للمستخدم
    
    def get_success_url(self):
        """ إعادة التوجيه بعد تسجيل الدخول """
        return "/dashboard/"  # يمكنك تغييرها إلى المسار المناسب


    