# companies_manager/utils.py
from django_tenants.utils import tenant_context
from system_companies.models import WeightCard
from companies_manager.models import TransferredWeightCard

def transfer_weight_cards(company):
    with tenant_context(company):
        # جلب جميع بطاقات الوزن من schema الشركة
        weight_cards = WeightCard.objects.all()
        print(f"تم العثور على {weight_cards.count()} بطاقة وزن في schema الشركة.")

        # نسخ البيانات إلى النظام الرئيسي
        for card in weight_cards:
            print(f"نقل بطاقة الوزن: {card.id} - {card.plate_number}")
            TransferredWeightCard.objects.create(
                company_name=company.company_name,  # استخدام الحقل الصحيح
                plate_number=card.plate_number.plate_number,
                empty_weight=card.empty_weight,
                loaded_weight=card.loaded_weight,
                net_weight=card.net_weight,
                driver_name=card.driver_name.driver_name if card.driver_name else None,
                entry_date=card.entry_date,
                exit_date=card.exit_date,
                quantity=card.quantity,
                material=card.material.name_material if card.material else None,
                status=card.get_status_display(),
            )
        print("تم نقل جميع بطاقات الوزن بنجاح.")