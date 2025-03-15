# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Devices, Device_Settings, Connection

# @receiver(post_save, sender=Devices)
# def create_device_settings(sender, instance, created, **kwargs):
#     if created:
#         # الحصول على نوع الاتصال المرتبط بالجهاز
#         connection_type = instance.connection_type  # الحصول على الاتصال المرتبط بالجهاز
        
#         # تخصيص الإعدادات بناءً على نوع الاتصال
#         if connection_type.connection_name == 'WiFi':
#             # إذا كان الاتصال WiFi
#             Device_Settings.objects.create(
#                 device_type=instance,
#                 connection_type=connection_type,
#                 port_number="N/A",  # لا يوجد منفذ لـ WiFi
#                 baud_rate="N/A",  # لا يوجد معدل باود لـ WiFi
#                 initialization_data_size=8,
#                 number_of_initialization_bits=1,
#                 parity_type="None",
#                 flow_control="None",
#                 number_of_digits_after_decimal_point=2
#             )
#         elif connection_type.connection_name == 'Serial':
#             # إذا كان الاتصال Serial
#             Device_Settings.objects.create(
#                 device_type=instance,
#                 connection_type=connection_type,
#                 port_number="COM1",  # تعيين المنفذ الافتراضي
#                 baud_rate="9600",  # تعيين معدل الباود الافتراضي
#                 initialization_data_size=8,
#                 number_of_initialization_bits=1,
#                 parity_type="None",
#                 flow_control="RTS/CTS",
#                 number_of_digits_after_decimal_point=2
#             )
#         elif connection_type.connection_name == 'USB':
#             # إذا كان الاتصال USB
#             Device_Settings.objects.create(
#                 device_type=instance,
#                 connection_type=connection_type,
#                 port_number="N/A",  # لا يوجد منفذ لـ USB
#                 baud_rate="N/A",  # لا يوجد معدل باود لـ USB
#                 initialization_data_size=8,
#                 number_of_initialization_bits=1,
#                 parity_type="None",
#                 flow_control="None",
#                 number_of_digits_after_decimal_point=2
#             )
#         elif connection_type.connection_name == 'API':
#             # إذا كان الاتصال API
#             Device_Settings.objects.create(
#                 device_type=instance,
#                 connection_type=connection_type,
#                 port_number="N/A",  # لا يوجد منفذ لـ API
#                 baud_rate="N/A",  # لا يوجد معدل باود لـ API
#                 initialization_data_size=8,
#                 number_of_initialization_bits=1,
#                 parity_type="None",
#                 flow_control="None",
#                 number_of_digits_after_decimal_point=2
#             )




















# # from django.db.models.signals import post_save
# # from django.dispatch import receiver
# # from django.contrib.auth.models import User
# # from django.core.mail import send_mail
# # from django.conf import settings
# # from .models import Company

# # @receiver(post_save, sender=Company)
# # def create_company_admin(sender, instance, created, **kwargs):
# #     """
# #     عند إنشاء شركة جديدة، يتم تلقائيًا إنشاء حساب "أدمن الشركة"
# #     وربطه بالشركة وإرسال بريد إلكتروني يحتوي على تفاصيل الحساب.
# #     """
# #     if created:
# #         # إنشاء مستخدم مسؤول عن الشركة
# #         admin_user = User.objects.create_user(
# #             username=instance.email,
# #             email=instance.email,
# #             password='CompanyAdmin123'  # يمكنك استخدام كلمة مرور عشوائية
# #         )
# #         admin_user.is_staff = True  # جعله أدمن في النظام
# #         admin_user.save()

# #         # ربط المستخدم بالشركة
# #         instance.admin_user = admin_user
# #         instance.save()

# #         # إرسال بريد إلكتروني يحتوي على بيانات الحساب
# #         send_mail(
# #             subject="تم إنشاء حساب الأدمن لشركتك",
# #             message=f"مرحبًا {instance.name}،\n\nتم إنشاء حساب الأدمن الخاص بشركتك.\n\n"
# #                     f"اسم المستخدم: {instance.email}\n"
# #                     f"كلمة المرور: CompanyAdmin123\n\n"
# #                     "يرجى تغيير كلمة المرور عند تسجيل الدخول لأول مرة.",
# #             from_email=settings.DEFAULT_FROM_EMAIL,
# #             recipient_list=[instance.email],
# #             fail_silently=False,
# #         )
