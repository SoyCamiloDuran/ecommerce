from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FixedPriceCoupon, PercentageCoupon
from .serializers import FixedPriceCouponSerializer, PercentageCouponSerializer


class CheckCouponView(APIView):
    def get(self, request, format=None):
        try:
            coupon_name = request.query_params.get('coupon_name')

            if FixedPriceCoupon.objects.filter(name=coupon_name).exists():
                coupon = FixedPriceCoupon.objects.get(name=coupon_name)
                coupon = FixedPriceCouponSerializer(coupon)

                return Response(
                    {'coupon': coupon.data},
                    status=status.HTTP_200_OK
                )
            elif PercentageCoupon.objects.filter(name=coupon_name).exists():
                coupon = PercentageCoupon.objects.get(name=coupon_name)
                coupon = PercentageCouponSerializer(coupon)

                return Response(
                    {'coupon': coupon.data},
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {'error': 'Código de cupón no encontrado.'},
                    status=status.HTTP_404_NOT_FOUND
                )
        except:
            return Response(
                {'error': 'Algo salió mal al verificar el cupón.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )