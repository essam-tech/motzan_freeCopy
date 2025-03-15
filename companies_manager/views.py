from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django_tenants.utils import schema_context
from .models import Company
# companies_manager/views.py
from django.shortcuts import render, get_object_or_404
from companies_manager.models import Company, TransferredWeightCard

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

# def company_list(request):
#     companies = Company.objects.all()
#     return render(request, 'companies/company_list.html', {'companies': companies})

# def company_detail(request, company_id):
#     company = get_object_or_404(Company, id=company_id)
#     weight_cards = WeightCard.objects.filter(company=company)  # جلب بطاقات الوزن الخاصة بالشركة
    
#     context = {
#         'company': company,
#         'weight_cards': weight_cards,
#     }
#     return render(request, 'companies/company_detail.html', context)
    