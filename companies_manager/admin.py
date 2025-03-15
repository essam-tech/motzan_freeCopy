from django.contrib import admin
from django.contrib.auth.models import User, Group  # استيراد النماذج المدمجة
from .models import *  # استيراد باقي النماذج مثل Tenant و Domain

# class CompanyAdmin(admin.ModelAdmin):
#     list_display = ("company_name", "admin_user", "created_at")
#     search_fields = ("company_name", "admin_user__username")
#     list_filter = ("country", "business_type")
#     autocomplete_fields = ["admin_user"]

#     def get_queryset(self, request):HK:
#         qs = super().get_queryset(request)
#         if request.user.is_superuser:
#             return qs  # السوبر أدمن يرى جميع الشركات
#         return qs.filter(admin_user=request.user)  # الأدمن يرى شركته فقط

# admin.site.register(Company, CompanyAdmin)

# @admin.register(ViolationsType)
# class ViolationsTypeAdmin(admin.ModelAdmin):
#     list_display = ['name', 'description', 'penalty_amount', 'violation_code', 'created_at', 'updated_at']
#     search_fields = ['name']
#     date_hierarchy = 'created_at'


class TenantAdminSete(admin.AdminSite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # تسجيل النماذج الخاصة بالمستأجرين
        self.register(Company)
        self.register(ViolationsType)
        self.register(Domain)

        # تسجيل نماذج المستخدمين والمجموعات
        self.register(User)  # جدول المستخدمين
        self.register(Group)  # جدول المجموعات

# إنشاء كائن من لوحة الإدارة المخصصة
tenant_admin_site = TenantAdminSete(name="tenant_admin_site")
