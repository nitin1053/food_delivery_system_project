# services.py

from delivery.models import Pricing


class PriceCalculator:
    @staticmethod
    def calculate_price(organization_id, zone, total_distance, item_type):
        pricing = Pricing.objects.filter(
            organization_id=organization_id,
            zone=zone,
            item__type=item_type
        ).first()

        if pricing:
            base_price = pricing.fixed_price * 100  # Converting to cents
            extra_distance = max(total_distance - pricing.base_distance_in_km, 0)
            extra_price = extra_distance * pricing.km_price * 100  # Converting to cents

            total_price_in_cents = base_price + extra_price
            total_price = total_price_in_cents / 100  # Converting back to euros

            return total_price
        else:
            return None
