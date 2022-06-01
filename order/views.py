from django.conf import settings
from django.contrib.auth.models import User
from django.http import Http404

from django.shortcuts import render

from rest_framework import status,authentication,permissions
from rest_framework.decorators import api_view, authentication_classes,permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Order,OrderItem
from .serializers import OrderSerializer,MyOrderSerializer



@api_view(['POST'])
def checkout(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        flutterwave.api.key = settings.FLUTTERWAVE_SECRET_KEY
        # paid_amount = sum(item.get('quantity')*item.get('product').price for item in serializer.validated_data['items'])
        paid_amount = sum(['items'])

        try:
            charge = flutterwave.charge.create(
                amount = int(paid_amount),
                currency='Ugx',
                description='Charge from Owinoonline',
                source=serializer.validated_data['flutterwave_token']
            )

            serializer.save(user=request.user,paid_amount=paid_amount)

            return Response(serializer.data,status=status.HTTP_201_CRAETED)

        except Exception:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
