# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Pricing
from .services import PriceCalculator

class DeliveryCostAPIView(APIView):
    def post(self, request):
        zone = request.data.get('zone')
        organization_id = request.data.get('organization_id')
        total_distance = request.data.get('total_distance')
        item_type = request.data.get('item_type')

        if not all([zone, organization_id, total_distance, item_type]):
            return Response({'error': 'Missing required parameters'}, status=400)

        total_price = PriceCalculator.calculate_price(organization_id, zone, total_distance, item_type)
        
        if total_price is not None:
            
            return Response({'total_price': total_price})
        else:
            return Response({'error': 'Pricing not found'}, status=404)
        
    def get(self, request):
        pricing_statements = Pricing.objects.all()
        response_data = []

        for statement in pricing_statements:
            payload = {
                'organization_id': statement.organization_id,
                'zone': statement.zone,
                'total_distance': statement.base_distance_in_km + 5,  # Example total distance
                'item_type': statement.item.type
            }

            total_price = PriceCalculator.calculate_price(statement.organization_id, statement.zone, payload['total_distance'], payload['item_type'])

            if total_price is not None:
                response_data.append({
                    'payload': payload,
                    'response': {'total_price': total_price}
                })
            else:
                response_data.append({
                    'payload': payload,
                    'response': {'error': 'Pricing not found'}
                })

        return Response(response_data)

    