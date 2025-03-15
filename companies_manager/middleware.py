from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
from companies_manager.models import Tenant

class TenantMiddleware(MiddlewareMixin):
    def process_request(self, request):
        domain = request.get_host().split(':')[0]  # استخراج الدومين بدون البورت
        try:
            request.tenant = Tenant.objects.get(domain=domain)  # البحث عن المستأجر
        except Tenant.DoesNotExist:
            return redirect('/')  # إعادة التوجيه للصفحة الرئيسية
