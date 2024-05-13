from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.utils import timezone
from coupons.models import Coupon
from coupons.forms import CouponApplyForm
import json

# @require_POST
def coupon_apply(request):
    data = json.loads(request.body)
    now = timezone.now()
    coupon_code = data['coupon']
    
    # coupon = request.POST['coupon']
    
    # try:
    #     coupon = Coupon.objects.get(code=coupon,
    #                                 valid_from__lte=now,
    #                                 valid_to__gte=now,
    #                                 active=True)
    #     request.session['coupon_id'] = coupon.id
        
    # except:
    #     request.session['coupon_id'] = None            
    # return redirect('home')
    return JsonResponse({"result": True})
