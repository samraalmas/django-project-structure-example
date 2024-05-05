from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Orders

class OrdersByUserOrDevice(APIView):
    def get(self, request):
        user_id = request.GET.get('user_id')
        device_id = request.GET.get('device_id')
        
        if user_id:
            orders = Orders.objects.filter(boo__id=user_id)
        elif device_id:
            orders = Orders.objects.filter(device_id__id=device_id)
        else:
            return Response("Please provide either user_id or device_id in the query parameters", status=status.HTTP_400_BAD_REQUEST)
        print(orders,"orders")
        serialized_orders = []
        for order in orders:
            serialized_orders.append({
                'name': order.name,
                'user_id': order.boo.id
            })
        
        return Response(serialized_orders)
