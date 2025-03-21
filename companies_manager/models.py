from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import connection, transaction, IntegrityError
from django_tenants.utils import schema_context

User = get_user_model()  # 🔥 جلب نموذج المستخدم الصحيح

class Company(TenantMixin):
    company_name = models.CharField(
        max_length=100,
        verbose_name="اسم الشركة",
        validators=[RegexValidator(r'^[\D]+$', message="يجب ألا يحتوي على أرقام")]
    )
    business_type = models.CharField(max_length=255, verbose_name="نوع النشاط")
    registration_number = models.PositiveIntegerField(unique=True, verbose_name="رقم السجل التجاري")
    country = models.CharField(
        max_length=100, 
        verbose_name="الدولة",
        validators=[RegexValidator(r'^[\D]+$', message="يجب ألا يحتوي على أرقام")]
    )
    address = models.CharField(max_length=255, verbose_name="العنوان")
    phone_number = models.CharField(
        max_length=15,
        verbose_name="رقم الهاتف",
        validators=[RegexValidator(r'^\d+$', message="يجب أن يحتوي على أرقام فقط")]
    )
    email = models.EmailField(unique=True, verbose_name="البريد الإلكتروني")
    logo = models.ImageField(upload_to="company_logos/%Y/%m/%d", verbose_name="شعار الشركة")
    employees_count = models.PositiveIntegerField(verbose_name="عدد الموظفين")
    founded_date = models.DateField(verbose_name="تاريخ التأسيس")
    services_offered = models.TextField(verbose_name="الخدمات المقدمة")
    port_license_number = models.PositiveIntegerField(unique=True, verbose_name="تصريح العمل بالميناء")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")

    # 🔥 المسؤول الإداري المرتبط بالشركة (يجب أن يكون موجودًا مسبقًا في النظام الرئيسي)
    admin_user = models.OneToOneField(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        verbose_name="المسؤول الإداري"
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "الشركات"

    def save(self, *args, **kwargs):
        """ عند حفظ Tenant جديد، يتم إنشاء الأسكيما وإضافة المستخدم الإداري إليها """
        is_new = self._state.adding  # التحقق مما إذا كان الكائن جديدًا أم لا
        
        # ✅ تعطيل القيود أثناء تنفيذ الحفظ
        with connection.cursor() as cursor:
            cursor.execute("SET CONSTRAINTS ALL DEFERRED;")  # تعطيل القيود مؤقتًا
            
        super().save(*args, **kwargs)  # حفظ الشركة أولاً

        if is_new:
            base_domain = f"{self.company_name.lower()}.localhost"
            domain_name = base_domain
            counter = 1

            while Domain.objects.filter(domain=domain_name).exists():
                domain_name = f"{self.company_name.lower()}{counter}.localhost"
                counter += 1

            try:
                Domain.objects.create(tenant=self, domain=domain_name, is_primary=True)
            except IntegrityError:
                print("❌ فشل إنشاء الدومين بسبب خطأ في النزاهة.")

            if self.admin_user:
                with schema_context(self.schema_name):  
                    if not User.objects.filter(username=self.admin_user.username).exists():
                        tenant_admin = User.objects.create_superuser(
                            username=self.admin_user.username,
                            email=self.admin_user.email,
                            password="Admin@123"
                        )
                        tenant_admin.is_staff = True
                        tenant_admin.is_superuser = True
                        tenant_admin.is_active = True
                        tenant_admin.save()

        # ✅ إعادة تفعيل القيود بعد التنفيذ
        with connection.cursor() as cursor:
            cursor.execute("SET CONSTRAINTS ALL IMMEDIATE;")

    def delete(self, *args, **kwargs):
        """ حذف الشركة مع الأسكيما الخاصة بها من قاعدة البيانات """
        schema_name = self.schema_name  # الاحتفاظ باسم الأسكيما قبل الحذف

        # ✅ حذف الدومينات المرتبطة
        self.domains.all().delete()

        # ✅ حذف الأسكيما من قاعدة البيانات
        with connection.cursor() as cursor:
            cursor.execute(f"DROP SCHEMA IF EXISTS {schema_name} CASCADE")

        # ✅ حذف الشركة من الجدول الأساسي
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"{self.company_name}"  # عرض اسم الشركة
# عرض اسم الشركة

class Domain(DomainMixin):
    tenant = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="domains")  # ربط الدومين بالمستأجر
    domain = models.CharField(max_length=255, unique=True)  # التأكد من أن كل دومين فريد
    
    def __str__(self):
        return self.domain



# -----------------------------------------------------------
#  ------------------------نوع المخالفات----------------------------

class ViolationsType(models.Model):
    name = models.CharField(max_length=255, verbose_name="اسم المخالفة")  # مثل "تجاوز الوزن القانوني"
    description = models.TextField(verbose_name="وصف المخالفة", null=True, blank=True)  # تفاصيل إضافية عن المخالفة
    penalty_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="قيمة الغرامة")  # قيمة الغرامة المالية
    violation_code = models.CharField(max_length=50, unique=True, verbose_name="رمز المخالفة")  # رمز فريد لكل مخالفة
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")  # متى أُضيفت المخالفة
    updated_at = models.DateTimeField(auto_now=True, verbose_name="آخر تحديث")  # متى تم تعديلها آخر مرة

    class Meta:
        verbose_name = "نوع المخالفة"
        verbose_name_plural = "أنواع المخالفات"

    def __str__(self):
        return self.name

# -----------------------------------------------------------
#  ---------------------------------------------------

class TransferredWeightCard(models.Model):
    name = models.CharField(max_length=255, verbose_name="اسم الشركة")
    plate_number = models.CharField(max_length=50, verbose_name="رقم اللوحة")
    empty_weight = models.DecimalField(max_digits=10, decimal_places=5, verbose_name="الوزن الفارغ", null=True, blank=True)
    loaded_weight = models.DecimalField(max_digits=10, decimal_places=5, verbose_name="الوزن المحمل", null=True, blank=True)
    net_weight = models.DecimalField(max_digits=10, decimal_places=5, verbose_name="الوزن الصافي", null=True, blank=True)
    driver_name = models.CharField(max_length=255, verbose_name="اسم السائق", null=True, blank=True)
    entry_date = models.DateTimeField(null=True, blank=True, verbose_name="تاريخ الدخول")
    exit_date = models.DateTimeField(null=True, blank=True, verbose_name="تاريخ الخروج")
    quantity = models.DecimalField(max_digits=10, decimal_places=5, verbose_name="الكمية", null=True, blank=True)
    material = models.CharField(max_length=255, verbose_name="المادة", null=True, blank=True)
    status = models.CharField(max_length=50, verbose_name="حالة البطاقة")

    class Meta:
        verbose_name = "بطاقة وزن منقولة"
        verbose_name_plural = "بطاقات وزن منقولة"