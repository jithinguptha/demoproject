from cart.models import cart


def total_count(request):
    count=0
    u=request.user
    try:
        c = cart.objects.filter(user=u)
        for i in c:
            count+=i.quantity

    except:
        count=0
    return {'count':count}

